import customtkinter
from tkinter import *


class PrepList(customtkinter.CTkFrame):
    from user_section import UserSection
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg_color='#131314', fg_color='#1B1A1D', corner_radius=10, border_width=1, border_color='#fff', width=280, height=250)

        font2=('Ariel', 24, 'bold')

        # making the title for the frame
        title3_label = customtkinter.CTkLabel(self, font=font2, text='Prep List', text_color='#fff', bg_color='#1B1A1D')
        title3_label.place(x=38, y=40)

        # We are getting these values from app and imputing them inside our labels for the preplist frame
    def insert_new_values(self, username, position, item_name, item_amount_left, item_amount_to_do, date):

        font1=('Ariel', 15, 'bold')

        # all these labels are essentially blank at first and when the prep list button is clicked they will turn to that value
        self.user_label = customtkinter.CTkLabel(self, font=font1, text=username, text_color='#fff', bg_color='#1B1A1D')
        self.user_label.place(x=10, y=70)
        

        # for every label we need to place it or it will not show up in the frame
        self.position_label = customtkinter.CTkLabel(self, font=font1, text=position, text_color='#fff', bg_color='#1B1A1D')
        self.position_label.place(x=100, y=70)

        self.item_label = customtkinter.CTkLabel(self, font=font1, text=f"Item: {item_name}", text_color='#fff', bg_color='#1B1A1D')
        self.item_label.place(x=10, y=100)

        self.item_amount_left = customtkinter.CTkLabel(self, font=font1, text=f"Amount left: {item_amount_left}", text_color='#fff', bg_color='#1B1A1D')
        self.item_amount_left.place(x=10, y=130)

        self.item_amount_to_do = customtkinter.CTkLabel(self, font=font1, text=f"Amount to do: {item_amount_to_do}", text_color='#fff', bg_color='#1B1A1D')
        self.item_amount_to_do.place(x=10, y=170)
        
        self.date_label = customtkinter.CTkLabel(self, font=font1, text=f"Date: {date}", text_color='#fff', bg_color='#1B1A1D')
        self.date_label.place(x=10, y=210)
