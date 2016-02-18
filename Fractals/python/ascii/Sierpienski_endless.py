from time import sleep

x = 1
while True:
  print(bin(x)[2:].replace('0', ' '))
  x ^= x<<1
  sleep(0.3)