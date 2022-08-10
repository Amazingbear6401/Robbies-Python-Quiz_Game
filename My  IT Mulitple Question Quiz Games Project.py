import tkinter as tk
from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.tix import COLUMN
from webbrowser import BackgroundBrowser



y = 0
tk = Tk()
tk.title("Robbies' IT MCQ ")
a = ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)

root = ttk.Frame(a)

#bg = Tk.PhotoImage(file="C:\Users\Robbie\Downloads\harley.jpg")

#my_label = Label(a, image=bg)
#my_label.place(x=0, y=0,)


def quiz(a):
    a.add(frame1, text="Question 1")
    a.add(frame2, text="Question 2")
    a.add(frame3, text="Question 3")
    a.add(frame4, text="Question 4")

    Label(frame1, text="What does CPU stand for ?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame1, text="Central Proccessing Unit", font=("Arial", 20, "bold"), bg="light blue", command=a_right).grid(row=3, column=2)
    Button(frame1, text="Computer Proccesing Unit", font=("Arial", 20, "bold"), bg="light blue", command=a_wrong).grid(row=3, column=1)
    Button(frame1, text="Computer Processes Unit", font=("Arial", 20, "bold"), bg="light blue", command=a_wrong).grid(row=3, column=3)

    Label(frame2, text="What does GPU stand for?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame2, text="Graphics Proccessing Unit", font=("Arial", 20, "bold"), bg="light blue", command=a2_right).grid(row=3, column=1)
    Button(frame2, text="Graphics Power Unit", font=("Arial", 20, "bold"), bg="light blue", command=a2_wrong).grid(row=3, column=3)
    Button(frame2, text="General Processing Unit", font=("Arial", 20, "bold"), bg="light blue", command=a2_wrong).grid(row=3, column=2)

    Label(frame3, text="What does RAM stand for?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame3, text="Random Access Memory", font=("Arial", 20, "bold"), bg="light blue", command=a3_right).grid(row=3, column=1)
    Button(frame3, text="Ready Access Memory", font=("Arial", 20, "bold"), bg="light blue", command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text="Recovery All Memory", font=("Arial", 20, "bold"), bg="light blue",command=a3_wrong).grid(row=3, column=3)

    Label(frame4, text="What does SSD stand for?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame4, text="Solid State Drive", font=("Arial", 20, "bold"), bg="light blue", command=a4_right).grid(row=3, column=3)
    Button(frame4, text="Solid State Disk", font=("Arial", 20, "bold"), bg="light blue", command=a4_wrong).grid(row=3, column=2)
    Button(frame4, text="Solid Static Disk", font=("Arial", 20, "bold"), bg="light blue", command=a4_wrong).grid(row=3, column=1)

       
def a_right():
    Label(frame1, text=" Correct  ", font=("Arial", 20, "bold"), background="green", ).grid(row=1, column=2)
    
   
def a_wrong():
    Label(frame1, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)
   

 
def a2_right():
    Label(frame2, text=" Correct ", font=("Arial", 20, "bold"), background="green", fg="yellow").grid(row=1, column=2)
   
   
def a2_wrong():
    Label(frame2, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)


def a3_right():
    Label(frame3, text=" Correct ", font=("Arial", 20, "bold"), background="green", fg="yellow").grid(row=1, column=2)

   
def a3_wrong():
    Label(frame3, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)


def a4_right():
    Label(frame4, text=" Correct ", font=("Arial", 20, "bold"), background="green", fg="yellow").grid(row=1, column=2)
 
   
def a4_wrong():
    Label(frame4, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)





quiz(a)
a.pack()
a.mainloop()
