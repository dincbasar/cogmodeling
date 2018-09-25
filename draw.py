from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import run_model

width = 282
height = 282
center = height//2
white = (255, 255, 255)
black = (0,0,0)

root = Tk()
cvframe = Frame(root, width=width, height=height, bg="grey", bd=4)
cvframe.pack(side=TOP)

# Tkinter create a canvas to draw on
cv = Canvas(cvframe, width=width-2, height=height-2, bg="white")
cv.pack(expand=YES, fill=BOTH)

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

filename = "output.png"

def save():
	global filename
	image1.save(filename)


def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 15), (event.y - 15)
    x2, y2 = (event.x + 15), (event.y + 15)
    cv.create_oval(x1, y1, x2, y2, fill="black")
    draw.ellipse([x1, y1, x2, y2],fill="black")

cv.bind("<B1-Motion>", paint)

def clear():
	global image1
	global draw
	cv.delete("all")
	image1 = PIL.Image.new("RGB", (width, height), white)
	draw = ImageDraw.Draw(image1)

btnFrame=Frame(root, height=40)
btnFrame.pack()
var = StringVar()
label = Label(textvariable = var)


response = {}
def runModel():
	global filename
	global response
	response = run_model.predict(filename)

	print(type(response))
	print(response)
	strResponse = response['prediction']+"\n"+response['confidence']+"% Confidence"
	var.set(strResponse)
	label.pack(side=BOTTOM)

def runACTR():
	print("running ACT-R from draw.py")
	global response
	print(response)
	letter = response['prediction']
	print(letter)
	print("loading act-r model")
	import project

	project.init_all(True)
	project.present_trial(letter, display = True)


button=Button(btnFrame, text="save",command=save)
button.pack(side=LEFT)
button1=Button(btnFrame, text="clear",command=clear)
button1.pack(side=LEFT)
button2=Button(btnFrame, text="run model", command=runModel)
button2.pack(side=LEFT)
button3=Button(btnFrame, text="send to ACT-R", command=runACTR)
button3.pack(side=LEFT)
label.pack()
root.mainloop()
