import sys
sys.dont_write_bytecode = True
import os
import threading
import customtkinter as ctk
from log.log_logging import report
from interface.icons import organize_image
from CTkMessagebox import CTkMessagebox
from tools.thread_manager import ThereadManager
from functions.files_organizer import files_organizer

class ChooseOrgarnization(ctk.CTkFrame):
    def __init__(self, master:ctk.CTk):
        super().__init__(master=master)
        self.configure(fg_color='transparent')
        self.grid(column=0, row=3, padx=0, pady=0, sticky="nswe")
        self.grid_rowconfigure((0, 1), weight=1, uniform=True)
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform=True)

        self.thread_manager = ThereadManager()

        self.organization_optionemenu = ctk.CTkOptionMenu(self, values=["Year", "Month", "Day"], command=None)
        self.organization_optionemenu.grid(column=0, row=0, padx=(10, 5), pady=(10, 0), sticky="nswe")
        self.organization_optionemenu.set('Month')

        self.checkbox_replace = ctk.CTkCheckBox(master=self, text="Replace files with\nthe same name", command=None, onvalue=True, offvalue=False)
        self.checkbox_replace.grid(column=1, row=0, padx=5, pady=(10, 0), sticky="nswe")

        self.checkbox_delete = ctk.CTkCheckBox(master=self, text="Delete original file", command=None, onvalue=True, offvalue=False)
        self.checkbox_delete.grid(column=2, row=0, padx=(5, 10), pady=(10, 0), sticky="nswe")

        self.button_organize = ctk.CTkButton(self, text='Organize', command=self.func_organize, image=organize_image)
        self.button_organize.grid(column=0, row=1, columnspan=3, padx=10, pady=(10, 0), sticky="nswe")

    def func_organize(self):
        input_path = self.master.choose_folders.entry_input_directory.get()
        output_path = self.master.choose_folders.entry_output_directory.get()
        organize_method = self.organization_optionemenu.get()
        replace = self.checkbox_replace.get()
        delete = self.checkbox_delete.get()

        if input_path == '' and output_path == '':
            CTkMessagebox(title="Warning!", message="Input and Output fileds must be filled!", icon="warning")
            report('Input and Output fileds must be filled!', 'warning')
        elif not os.path.isdir(input_path):
            CTkMessagebox(title="Warning!", message="Input directory is not a valid directory!", icon="warning")
            report('Input directory is not a valid directory!', 'warning')
        elif not os.path.isdir(output_path):
            CTkMessagebox(title="Warning!", message="Output directory is not a valid directory!", icon="warning")
            report('Output directory is not a valid directory!', 'warning')
        elif input_path == output_path:
            CTkMessagebox(title="Warning!", message="Input and Output diretories can`t be the same!", icon="warning")
            report('Input and Output diretories can`t be the same!', 'warning')
        else:
            self.thread_main = threading.Thread(target=files_organizer, args=(input_path, output_path, organize_method, replace, delete))
            self.thread_manager.start(thread=self.thread_main, master=self)