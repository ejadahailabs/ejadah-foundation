#!/usr/bin/env node
// Proves every colour pair the brand allows meets its WCAG threshold, and that the
// pairs the brand forbids really do fail (so the check cannot pass by being lenient).
// Exit 0 = all good. Exit 1 = a failure, named.
//
//   node brand/tokens/check-contrast.mjs            # check
//   node brand/tokens/check-contrast.mjs --verbose  # also print every ratio
import { tokens, resolve, contrast, MIN } from "./lib.mjs";

const verbose = process.argv.includes("--verbose");
const failures = [];
let checked = 0;

function check(fg, bg, kind, label = `${fg} on ${bg}`) {
  const ratio = contrast(fg, bg);
  checked++;
  const ok = ratio >= MIN[kind];
  if (verbose) console.log(`${ok ? "ok  " : "FAIL"} ${ratio.toFixed(2).padStart(5)}:1  ${kind.padEnd(7)} ${label}`);
  if (!ok) failures.push(`${label}: ${ratio.toFixed(2)}:1, needs ${MIN[kind]}:1 (${kind})`);
}

const c = tokens.contrast;
for (const kind of ["text", "large", "graphic"]) {
  for (const [fg, bg] of c[kind]) check(resolve(fg), resolve(bg), kind, `${fg} on ${bg}`);
}

// The diagram kinds: text on fill is body text, stroke on the ground is a graphic.
const grounds = { dark: { bg: resolve("ink"), fg: resolve("mist") }, light: { bg: resolve("paper"), fg: resolve("paper.text") } };
for (const [kind, spec] of Object.entries(tokens.color.diagram)) {
  if (kind.startsWith("$")) continue;
  for (const mode of ["dark", "light"]) {
    const { fill, stroke } = spec[mode];
    check(grounds[mode].fg, fill, "text", `diagram.${kind}.${mode}: text on fill`);
    check(stroke, grounds[mode].bg, "graphic", `diagram.${kind}.${mode}: stroke on ground`);
  }
}

// The negative controls. If one of these passes, the check has gone soft.
for (const [fg, bg, kind, why] of c.mustFail) {
  const ratio = contrast(resolve(fg), resolve(bg));
  checked++;
  const failsAsExpected = ratio < MIN[kind];
  if (verbose) console.log(`${failsAsExpected ? "ok  " : "FAIL"} ${ratio.toFixed(2).padStart(5)}:1  must-fail ${fg} on ${bg}`);
  if (!failsAsExpected) failures.push(`${fg} on ${bg} was expected to FAIL as ${kind} (${why}) but measures ${ratio.toFixed(2)}:1`);
}

if (failures.length) {
  console.error(`check-contrast: ${failures.length} of ${checked} checks failed`);
  for (const f of failures) console.error(`  - ${f}`);
  process.exit(1);
}
console.log(`check-contrast: ${checked} checks passed`);
