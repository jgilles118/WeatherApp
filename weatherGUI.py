#!/usr/bin/python3

import tkinter as tk

window = tk.Tk()

#The widget title
window.title("Weather App")

#The search button
search = tk.Button(window, text="Search", bg='', fg='')
search.pack() 


window.mainloop()
