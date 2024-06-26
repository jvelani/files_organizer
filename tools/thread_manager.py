import sys
sys.dont_write_bytecode = True
import time
import threading
import customtkinter as ctk
from interface.components.loading_window_ui import LoadingWindow

class ThereadManager(object):
    def __init__(self):
        pass

    def start(self, thread:threading.Thread, master:ctk.CTk):
        self.thread_loading = threading.Thread(target=self.__loading_function, args=(thread, master))
        self.thread_loading.start()
        thread.start()

    def __loading_function(self, thread:threading.Thread, master:ctk.CTk):
        self.loading_window = LoadingWindow(master=master)
        while thread.is_alive():
            time.sleep(0.5)
        self.loading_window.loading_frame.progress_bar.stop()
        self.loading_window.destroy()