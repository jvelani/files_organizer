import sys
sys.dont_write_bytecode = True
import customtkinter as ctk

def window_config(master:ctk.CTk, width:int, height:int):
    master.update_idletasks()
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    x = int(((screen_width/2) - (width/2)))
    y = int(((screen_height/2) - (height/1.5)))

    master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    master.deiconify()