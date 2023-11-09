import customtkinter, sqlite3
from tkinter import *
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk

class Myapp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Prep List')
        self.geometry('900x350')
        self.config(bg = '#0A0B0C')
        self.resizable(False, False)
        
        
        from user_section import UserSection
        from item_section import ItemSection
        from prep_list import PrepList

        font1=('Ariel', 15, 'bold')
        font2=('Ariel', 24, 'bold')


        self.users_section_1 = UserSection(self)
        self.users_section_1.place(x=15, y=15)

        chef_img = Image.open('chef_icon.png')
        resize_img1 = chef_img.resize((50, 50))
        img1 = ImageTk.PhotoImage(resize_img1)
        chef_img_label = Label(self.users_section_1, image=img1, bg='#1B1A1D')
        chef_img_label.place(x=140, y=20)

        self.items_section = ItemSection(self)
        self.items_section.place(x=310, y=15)

        prep_img = Image.open('butchering.png')
        resize_img2 = prep_img.resize((50, 50))
        img2 = ImageTk.PhotoImage(resize_img2)
        prep_img_label = Label(self.items_section, image=img2, bg='#1B1A1D')
        prep_img_label.place(x=140, y=20)

        self.prep_list_section = PrepList(self)
        self.prep_list_section.place(x=605, y=15)

        prep_list_img = Image.open('meal.png')
        resize_img3 = prep_list_img.resize((50, 50))
        img3 = ImageTk.PhotoImage(resize_img3)
        prep_list_img_label = Label(self.prep_list_section, image=img3, bg='#1B1A1D')
        prep_list_img_label.place(x=160, y=20)

        self.receipt_button = customtkinter.CTkButton(self, command=self.receipt, font=font1, text_color='#fff', text="Prep List", fg_color='navy', hover_color='green3', bg_color='#0A0B0C', cursor='circle', corner_radius=25, width=110 )
        self.receipt_button.place(x=190, y=280)

        save_button = customtkinter.CTkButton(self, font=font1, text_color='#fff', text="Save", fg_color='red3', hover_color='green3', bg_color='#0A0B0C', cursor='circle', corner_radius=25, width=110 )
        save_button.place(x=380, y=280)

        new_button = customtkinter.CTkButton(self, font=font1, text_color='#fff', text="New", fg_color='green4', hover_color='green3', bg_color='#0A0B0C', cursor='circle', corner_radius=25, width=110 )
        new_button.place(x=570, y=280)

        self.mainloop()

    
    def receipt(self):
        from prep_list import PrepList
    

        import database

        # users_section2 = UserSection
        # items_section2 = ItemSection


        username = self.users_section_1.Name_entry.get()
        position = self.users_section_1.Position_entry.get()

        # Connect to SQL Table for Product Data
        conn = sqlite3.connect("Products.db")
        cursor = conn.cursor()

        # Calculate Length of Table for User ID Increment
        # GET_COUNT_OF_TABLE_SCRIPT = '''SELECT COUNT(*) FROM Users'''
        GET_COUNT_OF_TABLE_SCRIPT = '''SELECT * FROM USERS'''
        NUM_PREEXISTING_USERS = len(cursor.execute(GET_COUNT_OF_TABLE_SCRIPT).fetchall())
        print(NUM_PREEXISTING_USERS)

        # Get New User Data from Form Submission (GUI) (with Incremented ID)
        new_user_data = (f"U{NUM_PREEXISTING_USERS + 1}", username, position)

        # Add New User Data and Commit to Backend Database
        ADD_USER_SCRIPT = '''INSERT INTO Users (id, username, position) VALUES (?, ?, ?)'''
        cursor.execute(ADD_USER_SCRIPT, new_user_data)
        conn.commit()
        conn.close()

        item_name = self.items_section.item_name_entry.get()
        amount_left = self.items_section.amount_left_entry.get()
        amount_to_do = self.items_section.amount_to_do_entry.get()

        # user_entries = [username, position]
        # item_entries = [item_name, amount_left, amount_to_do]
        item_name, amount_left, amount_to_do, username= database.get_product_amounts()
        # try: 
        #     items_quantities = []
        #     for entry in user_entries:
        #         text = entry
        #         if text:
        #             items_quantities.append(text)
        #         else:
        #             items_quantities.append(0)
        #     user_quantities = []
        #     for entry in item_entries:
        #         text = entry
        #         if text:
        #             user_entries.append(text)
        #         else:
        #             user_quantities.append(0)
            # todays_date = date.today().strftime('%d %m %Y')
        # except ValueError:('')
        prep_list_section2 = PrepList(self)
        user_label = prep_list_section2.user_label
        item_label = prep_list_section2.item_label
        item_amount_left = prep_list_section2.item_amount_left
        item_amount_to_do = prep_list_section2.item_amount_to_do
        # date = prep_list_section2.date_l
        user_label.configure(text=f'User: {username}')
        item_label.configure(text=f'Item name: {item_name}')
        item_amount_left.configure(text=f'Amount left: {amount_left}')
        item_amount_to_do.configure(text=f'Amount to do: {amount_to_do}')
        # date.configure(text=f'Date:{todays_date}')
        return username, item_name, amount_left, amount_to_do

        

        
        

newApp = Myapp()
