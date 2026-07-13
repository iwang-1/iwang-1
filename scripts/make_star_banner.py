#!/usr/bin/env python3
"""Render the profile banner star field from the star-catalog-web HYG snapshot.

Plots every star in the snapshot on an equirectangular RA/Dec chart (RA
increasing to the left, as on the sky), with magnitude-scaled radii and
B-V-color-index-tinted fills. Writes a dark and a light SVG variant for the
README's <picture> element.

Usage:
    python scripts/make_star_banner.py path/to/stars.json

The snapshot is the same public/data/stars.json file that
https://github.com/iwang-1/star-catalog-web serves to the sky map.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WIDTH = 1200
HEIGHT = 400
PAD = 8  # keep edge stars' circles inside the viewBox

# B-V color index -> approximate star tint, binned. The dark palette follows
# the conventional blue-white .. orange-red rendering of stellar colors; the
# light palette uses darker versions of the same hues so the field stays
# legible on a white page.
BINS = [
    # (upper B-V bound, dark-mode fill, light-mode fill)
    (0.00, "#9db4ff", "#3d5aa8"),  # O/B: blue
    (0.30, "#c6d4ff", "#4f6bb0"),  # A: blue-white
    (0.58, "#f4f2ff", "#6c7a94"),  # F: white
    (0.81, "#fff2d5", "#8a7440"),  # G: yellow-white
    (1.40, "#ffd9a1", "#a06a2c"),  # K: orange
    (99.0, "#ffb079", "#a04f24"),  # M: orange-red
]


def bin_index(ci: float | None) -> int:
    if ci is None:
        return 2  # unknown color index: render as white
    for i, (bound, _, _) in enumerate(BINS):
        if ci < bound:
            return i
    return len(BINS) - 1


def radius(mag: float) -> float:
    # Sirius (-1.44) ~ 3.1px; the mag ~6.5 naked-eye limit ~ 0.55px.
    return round(max(0.55, 0.55 + (6.5 - mag) * 0.32), 2)


def render(stars: list[dict], dark: bool) -> str:
    bg = "#0d1117" if dark else "#ffffff"
    groups: list[list[str]] = [[] for _ in BINS]
    for s in stars:
        x = round(PAD + (360.0 - s["ra"]) / 360.0 * (WIDTH - 2 * PAD), 1)
        y = round(PAD + (90.0 - s["dec"]) / 180.0 * (HEIGHT - 2 * PAD), 1)
        groups[bin_index(s.get("ci"))].append(
            f'<circle cx="{x}" cy="{y}" r="{radius(s["mag"])}"/>'
        )
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'role="img" aria-label="Star field rendered from the HYG snapshot">',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{bg}"/>',
    ]
    for (_, dark_fill, light_fill), circles in zip(BINS, groups):
        fill = dark_fill if dark else light_fill
        parts.append(f'<g fill="{fill}">{"".join(circles)}</g>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    stars = json.loads(Path(sys.argv[1]).read_text())
    out_dir = Path(__file__).resolve().parent.parent / "assets"
    out_dir.mkdir(exist_ok=True)
    for dark in (True, False):
        name = f"star-banner-{'dark' if dark else 'light'}.svg"
        (out_dir / name).write_text(render(stars, dark))
        print(f"wrote assets/{name} ({len(stars)} stars)")


if __name__ == "__main__":
    main()
