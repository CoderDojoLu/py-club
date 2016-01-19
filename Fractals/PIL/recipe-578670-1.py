#!/usr/bin/env python3
# Hofstadter Butterfly Fractal
# http://en.wikipedia.org/wiki/Hofstadter%27s_butterfly
# Wolfgang Kinzel/Georg Reents,"Physics by Computer" Springer Press (1998)
# FB36 - 20130922
import math
import sys, time
from PIL import Image
imgSize = 800
image = Image.new("RGB", (imgSize, imgSize))
pixels = image.load()

outFile = "../output/HofstadterButterflyFractal.png"

print("Writing a {}x{} picture: {}".format(imgSize, imgSize, outFile))

def gcd(a, b): # Greatest Common Divisor
    if b == 0: return a
    return gcd(b, a % b)

pi2 = math.pi * 2.0
MAXX = imgSize + 1
MAXY = imgSize + 1
qmax = imgSize
for q in range(4, qmax, 2):
    sys.stdout.write("\r%d%%" % int(100 * q / qmax))
    sys.stdout.flush()
    for p in range(1, q, 2):
        if gcd(p, q) <= 1:
            sigma = pi2 * p / q
            nold = 0
            ie = 0
            for ie in range(0, MAXY + 2):
                e = 8.0 * ie / MAXY - 4.0 - 4.0 / MAXY
                n = 0
                polyold = 1.0
                poly = 2.0 * math.cos(sigma) - e
                if polyold * poly < 0.0: n += 1

                for m in range(2, int(q / 2)):
                    polynew = (2.0 * math.cos(sigma * m) - e) * poly - polyold
                    if poly * polynew < 0.0: n += 1
                    polyold = poly
                    poly = polynew

                polyold = 1.0
                poly = 2.0 - e
                if polyold * poly < 0.0: n += 1
                polynew = (2.0 * math.cos(sigma) - e) * poly - 2.0 * polyold
                if poly * polynew < 0.0: n += 1
                polyold = poly
                poly = polynew

                for m in range(2, int(q / 2)):
                    polynew = (2.0 * math.cos(sigma * m) - e) * poly - polyold
                    if poly * polynew < 0.0: n += 1
                    polyold = poly
                    poly = polynew

                polynew = (2.0 * math.cos(sigma * q / 2.0) - e) * poly - 2.0 * polyold
                if poly * polynew < 0.0: n += 1

                polyold = 1.0
                poly = 2.0 - e
                if polyold * poly < 0.0: n += 1
                polynew = (2.0 * math.cos(sigma) - e) * poly - 2.0 * polyold
                if poly * polynew < 0.0: n += 1
                polyold = poly
                poly = polynew

                for m in range(2, int(q / 2)):
                    polynew = (2.0 * math.cos(sigma * m) - e) * poly - polyold
                    if poly * polynew < 0.0: n += 1
                    polyold = poly
                    poly = polynew

                polynew = (2.0 * math.cos(sigma * q / 2.0) - e) * poly - 2.0 * polyold
                if poly * polynew < 0.0: n += 1
                if n > nold:
                    pixels[int(MAXY - ie), int(MAXX * p / q)] = (255, 255, 255)
                    pixels[int(MAXX * p / q), int(MAXY - ie)] = (255, 255, 255)
                nold = n

image.save(outFile, "PNG")
