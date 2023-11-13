import customtkinter
from tkinter import *

class UserSection(customtkinter.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # code to design the frame 
        self.configure(bg_color='#131314', fg_color='#1B1A1D', corner_radius=10, border_width=1, border_color='#fff', width=280, height=250)


        font1=('Ariel', 15, 'bold')
        font2=('Ariel', 24, 'bold')

        # Creating a title for the UserSection frame
        title1_label = customtkinter.CTkLabel(self, font=font2, text="User", text_color='#fff', bg_color='#1B1A1D')
        title1_label.place(x=60, y=40)

        # Creating label for name and placing
        Name_label = customtkinter.CTkLabel(self, font=font1, text='Username', text_color='#fff', bg_color='#1B1A1D')
        Name_label.place(x=20, y=100)

        # crating like a input field for the name label
        self.Name_entry = customtkinter.CTkEntry(self, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=120)
        self.Name_entry.place(x=130, y=100)

        Position_label = customtkinter.CTkLabel(self, font=font1, text='Position', text_color='#fff', bg_color='#1B1A1D' )
        Position_label.place(x=20,y=150)

        self.Position_entry = customtkinter.CTkEntry(self, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=120)
        self.Position_entry.place(x=130, y=150)









        