"""Private business oracles, mounted only after subject execution has ended."""
import tempfile
import unittest
from pathlib import Path
from app import connect, list_changes, propose_change, publish_change, rate_on

REVIEWER = {'tenant': 'Org-A', 'role': 'reviewer'}
APPROVER = {'tenant': 'Org-A', 'role': 'approver'}


def candidate(change_id='c1', rate=1300, version='addendum:v2', span='s1', quote='Commission: 13%.'):
    return {'id': change_id, 'treaty': 'T-42', 'section': 'property', 'rate': rate,
            'start': '2026-11-01', 'end': '2026-12-01',
            'source': {'document_version': version, 'page_id': version + ':p1',
                       'span_id': span, 'quote': quote}}


class CommissionContract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.conn = connect(Path(self.tmp.name) / 'portal.db')
        self.addCleanup(self.conn.close)

    def rate(self, day='2026-11-01', section='property'):
        return rate_on(self.conn, REVIEWER, 'T-42', section, day)

    def test_pending_change_never_publishes(self):
        propose_change(self.conn, REVIEWER, candidate())
        self.assertEqual(self.rate(), 1250)
        self.assertEqual(list_changes(self.conn, REVIEWER, 'T-42', 'property')[0]['status'], 'pending')

    def test_roles_and_tenants_are_business_boundaries(self):
        propose_change(self.conn, REVIEWER, candidate())
        for actor in (REVIEWER, {'tenant': 'Org-B', 'role': 'approver'}):
            with self.subTest(actor=actor), self.assertRaises((PermissionError, KeyError)):
                publish_change(self.conn, actor, 'c1')
        self.assertEqual(list_changes(self.conn, {'tenant': 'Org-B', 'role': 'reviewer'}, 'T-42', 'property'), [])
        self.assertEqual(self.rate(), 1250)

    def test_source_reference_and_quote_are_verified(self):
        for key, value in (('span_id', 'missing'), ('page_id', 'wrong-page'), ('quote', 'Invented evidence')):
            change = candidate()
            change['source'][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                propose_change(self.conn, REVIEWER, change)
        self.assertEqual(list_changes(self.conn, REVIEWER, 'T-42', 'property'), [])

    def test_unsigned_later_upload_cannot_publish(self):
        propose_change(self.conn, REVIEWER, candidate())
        draft = candidate('draft', 1400, 'addendum:v3', quote='Commission: 14%.')
        propose_change(self.conn, REVIEWER, draft)
        with self.assertRaises(ValueError):
            publish_change(self.conn, APPROVER, 'draft')
        publish_change(self.conn, APPROVER, 'c1')
        self.assertEqual(self.rate(), 1300)
        self.assertEqual(len(list_changes(self.conn, REVIEWER, 'T-42', 'property')), 2)

    def test_effective_interval_and_unaffected_section(self):
        propose_change(self.conn, REVIEWER, candidate())
        publish_change(self.conn, APPROVER, 'c1')
        for day, expected in (('2026-10-31', 1250), ('2026-11-01', 1300),
                              ('2026-11-30', 1300), ('2026-12-01', 1250)):
            with self.subTest(day=day):
                self.assertEqual(self.rate(day), expected)
        self.assertEqual(self.rate(section='casualty'), 1000)

    def test_invalid_rate_and_dates_do_not_mutate_history(self):
        for patch in ({'rate': None}, {'rate': -1}, {'rate': 10001}, {'end': '2026-11-01'},
                      {'start': 'not-a-date'}):
            change = candidate()
            change.update(patch)
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                propose_change(self.conn, REVIEWER, change)
        self.assertEqual(list_changes(self.conn, REVIEWER, 'T-42', 'property'), [])
        self.assertEqual(self.rate(), 1250)
        for rate, span, quote in ((0, 's0', 'Commission: 0%.'), (10000, 's100', 'Commission: 100%.')):
            change = candidate('boundary-' + str(rate), rate, 'endorsement:v1', span, quote)
            self.assertEqual(propose_change(self.conn, REVIEWER, change)['status'], 'pending')
        self.assertEqual(self.rate(), 1250)

    def test_retry_is_idempotent_but_id_reuse_cannot_rewrite(self):
        for _ in range(2):
            self.assertEqual(propose_change(self.conn, REVIEWER, candidate())['id'], 'c1')
        changed = candidate(rate=1500)
        with self.assertRaises(ValueError):
            propose_change(self.conn, REVIEWER, changed)
        for _ in range(2):
            publish_change(self.conn, APPROVER, 'c1')
        self.assertEqual(len(list_changes(self.conn, REVIEWER, 'T-42', 'property')), 1)
        self.assertEqual(self.rate(), 1300)

    def test_signed_conflict_requires_reason_and_keeps_alternatives(self):
        propose_change(self.conn, REVIEWER, candidate())
        other = candidate('c2', 1500, 'endorsement:v1', 's2', 'Commission: 15%.')
        propose_change(self.conn, REVIEWER, other)
        with self.assertRaises(ValueError):
            publish_change(self.conn, APPROVER, 'c1')
        self.assertEqual(self.rate(), 1250)
        publish_change(self.conn, APPROVER, 'c1', reason='Underwriting selected signed addendum v2')
        records = list_changes(self.conn, REVIEWER, 'T-42', 'property')
        self.assertEqual({r['id'] for r in records}, {'c1', 'c2'})
        self.assertEqual(next(r for r in records if r['id'] == 'c1')['source'], candidate()['source'])
        self.assertEqual(self.rate(), 1300)


if __name__ == '__main__':
    unittest.main(verbosity=2)
