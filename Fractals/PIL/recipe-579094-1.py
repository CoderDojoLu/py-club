#!/usr/bin/env python3
# Quasicrystal Pattern Generator
# https://en.wikipedia.org/wiki/Quasicrystal
# http://mainisusuallyafunction.blogspot.com/2011/10/quasicrystals-as-sums-of-waves-in-plane.html
# FB - 20150808

import math
import random
import sys, time
from PIL import Image

imgx = 512; imgy = 512
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()

outFile = "../output/quasicrystal.png"

# Set mode to normal or animate
mode = "normal"

print("Writing a {}x{} picture: {}".format(imgx, imgy, outFile))

f = random.random() * 40 + 10 # frequency
p = random.random() * math.pi # phase
n = random.randint(10, 20) # of rotations
print(f, p, n)

for ky in range(imgy):
    sys.stdout.write("\r%d%%" % int(ky / (imgy / 100) + 1))
    sys.stdout.flush()
    y = float(ky) / (imgy - 1) * 4 * math.pi - 2 * math.pi
    for kx in range(imgx):
        x = float(kx) / (imgx - 1) * 4 * math.pi - 2 * math.pi
        z = 0.0
        for i in range(n):
            r = math.hypot(x, y)
            a = math.atan2(y, x) + i * math.pi * 2.0 / n
            z += math.cos(r * math.sin(a) * f + p)
        c = int(round(255 * z / n))
        pixels[kx, ky] = (c, c, c) # grayscale
    if mode == "animate":
        outFile = "../output/quasicrystal_" + "{0:03d}.png".format(ky)
        image.save(outFile, "PNG")
image.save(outFile, "PNG")
