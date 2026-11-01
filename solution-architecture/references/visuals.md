# Visual architecture as a decision tool

Use a picture when relationships, timing or state are harder to follow in prose. First state the question and inspect the evidence. Choose one useful view, not every type.

| Question | View | Include |
|---|---|---|
| Who uses what, inside which scope? | System context | Actors, system scope, external dependencies |
| What runs/stores data, where? | Container/deployment | Applications/stores/deployables, trust and ownership boundaries |
| What depends on what? | Component/dependency | Responsibilities, direction, allowed interfaces |
| What happens, including failure? | Sequence | Requests, transactions, async steps, retries, human decisions |
| Where did a value come from? | Data flow | Transforms, immutable inputs, persistence, ownership/provenance |
| Which transitions are legal? | State | Trigger/guard, terminal/recovery states |
| What has identity/relationships? | ER/domain | Keys, cardinality, constraints and lifecycle |
| What changes and when? | Current/proposed comparison | Separate views/stages, migration and cutover |

C4 (Simon Brown) informs context/container/component views; a Mermaid flowchart is not a complete C4 model just because it has boxes. A container means an application/data store, not necessarily Docker. Use the repository's existing tools and editable source. Mermaid works for many repository viewers; supported syntax differs by renderer/version. Avoid experimental diagram types when basic flowchart/sequence/state/ER suffice.

## Procedure and validation

1. Title as Current (observed), Proposed, or Possible future. State source facts and assumptions.
2. Name responsibilities rather than technologies alone. Label relationships with action/data and sync/async where meaningful. Mark owner/trust boundary when it affects access or transactions.
3. Walk one concrete example through diagram and prose, including failure. Check identities, cardinalities, arrows, transaction/ack order and human decisions against contracts.
4. Validate syntax with an available renderer; inspect the image for readable labels, crossings and scale. Syntax success alone does not establish correct architecture.

The bundled `examples/extraction.mmd` is proposed data flow, not a claim about a repository. `examples/publication.mmd` shows stale review behavior. CLI help/version below were verified with Node 24.19.0, Mermaid CLI 11.12.0 and system Chromium. Rendering was attempted but blocked here: Chromium denied the CLI file URL with ERR_BLOCKED_BY_ADMINISTRATOR; no image render is claimed. Syntax was separately checked with Mermaid parse. The command is a reproducible attempt, not evidence of successful rendering. Recheck versions and Chromium availability in another environment; do not install tools merely for style.

```sh
command -v chromium
npx --yes --package @mermaid-js/mermaid-cli@11.12.0 mmdc --help
# From the installed skill directory; output is a local scratch artifact.
npx --yes --package @mermaid-js/mermaid-cli@11.12.0 mmdc \
  -p examples/puppeteer.json -i examples/extraction.mmd -o /tmp/extraction.svg
```

`puppeteer.json` selects `/usr/bin/chromium` with no platform-specific sandbox override. Use your permitted browser setup; do not weaken execution isolation to render. If unavailable, retain source, report “not rendered”, and validate manually without claiming a render. Diagram sources must agree with data/contracts, not just parse. The project validator checks local reference availability separately.

## Multi-document evidence walkthrough

The flow diagram separates immutable document+OCR versions from candidates, normalization, adjudication and publication. A value can have several supporting/conflicting candidates; human choice does not mutate OCR. A new OCR version creates new evidence identities, so old decisions remain reproducible. The sequence diagram distinguishes a human's old revision from the transaction that checks current state; an arrow labeled “publish” alone would hide lost-update risk. Sources: https://c4model.com/ and https://mermaid.js.org/; rendering instructions rely on the actual CLI probe, not an invented API.

For a browser-independent syntax check, the bundled `examples/validate.mjs`
uses Mermaid 11.17.2 (the resolved parser in the tested CLI dependency tree)
and JSDOM 26.1.0. In a scratch directory, install those exact packages, copy
`validate.mjs` there, and run `node validate.mjs /absolute/path/extraction.mmd
/absolute/path/publication.mmd`. It initializes a DOM before importing Mermaid;
plain Node import without a DOM fails in sanitization. This checks parsing only.

## Material behind the visual guidance

Read the relevant entry for its attributed idea, applicability, procedure and example; do not load all entries by default.

- [Architecture views, audience and visual communication](topics/visual-communication.md).
- [C4 context, container and component views](topics/c4-views.md).
