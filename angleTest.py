#!/usr/bin/env python
import serial, time

def DataToStr(x,y):
	if isinstance(x, str):
		return x + chr(y)
	else:
		return chr(x) + chr(y)

con = serial.Serial("/dev/ttyAMA0",
					115200,
					parity = serial.PARITY_EVEN,
					stopbits = serial.STOPBITS_ONE,
					timeout = 1,)
print con.portstr

addr = range(12)
try:
	while True:
			inaddr = int(raw_input("input id from 0 to 11:"))
			if not(inaddr in addr):
				print("\nimproper id")
				continue
			val = int(raw_input("\ninput angle from 3500 to 11500:"))
			if not(3500 <= val <= 11500):
				print ("\nimproper data")
				continue
	
			data = reduce(DataToStr, [(0x80 | addr[inaddr]), val >> 7, val &0x7f])
			con.write(data)
			rcv = [ord(i) for i in con.read(6)]
			print rcv
finally:
	con.close()
