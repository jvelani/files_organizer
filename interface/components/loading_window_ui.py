import sys
sys.dont_write_bytecode = True
import customtkinter as ctk
from interface.ctk_window_config import window_config
from log.log_logging import report
from CTkMessagebox import CTkMessagebox

class LoadingWindow(ctk.CTkToplevel):
    def __init__(self, master:ctk.CTk):
        super().__init__(master=master)
        self.title("Loading")
        window_config(self, 400, 200)
        self.overrideredirect(True)
        self.focus_force()
        self.grab_set()

        self.grid_rowconfigure(0, weight=1, uniform=True)
        self.grid_columnconfigure(0, weight=1, uniform=True)

        self.loading_frame = LoadingFrame(self)

class LoadingFrame(ctk.CTkFrame):
    def __init__(self, master:ctk.CTkToplevel):
        super().__init__(master=master)
        self.grid(column=0, row=0, padx=10, pady=10, sticky="nswe")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform=True)
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform=True)

        self.label_title = ctk.CTkLabel(self, text="Loading...", font=ctk.CTkFont(size=25, weight="bold"))
        self.label_title.grid(column=0, row=1, columnspan=3, padx=10, pady=0, sticky="nswe")

        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.grid(column=0, row=3, columnspan=3, padx=25, pady=3, sticky="nswe")
        self.progress_bar.configure(mode="indeterminate")
        self.progress_bar.start()

        self.button_cancel = ctk.CTkButton(self, text='Cancel', command=self.func_cancel)
        self.button_cancel.grid(column=1, row=5, padx=10, pady=0, sticky="nswe")

    def func_cancel(self):
        msg = CTkMessagebox(title="Warning!", message="Input and Output diretories can`t be the same!", icon="warning", option_1="Yes", option_2="No")
        if msg.get() == "Yes":
            report(f'The program as finished with SystemExit!', 'critical')
            sys.exit()
        else:
            pass