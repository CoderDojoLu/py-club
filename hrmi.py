import serial
import binascii as b
import http.server
import socketserver
import os

PORT = 8080

fh = open('hr-temp.txt', 'w')
ser = serial.Serial('/dev/cu.usbserial-A600dSzj', 9600, timeout=1)

try:
    ser.isOpen()
except:
    print("Serial port is not open!")


ser.write("G3\r\n".encode())

result = ser.readline()

s = str(result).split()

avg = (int(s[2]) + int(s[3]) + int(s[4])) / 3

print(int(avg), file = fh)

ser.close()

os.system('mv hr-temp.txt hr.txt')

#Handler = http.server.SimpleHTTPRequestHandler

#httpd = socketserver.TCPServer(("", PORT), Handler)

#print("serving at port", PORT)
#httpd.serve_forever()