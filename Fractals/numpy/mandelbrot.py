import sys
from numpy import NaN
try:
  from pylab import *
except ImportError:
  sys.exit("Please install matplotlib: pip3 install matplotlib")

def m(a):
  z = 0
  for n in range(1, 100):
    z = z**2 + a
    if abs(z) > 2:
      return n
  return NaN

X = arange(-2, .5, .002)
Y = arange(-1,  1, .002)
Z = zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
  sys.stdout.write("\r%d%%" % int(iy / len(Y)/100)+1)
  sys.stdout.flush()
  for ix, x in enumerate(X):
    Z[iy,ix] = m(x + 1j * y)

imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
xlabel("Re(c)")
ylabel("Im(c)")
savefig("mandelbrot_python.svg")
show()