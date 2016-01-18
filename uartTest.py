#!/usr/bin/env python
import serial, time

def DataToStr(x,y):
	if isinstance(x, str):
		return x + chr(y)
	else:
		return chr(x) + chr(y)

con = serial.Serial("/dev/ttyAMA0", 115200, parity = serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout = 1)
#con = serial.Serial("/dev/ttyAMA0", 115200, timeout = 1)
print con.portstr

while True:
	data = reduce(DataToStr,[0xff,00,00,00])
	con.write(data)
	#time.sleep(0.01)
	rcv = [ord(i) for i in con.read(6)]
	print rcv
	#time.sleep(1)
