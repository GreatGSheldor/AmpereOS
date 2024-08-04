#Import Libraries
import customtkinter as ctk

#Code
def setup_powerstrip(root):
    powerstrip_frame = ctk.CTkFrame(root, height=60, fg_color="grey")
    powerstrip_frame.pack(side="bottom", fill="x", padx=15, pady=10)

