#!/usr/bin/env python3
"""Genera panel.html: una vista autocontenida del conocimiento de una instancia Mycelia.

Un fichero HTML sin dependencias ni red: mapa del grafo, salud, y lo que pide atencion.
Derivado y regenerable, como MAPA.md. Uso: python scripts/panel.py [ruta-instancia]
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

CAPAS = ("mundo", "equipos", "proyectos", "direccion", "metodo")
LINK_RE = re.compile(r"\[\[([^\]|#]+)")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def title_of(text: str, stem: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return stem.replace("-", " ")


def collect(root: Path) -> list[dict]:
    notes: list[dict] = []
    for capa in CAPAS:
        base = root / capa
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name == "README.md":
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            meta = frontmatter(text)
            rel = path.relative_to(root).as_posix()
            body = text.split("\n---\n", 1)[-1]
            notes.append(
                {
                    "id": path.stem,
                    "ruta": rel,
                    "titulo": title_of(text, path.stem),
                    "capa": meta.get("capa", capa),
                    "grupo": rel.split("/")[1] if rel.count("/") > 1 else capa,
                    "tipo": meta.get("tipo", "?"),
                    "estado": meta.get("estado", "?"),
                    "autor": meta.get("autor", "?"),
                    "creado": meta.get("creado", ""),
                    "descripcion": meta.get("descripcion", ""),
                    "fuente": meta.get("fuente", ""),
                    "cuarentena": meta.get("cuarentena", "").lower() == "true",
                    "temas": [t.strip() for t in meta.get("temas", "").strip("[]").split(",") if t.strip()],
                    "enlaces": sorted({m for m in LINK_RE.findall(body)}),
                    "palabras": len(body.split()),
                }
            )
    return notes


def html(notes: list[dict], root: Path) -> str:
    ids = {n["id"] for n in notes}
    inbound: Counter[str] = Counter()
    for n in notes:
        for link in n["enlaces"]:
            target = link.split("/")[-1]
            if target in ids:
                inbound[target] += 1
    for n in notes:
        n["entrantes"] = inbound.get(n["id"], 0)
        n["roto"] = [l for l in n["enlaces"] if l.split("/")[-1] not in ids]

    atencion = {
        "cuarentena pendiente": [n for n in notes if n["cuarentena"]],
        "sin enlaces entrantes": [n for n in notes if n["entrantes"] == 0 and n["capa"] != "metodo"],
        "enlaces rotos": [n for n in notes if n["roto"]],
        "superadas": [n for n in notes if n["estado"] == "superado"],
        "notas ladrillo (>900 palabras)": [n for n in notes if n["palabras"] > 900],
    }
    stats = {
        "capa": Counter(n["capa"] for n in notes),
        "tipo": Counter(n["tipo"] for n in notes),
        "autor": Counter(n["autor"] for n in notes),
        "grupo": Counter(n["grupo"] for n in notes),
    }
    data = {
        "notas": notes,
        "atencion": {k: [n["id"] for n in v] for k, v in atencion.items()},
        "stats": {k: dict(v.most_common()) for k, v in stats.items()},
        "instancia": root.name,
        "total": len(notes),
    }
    return TEMPLATE.replace("__DATOS__", json.dumps(data, ensure_ascii=False))


TEMPLATE = r"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Panel Mycelia</title>
<style>
:root{--bg:#0f1210;--panel:#171b18;--line:#2a312c;--tx:#e8ece9;--dim:#93a09a;--ac:#7fc4a0;--warn:#e0b25e}
@media(prefers-color-scheme:light){:root{--bg:#f7f8f7;--panel:#fff;--line:#dfe4e0;--tx:#1a201c;--dim:#5f6b65;--ac:#2f7d5c;--warn:#a06d12}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.55 ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif}
header{padding:20px 24px;border-bottom:1px solid var(--line)}
h1{margin:0;font-size:19px;letter-spacing:.2px}h1 span{color:var(--dim);font-weight:400}
main{padding:20px 24px;max-width:1400px;margin:0 auto;display:grid;gap:20px}
.row{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px}
.card h2{margin:0 0 12px;font-size:12px;text-transform:uppercase;letter-spacing:.09em;color:var(--dim);font-weight:600}
.big{font-size:30px;font-weight:600;line-height:1}
.bar{display:flex;align-items:center;gap:8px;margin:5px 0;font-size:13px}
.bar b{min-width:112px;color:var(--dim);font-weight:400}
.bar i{height:7px;background:var(--ac);border-radius:4px;display:block;opacity:.75}
.bar u{text-decoration:none;color:var(--dim);font-variant-numeric:tabular-nums}
table{width:100%;border-collapse:collapse;font-size:13.5px}
th{text-align:left;color:var(--dim);font-weight:500;padding:6px 8px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--panel);cursor:pointer}
td{padding:7px 8px;border-bottom:1px solid var(--line);vertical-align:top}
tr:hover td{background:rgba(127,196,160,.06)}
.tag{display:inline-block;padding:1px 7px;border-radius:20px;font-size:11px;border:1px solid var(--line);color:var(--dim)}
.t-hecho{color:var(--ac);border-color:var(--ac)}.t-hipotesis,.t-pregunta{color:var(--warn);border-color:var(--warn)}
.warn{color:var(--warn)}
.wrap{max-height:440px;overflow:auto}
input,select{background:var(--bg);color:var(--tx);border:1px solid var(--line);border-radius:7px;padding:7px 10px;font:inherit;font-size:13px}
.tools{display:flex;gap:9px;flex-wrap:wrap;margin-bottom:12px}
canvas{width:100%;height:420px;display:block;cursor:grab}
.desc{color:var(--dim);font-size:12.5px}
a{color:var(--ac)}
footer{padding:14px 24px;color:var(--dim);font-size:12px;border-top:1px solid var(--line)}
</style></head><body>
<header><h1>Panel Mycelia · <span id="inst"></span></h1></header>
<main>
  <div class="row" id="kpis"></div>
  <div class="row">
    <div class="card"><h2>Por capa</h2><div id="c-capa"></div></div>
    <div class="card"><h2>Por tipo epistémico</h2><div id="c-tipo"></div></div>
    <div class="card"><h2>Por autoría</h2><div id="c-autor"></div></div>
    <div class="card"><h2>Pide atención</h2><div id="c-aten"></div></div>
  </div>
  <div class="card"><h2>Mapa de enlaces</h2><canvas id="g"></canvas>
    <div class="desc">Cada punto es una nota; el tamaño, sus enlaces entrantes. Arrastra para mover. Pasa el ratón para ver el título.</div></div>
  <div class="card"><h2>Notas</h2>
    <div class="tools">
      <input id="q" placeholder="buscar en título y descripción…" style="flex:1;min-width:200px">
      <select id="f-capa"><option value="">toda capa</option></select>
      <select id="f-tipo"><option value="">todo tipo</option></select>
      <select id="f-grupo"><option value="">todo grupo</option></select>
    </div>
    <div class="wrap"><table><thead><tr>
      <th data-k="titulo">Nota</th><th data-k="capa">Capa</th><th data-k="grupo">Grupo</th>
      <th data-k="tipo">Tipo</th><th data-k="autor">Autoría</th><th data-k="creado">Creado</th><th data-k="entrantes">In</th>
    </tr></thead><tbody id="tb"></tbody></table></div>
  </div>
</main>
<footer>Índice derivado y regenerable (<code>scripts/panel.py</code>). La fuente son las notas y su historial git.</footer>
<script>
const D=__DATOS__;
document.getElementById('inst').textContent=D.instancia+' · '+D.total+' notas';
const el=s=>document.querySelector(s);
const kpi=(v,l)=>`<div class="card"><h2>${l}</h2><div class="big">${v}</div></div>`;
const nAten=Object.values(D.atencion).reduce((a,b)=>a+b.length,0);
const hechos=D.stats.tipo.hecho||0, hip=(D.stats.tipo.hipotesis||0)+(D.stats.tipo.pregunta||0);
el('#kpis').innerHTML=kpi(D.total,'Notas vigentes')+kpi(Object.keys(D.stats.grupo).length,'Grupos de conocimiento')
  +kpi(hechos,'Hechos con fuente')+kpi(hip,'Hipótesis y preguntas abiertas')+kpi(nAten,'Avisos de la bibliotecaria');
function bars(id,obj){const m=Math.max(...Object.values(obj),1);
  el(id).innerHTML=Object.entries(obj).map(([k,v])=>
    `<div class="bar"><b>${k}</b><i style="width:${Math.round(v/m*100)}%"></i><u>${v}</u></div>`).join('');}
bars('#c-capa',D.stats.capa);bars('#c-tipo',D.stats.tipo);bars('#c-autor',D.stats.autor);
el('#c-aten').innerHTML=Object.entries(D.atencion).map(([k,v])=>
  `<div class="bar"><b style="min-width:170px">${k}</b><u class="${v.length?'warn':''}">${v.length}</u></div>`).join('')
  +'<div class="desc" style="margin-top:8px">Cero avisos no es el objetivo; el objetivo es que ninguno sorprenda.</div>';
// tabla
const S={k:'creado',dir:-1};
function render(){const q=el('#q').value.toLowerCase(),fc=el('#f-capa').value,ft=el('#f-tipo').value,fg=el('#f-grupo').value;
  const rows=D.notas.filter(n=>(!q||(n.titulo+' '+n.descripcion).toLowerCase().includes(q))
    &&(!fc||n.capa===fc)&&(!ft||n.tipo===ft)&&(!fg||n.grupo===fg))
    .sort((a,b)=>((a[S.k]>b[S.k])-(a[S.k]<b[S.k]))*S.dir);
  el('#tb').innerHTML=rows.map(n=>`<tr><td><b>${n.titulo}</b>${n.cuarentena?' <span class="tag warn">cuarentena</span>':''}
    <div class="desc">${n.descripcion}</div><div class="desc"><code>${n.ruta}</code></div></td>
    <td><span class="tag">${n.capa}</span></td><td>${n.grupo}</td>
    <td><span class="tag t-${n.tipo}">${n.tipo}</span></td><td>${n.autor}</td><td>${n.creado}</td><td>${n.entrantes}</td></tr>`).join('')
    ||'<tr><td colspan="7" class="desc">Sin resultados.</td></tr>';}
for(const [sel,key] of [['#f-capa','capa'],['#f-tipo','tipo'],['#f-grupo','grupo']])
  el(sel).innerHTML+=Object.keys(D.stats[key]).map(v=>`<option>${v}</option>`).join('');
['#q','#f-capa','#f-tipo','#f-grupo'].forEach(s=>el(s).addEventListener('input',render));
document.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{const k=th.dataset.k;S.dir=S.k===k?-S.dir:1;S.k=k;render();});
render();
// grafo
const cv=el('#g'),cx=cv.getContext('2d');const ids=new Set(D.notas.map(n=>n.id));
const N=D.notas.map(n=>({...n,x:Math.random(),y:Math.random(),vx:0,vy:0}));
const idx=new Map(N.map((n,i)=>[n.id,i]));
const E=[];for(const n of N)for(const l of n.enlaces){const t=idx.get(l.split('/').pop());if(t!==undefined&&t!==idx.get(n.id))E.push([idx.get(n.id),t]);}
const COL={mundo:'#7fc4a0',proyectos:'#8ab4f8',metodo:'#e0b25e',equipos:'#c58af9',direccion:'#f28b82'};
function size(){const r=cv.getBoundingClientRect();cv.width=r.width*devicePixelRatio;cv.height=r.height*devicePixelRatio;
  cx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);}
let W=0,H=0,hov=null;
function step(){W=cv.width/devicePixelRatio;H=cv.height/devicePixelRatio;
  for(let i=0;i<N.length;i++){let fx=0,fy=0;const a=N[i];
    for(let j=0;j<N.length;j++){if(i===j)continue;const b=N[j];let dx=a.x-b.x,dy=a.y-b.y;let d=Math.hypot(dx,dy)||.001;
      if(d<.35){const f=.00018/(d*d);fx+=dx/d*f;fy+=dy/d*f;}}
    fx+=(.5-a.x)*.006;fy+=(.5-a.y)*.006;a.vx=(a.vx+fx)*.86;a.vy=(a.vy+fy)*.86;}
  for(const [s,t] of E){const a=N[s],b=N[t];const dx=b.x-a.x,dy=b.y-a.y;
    a.vx+=dx*.004;a.vy+=dy*.004;b.vx-=dx*.004;b.vy-=dy*.004;}
  for(const n of N){if(n===drag)continue;n.x=Math.min(.98,Math.max(.02,n.x+n.vx));n.y=Math.min(.98,Math.max(.02,n.y+n.vy));}
  cx.clearRect(0,0,W,H);cx.lineWidth=1;cx.strokeStyle='rgba(147,160,154,.28)';
  for(const [s,t] of E){cx.beginPath();cx.moveTo(N[s].x*W,N[s].y*H);cx.lineTo(N[t].x*W,N[t].y*H);cx.stroke();}
  for(const n of N){const r=4+Math.min(7,n.entrantes*1.6);cx.beginPath();cx.arc(n.x*W,n.y*H,r,0,7);
    cx.fillStyle=COL[n.capa]||'#93a09a';cx.globalAlpha=n.estado==='superado'?.3:.9;cx.fill();cx.globalAlpha=1;}
  if(hov){cx.fillStyle=getComputedStyle(document.body).color;cx.font='12px ui-sans-serif,system-ui';
    const t=hov.titulo;const w=cx.measureText(t).width;let x=Math.min(hov.x*W+10,W-w-8);
    cx.fillStyle='rgba(0,0,0,.6)';cx.fillRect(x-4,hov.y*H-20,w+8,17);cx.fillStyle='#fff';cx.fillText(t,x,hov.y*H-8);}
  requestAnimationFrame(step);}
let drag=null;
function at(e){const r=cv.getBoundingClientRect();const mx=(e.clientX-r.left)/r.width,my=(e.clientY-r.top)/r.height;
  let best=null,bd=1;for(const n of N){const d=Math.hypot(n.x-mx,n.y-my);if(d<bd){bd=d;best=n;}}
  return bd<.03?[best,mx,my]:[null,mx,my];}
cv.onmousedown=e=>{const [n]=at(e);drag=n;};
cv.onmousemove=e=>{const [n,mx,my]=at(e);hov=drag||n;if(drag){drag.x=mx;drag.y=my;}cv.style.cursor=n?'pointer':'grab';};
cv.onmouseup=cv.onmouseleave=()=>{drag=null;};
addEventListener('resize',size);size();step();
</script></body></html>"""


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    notes = collect(root)
    if not notes:
        print(f"No hay notas bajo {root}. Ejecuta desde una instancia Mycelia.")
        raise SystemExit(1)
    out = root / "panel.html"
    out.write_text(html(notes, root), encoding="utf-8")
    print(f"panel.html generado: {len(notes)} notas de {root.name}")


if __name__ == "__main__":
    main()
