#!/usr/bin/python3
import sys
import os

import svgutils.transform as svg


pos = (148.000, 156.000, 2.5)


t, v = sys.argv[1:]

base = svg.fromfile(f"in/{t}.svg")
qr = svg.fromfile(f"QR/{t}/{v}").getroot()
base.append(qr)
qr.moveto(*pos)

os.makedirs(f"SVG/{t}", exist_ok=True)
base.save(f"SVG/{t}/{v}", encoding="utf-8")
