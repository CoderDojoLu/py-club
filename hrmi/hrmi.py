#!/usr/bin/env python3
import serial
import shutil

def cleanUp(ser,fh):
	ser.close()
	fh.close()

def main():
	while True:
		fh = open('hr-temp.txt', 'w')
		ser = serial.Serial('/dev/cu.usbserial-A600dSzj', 9600, timeout=1)

		try:
			ser.isOpen()
		except:
			print("Serial port is not open!")
			cleanUp(ser,fh)
			continue

		ser.write("G3\r\n".encode())
		result = ser.readline()
		s = str(result).split()
		avg = (int(s[2]) + int(s[3]) + int(s[4])) / 3
		print("[Debug] Current avg HR: {}".format(int(avg)))
		if avg < 50 or avg > 180:
			continue
			cleanUp(ser,fh)
		else:
			print(int(avg), file = fh)
			shutil.move('hr-temp.txt','hr.txt')

		cleanUp(ser,fh)

if __name__ == "__main__": main()