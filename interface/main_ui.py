import sys
sys.dont_write_bytecode = True
import customtkinter as ctk
from interface.ctk_window_config import window_config
from interface.icons import main_icon_path
from interface.components.title_ui import Title
from interface.components.log_ui import Log
from interface.components.settings_ui import Settings
from interface.components.choose_organization_ui import ChooseOrgarnization
from interface.components.choose_folders_ui import ChooseFolders

class Application(ctk.CTk):
    def __init__(self):
        super().__init__() 
        self.title("Files Organizer")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")
        window_config(self, 450, 550)
        self.iconbitmap(main_icon_path)

        self.grid_rowconfigure(0, weight=1, uniform=True)
        self.grid_rowconfigure(1, weight=1, uniform=True)
        self.grid_rowconfigure(2, weight=2, uniform=True)
        self.grid_rowconfigure(3, weight=2, uniform=True)
        self.grid_rowconfigure(4, weight=8, uniform=True)

        self.grid_columnconfigure(0, weight=1, uniform=True)

        self.title_frame = Title(self)
        self.settings = Settings(self)
        self.choose_folders = ChooseFolders(self)
        self.choose_organization = ChooseOrgarnization(self)
        self.log = Log(self)