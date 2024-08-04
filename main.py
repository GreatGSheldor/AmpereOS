#Import Libraries
import customtkinter as ctk
#Import Local
from Components.PowerStrip import setup_powerstrip
from Components.Workbench import setup_workbench

#Code
root = ctk.CTk()
root.after(0, lambda:root.state('zoomed'))\

setup_powerstrip(root)
setup_workbench(root)

#Mainloop
root.mainloop()