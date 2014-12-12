import pyb
lcd = pyb.LCD('X')
lcd.light(True)
for x in range(-80, 128):
    lcd.fill(0)
    lcd.text('Welcome to CodeClub@ISLux', x, 10, 1)
    lcd.show()
    pyb.delay(50)

# A pressed == 8
# B pressed == 12
# X pressed == 2
# Y pressed == 1

while True:
    i2c = pyb.I2C(1, pyb.I2C.MASTER)
    i2c.mem_write(4, 90, 0x5e)
    touch = i2c.mem_read(1, 90, 0)[0]
    lcd.fill(0)
    lcd.text(str(touch), 0, 10, 1)
    lcd.show()
    pyb.delay(50)
    i2c.deinit()
