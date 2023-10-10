import tkinter
import time

import serial

h = 500
w = 1000

def create_animation_window():
    window = tkinter.Tk()
    window.title("Accident Prevention GUI") 
    window.geometry(f'{w}x{h}')
    return window


def create_animation_canvas(window):
    canvas = tkinter.Canvas (window)
    canvas.pack(fill="both", expand=True)
    return canvas


def animate(window, canvas):
    colour = ['','','','']
    dist = [0, 0, 0, 0]
    c = 0


    rect_width = 166
    rect_height = 300
    rect_thick = 5


    rect_x0 = (w / 2) - (rect_width / 2)
    rect_y0 = (h / 2) - (rect_height / 2)
    rect_x1 = (w / 2) - (rect_width / 2)
    rect_y1 = (h / 2) - (rect_height / 2)

    image = tkinter. PhotoImage(file="/vehicle.png") 
    label = tkinter.Label(animation_window_image=image)
    label.place(x=rect_x0, y=rect_y0)

    X0=rect_x0
    y0=rect_y0
    x1=rect_x0
    y1=y0+30
    #

    oval1 = None
    oval2 = None
    oval3 = None
    oval4 = None
    vehicle = None

    while True:

        if (dist[0] <= 0):
            c = 3

        if (dist[0] >= 348):
            c = -3

    window.update()

    for i in range(4):
        if (dist[1] >= 200):
            colour[i] = 'green'
        elif (dist[i] < 200 and dist[i] >= 100):
            colour[i] = 'yellow'
        elif (dist[i] < 100):
            colour[i] = 'red'
    W=tkinter.Label(animation_window_text=dist[0])
    W.pack()

    #vehicle = canvas.create_rectangle(rect_x0,rect_ye, rect_x1, rect_y1 rect x1, rect y1, width=rect_thick)
    
    oval1 = canvas.create_oval(rect_x0 - 30 - dist[0], rect_y0, rect_x0 - dist[0], rect_y0 + 30, fill=colour[0]) 
    oval2 = canvas.create_oval(rect_x1 + dist[1], rect_ye, rect_x1 + dist[1] + 30, rect_y0 + 30, fill=colour[1]) 
    oval3 = canvas.create_oval(rect_x0 - 30 dist[2], rect_y1 30, rect_x0 - dist[2], rect_y1, fill=colour [2]) 
    oval4 = canvas.create_oval(rect_x1 + dist[3], rect_y1 30, rect_x1 + dist[3] + 30, rect_y1, fill=colour [3])

    for i in range(4):
        dist[i] += c


animation_window= create_animation_window()
icon = tkinter.PhotoImage(file="/vehicle.png")
animation_window.iconphoto(True, icon)
animation_canvas = create_animation_canvas(animation_window)
animate(animation_window, animation_canvas)