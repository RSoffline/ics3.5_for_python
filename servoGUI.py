import serialServo
import sys
import Tkinter as tk

serialServo.setSerial()

def scaleFunc(event):
	value = scale1.get()
	deg = round(270.0 * (value - 3500.0) / 8000.0, 4)
	label.configure(text="deg:"+str(deg))
	servo(deg)

servo = serialServo.Servo(0)

root = tk.Tk()
label = tk.Label(root, text = "deg:0")
label.pack()
scale1 = tk.Scale(root,
				  label = "servo position",
				  orient = "h",
				  from_ = 3500, to = 11500,
				  command = scaleFunc)
scale1.pack()
root.mainloop()
