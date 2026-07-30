#!/usr/bin/env python3
"""Audita invariantes ligeros del grafo Mycelia.

Por defecto informa de la deuda heredada sin bloquear. Usa `--strict` cuando el
grafo haya sido saneado y se quiera convertir cada hallazgo en fallo de CI.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIRS = ("metodo", "equipos", "proyectos", "mundo")
REQUIRED = {"descripcion", "capa", "tipo", "estado", "autor", "creado"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, "sin frontmatter"
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, "frontmatter sin cierre"
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, None


def audit() -> tuple[int, list[str]]:
    findings: list[str] = []
    checked = 0
    for dirname in GRAPH_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if path.name == "README.md":
                continue
            checked += 1
            rel = path.relative_to(ROOT)
            meta, error = parse_frontmatter(path)
            if error:
                findings.append(f"{rel}: {error}")
                continue
            missing = REQUIRED - meta.keys()
            if missing:
                findings.append(f"{rel}: faltan campos {', '.join(sorted(missing))}")
            if meta.get("creado") and not DATE_RE.match(meta["creado"]):
                findings.append(f"{rel}: creado debe usar AAAA-MM-DD")
            if meta.get("fuente", "").startswith("http") and not meta.get("fecha_acceso"):
                findings.append(f"{rel}: fuente externa sin fecha_acceso")
            if meta.get("estado") == "superado" and not meta.get("supersedido_por"):
                findings.append(f"{rel}: estado superado sin supersedido_por")
            if meta.get("estado") == "adoptada" and not meta.get("adoptada_en"):
                findings.append(f"{rel}: estado adoptada sin adoptada_en")
    return checked, findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    checked, findings = audit()
    if findings:
        print("Hallazgos de calidad del grafo:")
        print("\n".join(findings))
        print(f"\n{len(findings)} hallazgos en {checked} notas.")
        return 1 if args.strict else 0
    print(f"Grafo válido: {checked} notas comprobadas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
