import sys
sys.dont_write_bytecode = True
from interface.main_ui import Application
from functions.create_default_files import create_default_files

if __name__ == "__main__":
    create_default_files()
    app = Application()
    app.mainloop()