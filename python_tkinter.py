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