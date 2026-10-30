// Optional syntax check. Copy into an isolated npm scratch directory with
// mermaid@11.17.2 and jsdom@26.1.0 installed, then pass .mmd paths as arguments.
// Does not render or validate architectural meaning.
import {JSDOM} from 'jsdom';
import fs from 'node:fs';
const dom = new JSDOM('<!doctype html><html><body></body></html>');
globalThis.window = dom.window;
globalThis.document = dom.window.document;
const {default: mermaid} = await import('mermaid');
for (const path of process.argv.slice(2)) {
  await mermaid.parse(fs.readFileSync(path, 'utf8'));
  console.log('Parsed:', path);
}
