import sys
sys.dont_write_bytecode = True
import os
import customtkinter as ctk
from PIL import Image

icons_path = f'{os.path.abspath(os.curdir)}/interface/icons'

clear_image = ctk.CTkImage(light_image=Image.open(f'{icons_path}/broom.png'))
organize_image = ctk.CTkImage(light_image=Image.open(f'{icons_path}/tornado.png'))
main_icon_image = ctk.CTkImage(light_image=Image.open(f'{icons_path}/tornado.png'), size=(30, 30))
main_icon_path = f'{icons_path}/tornado.ico'