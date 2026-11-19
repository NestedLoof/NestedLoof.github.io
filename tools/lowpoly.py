"""Generate the low-poly wireframe SVG used behind the Games band.

    python tools/lowpoly.py            # writes assets/img/brand/lowpoly.svg

Seeded, so it is reproducible. Change the seed for a different mesh.
"""
import os, random, sys
from _paths import IMG
random.seed(7)
W, H, C, R = 1200, 720, 12, 7
sx, sy = W / C, H / R
pts = {}
for j in range(R + 1):
    for i in range(C + 1):
        x, y = i * sx, j * sy
        if 0 < i < C: x += random.uniform(-.32, .32) * sx
        if 0 < j < R: y += random.uniform(-.32, .32) * sy
        pts[i, j] = (round(x, 1), round(y, 1))
edges = set()
def e(a, b): edges.add(tuple(sorted((a, b))))
for j in range(R):
    for i in range(C):
        a, b, c, d = (i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)
        e(a, b); e(b, c); e(c, d); e(d, a)
        if random.random() < .5: e(a, c)
        else: e(b, d)
path = " ".join(f"M{pts[a][0]} {pts[a][1]}L{pts[b][0]} {pts[b][1]}" for a, b in sorted(edges))
dots = "".join(f'<rect x="{x-1.5}" y="{y-1.5}" width="3" height="3"/>' for (i, j), (x, y) in pts.items() if 0 < i < C and 0 < j < R)
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
       f'<path d="{path}" fill="none" stroke="#CDB98F" stroke-width="1" vector-effect="non-scaling-stroke"/>'
       f'<g fill="#CDB98F">{dots}</g></svg>')
open(os.path.join(IMG, 'brand', 'lowpoly.svg'), 'w').write(svg)
print(len(svg))
