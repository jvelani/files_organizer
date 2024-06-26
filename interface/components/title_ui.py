import sys
sys.dont_write_bytecode = True
import customtkinter as ctk
from interface.icons import main_icon_image

class Title(ctk.CTkFrame):
    def __init__(self, master:ctk.CTk):
        super().__init__(master=master)
        self.configure(fg_color='transparent')
        self.grid(column=0, row=0, padx=0, pady=0)
        self.grid_rowconfigure(0, weight=1, uniform=True)
        self.grid_columnconfigure((0, 1), weight=1, uniform=True)

        self.title_image = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=25, weight="bold"), image=main_icon_image)
        self.title_image.grid(column=0, row=0, padx=(10, 5), pady=(10, 0), sticky="nse")

        self.title_label = ctk.CTkLabel(self, text="Files Organizer", font=ctk.CTkFont(size=25, weight="bold"))
        self.title_label.grid(column=1, row=0, columnspan=2, padx=(10, 5), pady=(10, 0), sticky="nsw")