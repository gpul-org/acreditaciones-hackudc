#!/usr/bin/python3
import sys

import svgutils.transform as svg


pos = (81.758 - 2.759, 41.758 - 2.759, 0.6897)


t, v = sys.argv[1:]

base = svg.fromfile(f"in/{t}.svg")
qr = svg.fromfile(f"QR/{t}/{v}").getroot()
base.append(qr)
qr.moveto(*pos)

base.save(f"SVG/{t}/{v}", encoding="utf-8")
