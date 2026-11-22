import json, re, sys, pathlib
brand = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); src = pathlib.Path(sys.argv[3])
T = json.loads((brand/"tokens/tokens.json").read_text()); C = T["color"]
def svgfile(name, w=None):
    s = (brand/"logos"/name).read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S); s = re.sub(r"<title>.*?</title>", "", s)
    if w: s = s.replace("<svg ", f'<svg width="{w}" height="{w}" style="width:{w}px;height:{w}px" ', 1)
    return s.strip()
def tpl(name, fills):
    s = (brand/"templates"/name).read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    for k, v in fills.items(): s = s.replace("{{" + k + "}}", v)
    s = re.sub(r"\{\{[^}]*\}\}", "", s)
    return s.strip()
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; c=[v/12.92 if v<=.03928 else ((v+.055)/1.055)**2.4 for v in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def ratio(a,b):
    x,y=lum(a),lum(b); return (max(x,y)+.05)/(min(x,y)+.05)
INK, PAPER = C["ink"]["DEFAULT"]["value"], C["paper"]["DEFAULT"]["value"]
sw = []
for group in ("ink","mist","gold","paper"):
    for key, v in C[group].items():
        if key.startswith("$"): continue
        hexv = v["value"]; name = group if key=="DEFAULT" else f"{group}.{key}"
        ground = PAPER if group in ("ink",) or (group=="paper" and key in ("text","dim","muted")) or (group=="gold" and key in ("dim","deep")) else INK
        if group=="paper" and key in ("DEFAULT","raised","line"): ground = INK
        r = ratio(hexv, ground); gname = "on paper" if ground==PAPER else "on ink"
        if group=="paper" and key in ("DEFAULT","raised","line"): gname = "ink text on it"
        if group=="ink" and key=="DEFAULT": gname = "on paper"
        cls = "ok" if r>=4.5 else ("warn" if r>=3 else "bad")
        verdict = "text" if r>=4.5 else ("large / graphic" if r>=3 else "decoration only")
        fg = "#070B14" if lum(hexv)>.25 else "#E8ECF5"
        sw.append(f'<div class="sw"><div class="chip" style="background:{hexv};color:{fg}"><span>{name}</span><span class="mono" style="font-weight:400">{hexv}</span></div>'
                  f'<div class="meta"><span>{v["use"]}</span><span>{gname}: <span class="ratio {cls}">{r:.1f}:1</span> {verdict}</span></div></div>')
kinds_css_d, kinds_css_l = [], []
for k, s in C["diagram"].items():
    if k.startswith("$"): continue
    kinds_css_d.append(f"--k-{k}-f:{s['dark']['fill']};--k-{k}-s:{s['dark']['stroke']};")
    kinds_css_l.append(f"--k-{k}-f:{s['light']['fill']};--k-{k}-s:{s['light']['stroke']};")
def shape(k):
    f, s = f"var(--k-{k}-f)", f"var(--k-{k}-s)"
    box = {"part": f'<rect x="10" y="10" width="100" height="44" rx="6" fill="{f}" stroke="{s}" stroke-width="4"/>',
      "port": f'<rect x="10" y="10" width="100" height="44" rx="6" fill="{f}" stroke="{s}" stroke-width="2"/><rect x="102" y="24" width="16" height="16" fill="{f}" stroke="{s}" stroke-width="2"/>',
      "requirement": f'<path d="M16 10 H94 L110 26 V48 a6 6 0 0 1 -6 6 H16 a6 6 0 0 1 -6 -6 V16 a6 6 0 0 1 6 -6 Z" fill="{f}" stroke="{s}" stroke-width="2"/>',
      "state": f'<rect x="10" y="10" width="100" height="44" rx="22" fill="{f}" stroke="{s}" stroke-width="2"/>',
      "lifeline": f'<rect x="25" y="4" width="70" height="30" rx="6" fill="{f}" stroke="{s}" stroke-width="2"/><line x1="60" y1="34" x2="60" y2="70" stroke="{s}" stroke-width="2" stroke-dasharray="5 4"/>',
      "hazard": f'<rect x="8" y="8" width="104" height="48" rx="7" fill="{f}" stroke="{s}" stroke-width="2"/><rect x="13" y="13" width="94" height="38" rx="4" fill="none" stroke="{s}" stroke-width="2"/>'}[k]
    return f'<div class="kind"><svg viewBox="0 0 120 72" role="img" aria-label="{k}: {C["diagram"][k]["cue"]}">{box}</svg><b>{k}</b><span>{C["diagram"][k]["cue"]}</span></div>'
kinds = "".join(shape(k) for k in C["diagram"] if not k.startswith("$"))
html = src.read_text()
dark, light = "".join(kinds_css_d), "".join(kinds_css_l)
html = html.replace("</style>", f'\n:root {{ {dark} }}\n@media (prefers-color-scheme: light) {{ :root:not([data-theme="dark"]) {{ {light} }} }}\n:root[data-theme="light"] {{ {light} }}\n</style>', 1)
rep = {
 "@@SANAD_MARK@@": svgfile("sanad-mark.svg"), "@@EJADAH_MARK@@": svgfile("ejadah-mark.svg"),
 "@@SANAD_LIGHT@@": svgfile("sanad-mark-on-light.svg"), "@@EJADAH_LIGHT@@": svgfile("ejadah-mark-on-light.svg"),
 "@@SANAD_MONO@@": svgfile("sanad-mark-mono.svg"),
 "@@SANAD_SMALL32@@": svgfile("sanad-mark-small.svg", 32), "@@SANAD_SMALL16@@": svgfile("sanad-mark-small.svg", 16),
 "@@SWATCHES@@": "".join(sw), "@@KINDS@@": kinds,
 "@@POST_EXAMPLE@@": tpl("social-post-1200x627.svg", {"ALT_TEXT":"Example social post: Documents decay. Intelligence compounds.","EYEBROW":"ENGINEERING INTELLIGENCE","HEADLINE_LINE_1":"Documents decay.","HEADLINE_LINE_2":"Intelligence compounds.","SUPPORTING_LINE":"Sanad generates, validates and governs the digital thread of a regulated product.","STATUS: build in progress | planned":"build in progress"}),
 "@@GH_EXAMPLE@@": tpl("github-social-1280x640.svg", {"ALT_TEXT":"Example GitHub social preview for Sanad","HEADLINE_LINE_1":"Requirements to tests,","HEADLINE_LINE_2":"traced in VS Code.","REPO_OR_COMMAND, e.g. ejadahailabs/E-REW-support":"ejadahailabs/E-REW-support"}),
}
for k, v in rep.items(): html = html.replace(k, v)
assert "@@" not in html, re.findall(r"@@\w+@@", html)
out.write_text(html); print("built", out, len(html), "bytes")
