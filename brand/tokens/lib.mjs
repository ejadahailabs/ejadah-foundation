// Shared helpers for the token scripts. No dependencies: Node 18+ only.
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

export const here = dirname(fileURLToPath(import.meta.url));
export const tokens = JSON.parse(readFileSync(join(here, "tokens.json"), "utf8"));

/** Resolve a token path like "gold", "ink.raised" or "status.built.dark" to a hex value. */
export function resolve(path) {
  const parts = path.split(".");
  let node = tokens.color[parts[0]];
  for (const p of parts.slice(1)) node = node?.[p];
  if (node && typeof node === "object" && "DEFAULT" in node) node = node.DEFAULT;
  if (node && typeof node === "object" && "value" in node) node = node.value;
  if (typeof node !== "string" || !/^#[0-9A-Fa-f]{6}$/.test(node)) {
    throw new Error(`Token "${path}" does not resolve to a #RRGGBB colour`);
  }
  return node;
}

/** WCAG 2.2 relative luminance and contrast ratio. */
function luminance(hex) {
  const [r, g, b] = [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16) / 255)
    .map((v) => (v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
export function contrast(a, b) {
  const [x, y] = [luminance(a), luminance(b)];
  return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
}

/** The thresholds, the same ones Sanad's picture theme enforces. */
export const MIN = { text: 4.5, large: 3, graphic: 3 };
