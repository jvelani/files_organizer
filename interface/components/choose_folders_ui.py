import sys
sys.dont_write_bytecode = True
import customtkinter as ctk
from customtkinter import filedialog

class ChooseFolders(ctk.CTkFrame):
    def __init__(self, master:ctk.CTk):
        super().__init__(master=master)
        self.configure(fg_color='transparent')
        self.grid(column=0, row=2, padx=0, pady=0, sticky="nswe")
        self.grid_rowconfigure((0, 1), weight=1, uniform=True)
        self.grid_columnconfigure(0, weight=2, uniform=True)
        self.grid_columnconfigure(1, weight=5, uniform=True)
        self.grid_columnconfigure(2, weight=1, uniform=True)

        self.label_input_directory = ctk.CTkLabel(self, text="Input Directory")
        self.label_input_directory.grid(column=0, row=0, padx=(10, 5), pady=(10, 0), sticky="nswe")

        self.entry_input_directory_string_var = ctk.StringVar()
        self.entry_input_directory = ctk.CTkEntry(self, textvariable=self.entry_input_directory_string_var)
        self.entry_input_directory.grid(column=1, row=0, padx=(5, 5), pady=(10, 0), sticky="nswe")

        self.button_input_directory = ctk.CTkButton(self, text='...', command=self.choose_input_directory, fg_color='transparent', border_width=1)
        self.button_input_directory.grid(column=2, row=0, padx=(5, 10), pady=(10, 0), sticky="nswe")

        self.label_output_directory = ctk.CTkLabel(self, text="Output Directory")
        self.label_output_directory.grid(column=0, row=1, padx=(10, 5), pady=(10, 0), sticky="nswe")

        self.entry_output_directory_string_var = ctk.StringVar()
        self.entry_output_directory = ctk.CTkEntry(self, textvariable=self.entry_output_directory_string_var)
        self.entry_output_directory.grid(column=1, row=1, padx=(5, 5), pady=(10, 0), sticky="nswe")

        self.button_output_directory = ctk.CTkButton(self, text='...', command=self.choose_output_directory, fg_color='transparent', border_width=1)
        self.button_output_directory.grid(column=2, row=1, padx=(5, 10), pady=(10, 0), sticky="nswe")

    def choose_input_directory(self):
        directory = filedialog.askdirectory()
        self.entry_input_directory_string_var.set(directory)

    def choose_output_directory(self):
        directory = filedialog.askdirectory()
        self.entry_output_directory_string_var.set(directory)