import sys
sys.dont_write_bytecode = True
import customtkinter as ctk

class Settings(ctk.CTkFrame):
    def __init__(self, master:ctk.CTk):
        super().__init__(master=master)
        self.configure(fg_color='transparent')
        self.grid(column=0, row=1, padx=0, pady=0, sticky="nswe")
        self.grid_rowconfigure(0, weight=1, uniform=True)
        self.grid_columnconfigure((0, 1), weight=1, uniform=True)

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(column=0, row=0, padx=(10, 5), pady=(10, 0), sticky="nswe")
        self.appearance_mode_optionemenu.set('System')

        self.scaling_optionemenu = ctk.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(column=1, row=0, padx=(5, 10), pady=(10, 0), sticky="nswe")
        self.scaling_optionemenu.set('100%')

    def change_appearance_mode_event(self, new_appearance_mode:str):
        ctk.set_appearance_mode(new_appearance_mode.lower())

    def change_scaling_event(self, new_scaling:str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)