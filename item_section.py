import customtkinter
from tkinter import *
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk
# from app import app

class ItemSection(customtkinter.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg_color='#131314', fg_color='#1B1A1D', corner_radius=10, border_width=1, border_color='#fff', width=280, height=250)

        font1=('Ariel', 15, 'bold')
        font2=('Ariel', 24, 'bold')

        title2_label = customtkinter.CTkLabel(self, font=font2, text='Items', text_color='#fff', bg_color='#1B1A1D')
        title2_label.place(x=60, y=40)

        Item_label = customtkinter.CTkLabel(self, font=font1, text='Item name', text_color='#fff', bg_color='#1B1A1D')
        Item_label.place(x=20, y=100)

        self.item_name_entry = customtkinter.CTkEntry(self, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=120)
        self.item_name_entry.place(x=140, y=100)

        amount_left_label = customtkinter.CTkLabel(self, font=font1, text='Amount left', text_color='#fff', bg_color='#1B1A1D' )
        amount_left_label.place(x=20,y=150)

        self.amount_left_entry = customtkinter.CTkEntry(self, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=50)
        self.amount_left_entry.place(x=150,y=150)


        amount_to_do_label = customtkinter.CTkLabel(self, font=font1, text='Amount to do', text_color='#fff', bg_color='#1B1A1D' )
        amount_to_do_label.place(x=20,y=200)

        self.amount_to_do_entry = customtkinter.CTkEntry(self, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=50)
        self.amount_to_do_entry.place(x=150,y=200)

        # parent.prepList1(item_name_entry, amount_left_entry, amount_to_do_entry)



        