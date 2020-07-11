#!/usr/bin/python3

import tkinter as tk

window = tk.Tk()

#The widget title
window.title("Weather App")

#The widget size
winsize = tk.Canvas(window, height=700, width=800)
winsize.pack()

#Frames and  colors
frame1 = tk.Frame(window, bg='#80c1ff', bd=6)
frame1.place(relx=0.5, rely=0.1,relheight=0.1, relwidth=0.75, anchor='n')

frame2 = tk.Frame(window, bg='#80c1fa', bd=6)
frame2.place(rely=0.25,relx=0.5, relheight=0.6,relwidth=0.75, anchor='n') 

#The search button
search = tk.Button(frame1, text="Peek out your window!", font=30)
search.place(relx=0.7, relheight=1, relwidth=0.3) 

#Label
label = tk.Label(frame2)
label.place(relheight=1,relwidth=1)

#Input box
userin = tk.Entry(frame1, font=30)
userin.place(relheight=1, relwidth=0.65)


window.mainloop()
