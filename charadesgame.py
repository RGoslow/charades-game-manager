#necessary imports

import tkinter as tk
import tkinter.font as font
import webbrowser

#function that creates title screen

def title_screen():
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()
    
    
    #create widgets
    title = tk.Label(master=window, text="CHARADES", fg="#FFC0CB",)
    title["font"] = font.Font(size="36", weight="bold")
    fr_buttons = tk.Frame(master=window, bg="white")
    play_button = tk.Button(master=fr_buttons,text="Play")
    rules_button = tk.Button(master=fr_buttons,text="Rules")
    credits_button = tk.Button(master=fr_buttons,text="Credits")

    #place buttons in button frame
    play_button.grid(row="0", column="0", sticky="ew")
    rules_button.grid(row="1", column="0", sticky="ew")
    credits_button.grid(row="2", column="0", sticky="ew")

    #place all widgets
    title.grid(row="0", column="0")
    fr_buttons.grid(row="1", column="0")

    rules_button.bind("<Button-1>", rules_click)  
    credits_button.bind("<Button-1>", credits_click)
def credits_screen():
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()
    credits_label = tk.Label(text="TESTLABEL")
    home_button = tk.Button(text="BACK TO HOME")
    home_button.bind("<Button-1>", home_click)
    credits_label.pack()
    home_button.pack()
#what happens when buttons are clicked
#clicking rules button opens rules in pastebin
def rules_click(self):
    webbrowser.open("https://pastebin.com/WPXtPBig")
#clicking credits button
def credits_click(self):
    credits_screen()
def home_click(self):
    title_screen()
  

window = tk.Tk()
window.title("Charades Manager")
title_screen()
window.mainloop()