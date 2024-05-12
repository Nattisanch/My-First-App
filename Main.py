import tkinter as tk
from tkinter import *
import customtkinter


#setting up app and window/title etc
customtkinter.set_appearance_mode("dark")
root =customtkinter.CTk()
root.title("Natalie's App")
root.geometry ("600x350")

#displays whats gonna be in app
mybutton = customtkinter.CTkButton(root, text="Hey Natalie", corner_radius=40,fg_color="Pink",text_color="Black")
mybutton.pack(pady=100)

root.mainloop()
root.destroy()