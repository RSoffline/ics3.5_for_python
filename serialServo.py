#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import serial
import time

def ListToStr(data):
	def add(x, y):
		if isinstance(x, str):
			return x + chr(y)
		else:
			return chr(x) + chr(y)
	
	return reduce(add, data)

def setSerial(port):
	global con
	con = serial.Serial(port,
                        115200,
					    parity = serial.PARITY_EVEN,
						stopbits = serial.STOPBITS_ONE,
						timeout = 1)
					
con = serial.Serial("/dev/ttyAMA0",
                    115200,
					parity = serial.PARITY_EVEN,
					stopbits = serial.STOPBITS_ONE,
					timeout = 1)

class Servo:
	def __init__(self, addr, angle=None):
		self.addr = addr
		self.angle = angle
		self.bef_angle = 0
		if angle != None:
			self.Pos(angle)
		
	def GetId(self):
		return self.addr

	def Pos(self, angle):
		if angle > 270: angle = 270
		if angle < 0:   angle = 0
		self.bef_angle = self.angle
		self.angle = angle
		angle = 3500 + int((8000 * angle) / 270)
		con.write(ListToStr([(0x80 | self.addr), angle >> 7, angle & 0x7f]))
		time.sleep(0.001)
		#rcv = [ord(i) for i in con.read(6)]
		#bef_angle = rcv[-2:]
		#self.bef_angle = 270.0*((rcv[0] << 7 | rcv[1] & 0x7f) - 3500)/8000
		con.flushInput()
		return self.bef_angle

	def Getpos(self):
		return self.angle

	def Speed(self, speed):
		con.flushInput()
		con.write(ListToStr([(0xc0 | self.addr), 0x03, speed]))
		rcv = [ord(i) for i in con.read(6)]
		return rcv[-1]

	def GetSpeed(self):
		con.flushInput()
		con.write(ListToStr([(0xa0 | self.addr), 0x03]))
		rcv = [ord(i) for i in con.read(5)]
		return rcv[-1]

	def Stretch(self, stretch):
		con.flushInput()
		con.write(ListToStr([(0xc0 | self.addr), 0x02, stretch]))
		rcv = [ord(i) for i in con.read(6)]
		return rcv[-1]

	def GetStretch(self):
		con.flushInput()
		con.write(ListToStr([(0xc0 | self.addr), 0x02]))
		rcv = [ord(i) for i in con.read(5)]
