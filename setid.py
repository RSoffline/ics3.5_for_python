#!/usr/bin/env python
import serial

def DataToStr(x, y):
	if isinstance(x, str):
		return x + chr(y)
	else:
		return chr(x) + chr(y)

con = serial.Serial("/dev/ttyAMA0",
					115200,
					parity = serial.PARITY_EVEN,
					stopbits = serial.STOPBITS_ONE,
					timeout = 1)

while True:
	while con.read():
		print "please wait"

	con.write(reduce(DataToStr, [0xff, 00, 00, 00]))
	rcv = [ord(i) for i in con.read(6)]
	print rcv
	print "old id:", rcv[-1] & 0x1f

	addr = int(raw_input("new id from 0 to 30:"))
	con.write(reduce(DataToStr, [(0xe0 | addr), 1, 1, 1]))
	rcv = [ord(i) for i in con.read(6)]
	print rcv
	print "\nnew id:", rcv[-1] & 0x1f
	
	YorN = raw_input("continue? y/n:")
	if YorN == "y":
		raw_input("Please enter when you are ready")
	elif YorN == "n":
		break

con.close()
