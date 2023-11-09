import customtkinter
from tkinter import *
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk

class PrepList(customtkinter.CTkFrame):
    from user_section import UserSection
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg_color='#131314', fg_color='#1B1A1D', corner_radius=10, border_width=1, border_color='#fff', width=280, height=250)

        font1=('Ariel', 15, 'bold')
        font2=('Ariel', 24, 'bold')

        title3_label = customtkinter.CTkLabel(self, font=font2, text='Prep List', text_color='#fff', bg_color='#1B1A1D')
        title3_label.place(x=38, y=40)

        self.user_label = customtkinter.CTkLabel(self, font=font1, text='', text_color='#fff', bg_color='#1B1A1D')
        self.user_label.place(x=10, y=50)

        self.item_label = customtkinter.CTkLabel(self, font=font1, text='', text_color='#fff', bg_color='#1B1A1D')
        self.item_label.place(x=10, y=90)

        self.item_amount_left = customtkinter.CTkLabel(self, font=font1, text='', text_color='#fff', bg_color='#1B1A1D')
        self.item_amount_left.place(x=10, y=130)

        self.item_amount_to_do = customtkinter.CTkLabel(self, font=font1, text='', text_color='#fff', bg_color='#1B1A1D')
        self.item_amount_to_do.place(x=10, y=170)

        self.date_label = customtkinter.CTkLabel(self, font=font1, text='', text_color='#fff', bg_color='#1B1A1D')
        self.date_label.place(x=10, y=210)
