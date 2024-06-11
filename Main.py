import tkinter as tk
from tkinter import *
import customtkinter as ctk


#setting up app and window/title etc
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Natalie's App")
root.geometry ("600x350")

#displays whats gonna be in app

email=ctk.CTkEntry(root)
email.pack(pady=10)

passw=ctk.CTkEntry(root)
passw.pack(pady=10)
mybutton = ctk.CTkButton(root, text="Log In", corner_radius=40,fg_color="Pink",text_color="Black")
mybutton.pack(pady=10)
    
root.mainloop()
