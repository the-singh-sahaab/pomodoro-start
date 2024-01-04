from argparse import MetavarTypeHelpFormatter
from cgitb import text
from ctypes.wintypes import LONG
# from curses import longname
from distutils.command.build import build
from lib2to3.refactor import get_fixers_from_package
from sqlite3 import Row
from tkinter import *
from turtle import bgcolor
import math
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(time_text, text = "00:00")
    lable.config(text = 'timer')
    global reps
    reps = 0    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60
    
    if reps== 0:
        count_timer(long_break_sec)
        lable.config(text="break", fg= RED)
    elif reps %2 == 0:
        lable.config(text = "break", fg = PINK)
        count_timer(short_break_sec)
    else:
        lable.config(text = "work", fg = GREEN)
        count_timer(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_timer(count):
    global time
    count_min = math.floor(count / 60)
    count_sec = int(count%60)
    if count_sec == 0:
        count_sec = 00
    if count_sec > 9:
        canvas.itemconfig(time_text, text = f"{count_min}:{count_sec}")
    else:
        canvas.itemconfig(time_text, text = f"{count_min}:0{count_sec}")
    if count> 0:
        time = window.after(1000, count_timer, count - 1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
lable = Label(window, text = "TIMER", fg=GREEN, bg= YELLOW, font=(FONT_NAME, 30))
lable.grid( row = 0, column = 1)
window.config(padx= 100, pady= 50, bg=YELLOW)
# def some_thing(things):
#     print(things)
# window.after(1000, some_thing, "hello")
canvas = Canvas(height=224, width= 200, bg= YELLOW)
tomato=PhotoImage(file="pomodoro-start\omato.png")
canvas.create_image(102.5,100, image = tomato )
time_text =  canvas.create_text(103,120, text = "00:00", fill= "white", font = (FONT_NAME, 40,"bold"))
# count_timer(10)
canvas.grid(row=1, column=1)
start_button = Button(text = "start", highlightthickness=0,command=start_timer)
end_button = Button(text = "reset", highlightthickness=0, command= reset_timer)
start_button.grid(row = 2, column= 0)
end_button.grid(row=2, column=2)

window.mainloop()
