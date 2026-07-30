#!/usr/bin/env python3
"""Regenera MAPA.md desde las notas vigentes del grafo."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ("metodo", "equipos", "proyectos", "mundo")
SKIP = {"README.md", "MAPA.md", "AGENTS.md"}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ")


def main() -> None:
    lines = [
        "# MAPA",
        "",
        "*Índice derivado generado por `scripts/generate_map.py`. No se edita a mano.*",
        "",
    ]
    for section in SECTIONS:
        base = ROOT / section
        if not base.exists():
            continue
        lines.extend([f"## {section}/", ""])
        rows: list[str] = []
        if True:
            for path in sorted(base.rglob("*.md")):
                if path.name in SKIP:
                    continue
                meta = frontmatter(path)
                # Lo cerrado no ocupa sitio en el indice: superado y adoptada salen.
                if meta.get("estado") in ("superado", "adoptada"):
                    continue
                rel = path.relative_to(ROOT).as_posix()
                rows.append(f"- [{title(path)}]({rel}) — {meta.get('descripcion', 'Sin descripción')}")
        lines.extend(rows or ["- Sin entradas vigentes."])
        lines.append("")
    (ROOT / "MAPA.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
