import sys
sys.dont_write_bytecode = True
import darkdetect
import customtkinter as ctk
from log.log_logging import LOG_PATH
from tools.text_utils import TxtUtils
from interface.icons import clear_image

class Log(ctk.CTkFrame):
    def __init__(self, master:ctk.CTk):
        super().__init__(master=master)
        self.configure(fg_color='transparent')
        self.grid(column=0, row=4, padx=0, pady=0, sticky="nswe")
        self.grid_rowconfigure(0, weight=5, uniform=True)
        self.grid_rowconfigure(1, weight=1, uniform=True)
        self.grid_columnconfigure(0, weight=1, uniform=True)

        self.txt_utils = TxtUtils()

        self.log_textbox = ctk.CTkTextbox(self, wrap='none')
        self.log_textbox.grid(column=0, row=0, padx=10, pady=(10, 0), sticky="nswe")
        self.log_textbox.configure(state='disabled')

        self.button_clear = ctk.CTkButton(self, text='Clear', command=self.clear_log, image=clear_image)
        self.button_clear.grid(column=0, row=1, padx=10, pady=10, sticky="nswe")

        self.log_func()
        self.log_tag_config_function()

    def detect_application_theme(self):
        theme_selected = self.master.settings.appearance_mode_optionemenu.get()
        if theme_selected == 'Dark':
            return 'Dark'
        elif theme_selected == 'Light':
            return 'Light'
        elif theme_selected == 'System':
            return darkdetect.theme()

    def log_tag_config_function(self):
        theme = self.detect_application_theme()
        if theme == 'Dark':
            self.log_textbox.tag_config(tagName="error", foreground='yellow')
            self.log_textbox.tag_config(tagName="info", foreground='green2')
            self.log_textbox.tag_config(tagName="debug", foreground='white')
            self.log_textbox.tag_config(tagName="critical", foreground='red')
            self.log_textbox.tag_config(tagName="warning", foreground='orange')
        else:
            self.log_textbox.tag_config(tagName="error", foreground='yellow3')
            self.log_textbox.tag_config(tagName="info", foreground='green3')
            self.log_textbox.tag_config(tagName="debug", foreground='black')
            self.log_textbox.tag_config(tagName="critical", foreground='red')
            self.log_textbox.tag_config(tagName="warning", foreground='Darkorange2')

    def log_func(self):
        log_data = self.txt_utils.read(LOG_PATH)
        new_log_data = [i.replace('\n', '') for i in log_data]
        text_box_data = self.log_textbox.get('0.0', 'end').splitlines()

        if new_log_data != text_box_data and len(log_data) != 0:
            self.insert_text_in_textbox(log_data)
        else:
            pass
        self.after(500, self.log_func)

    def insert_text_in_textbox(self, log_data:list[str]):
        self.log_textbox.configure(state='normal')
        self.log_textbox.delete('0.0', 'end')
        log_data[-1] = log_data[-1].rstrip()
        line_number = 1
        for line in log_data:
            self.log_textbox.insert('end', f'{line}')
            index1=f'{line_number}.0'
            index2=f'{line_number}.{len(line)}'
            self.tag_line(line=line, index1=index1, index2=index2)
            line_number += 1
        self.log_textbox.see(index1)
        self.log_textbox.configure(state='disabled')

    def tag_line(self, line:str, index1:str, index2:str):
        if 'ERROR' in line:
            self.log_textbox.tag_add(tagName='error', index1=index1, index2=index2)
        elif 'INFO' in line:
            self.log_textbox.tag_add(tagName='info', index1=index1, index2=index2)
        elif 'WARNING' in line:
            self.log_textbox.tag_add(tagName='warning', index1=index1, index2=index2)
        elif 'CRITICAL' in line:
            self.log_textbox.tag_add(tagName='critical', index1=index1, index2=index2)
        elif 'DEBUG' in line:
            self.log_textbox.tag_add(tagName='debug', index1=index1, index2=index2)
        else:
            self.log_textbox.tag_add(tagName='debug', index1=index1, index2=index2)

    def clear_log(self):
        self.log_textbox.configure(state='normal')
        self.log_textbox.delete('0.0', 'end')
        self.log_textbox.configure(state='disabled')
        self.txt_utils.clear(LOG_PATH)