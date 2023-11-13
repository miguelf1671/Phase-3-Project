import customtkinter, sqlite3
from tkinter import *
# messagebox is used to pop up a window to communicate an alert or prompt to the user
from tkinter import messagebox
from datetime import date
# PIL is used to get pictures into your project
from PIL import Image, ImageTk

class Myapp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # creating the tittle for the app
        self.title('Prep List')
        # dimensions off the window
        self.geometry('900x350')
        self.config(bg = '#0A0B0C')
        self.resizable(False, False)
        
        # importing modules
        from user_section import UserSection
        from item_section import ItemSection
        from prep_list import PrepList

        font1=('Ariel', 15, 'bold')
        font2=('Ariel', 24, 'bold')

        # placing the frames
        self.users_section_1 = UserSection(self)
        self.users_section_1.place(x=15, y=15)

        # steps you need to take to get a image and place it
        chef_img = Image.open('chef_icon.png')
        resize_img1 = chef_img.resize((50, 50))
        img1 = ImageTk.PhotoImage(resize_img1)

        # this is where you can choose what frame to place it in
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

        save_button = customtkinter.CTkButton(self, command=self.save, font=font1, text_color='#fff', text="Save", fg_color='red3', hover_color='green3', bg_color='#0A0B0C', cursor='circle', corner_radius=25, width=110 )
        save_button.place(x=380, y=280)

        new_button = customtkinter.CTkButton(self, command=self.new, font=font1, text_color='#fff', text="New", fg_color='green4', hover_color='green3', bg_color='#0A0B0C', cursor='circle', corner_radius=25, width=110 )
        new_button.place(x=570, y=280)

        self.mainloop()
    
    def receipt(self):
        from prep_list import PrepList
    

        import database


        # getting the input from the user section and saving it in a variable
        username = self.users_section_1.Name_entry.get()
        position = self.users_section_1.Position_entry.get()

        # Connect to SQL Table for Product Data
        conn = sqlite3.connect("Products.db")
        cursor = conn.cursor()

        # Calculate Length of Table for User ID Increment
        # GET_COUNT_OF_TABLE_SCRIPT = '''SELECT COUNT(*) FROM Users'''
        GET_COUNT_OF_TABLE_SCRIPT = '''SELECT * FROM USERS'''
        NUM_PREEXISTING_USERS = len(cursor.execute(GET_COUNT_OF_TABLE_SCRIPT).fetchall())
        # print(NUM_PREEXISTING_USERS)

        # Get New User Data from Form Submission (GUI) (with Incremented ID)
        new_user_data = (f"U{NUM_PREEXISTING_USERS + 1}", username, position)

        # Add New User Data and Commit to Backend Database
        ADD_USER_SCRIPT = '''INSERT INTO Users (id, username, position) VALUES (?, ?, ?)'''
        cursor.execute(ADD_USER_SCRIPT, new_user_data)
        conn.commit()
        conn.close()

        # getting entry inputs
        item_name = self.items_section.item_name_entry.get()
        amount_left = self.items_section.amount_left_entry.get()
        amount_to_do = self.items_section.amount_to_do_entry.get()

        conn_items = sqlite3.connect("Products.db")
        cursor_2 = conn_items.cursor()

        GET_COUNT_OF_TABLE_ITEMS = '''SELECT * FROM ITEMS'''
        
        # getting number of tables
        NUM_OF_ITEMS = len(cursor_2.execute(GET_COUNT_OF_TABLE_ITEMS).fetchall())
        print(NUM_OF_ITEMS)

        new_items_data = (f"I{NUM_OF_ITEMS + 1}", item_name, amount_left, amount_to_do)
        # print(new_items_data[0])
        ADD_ITEMS_SCRIPT = '''INSERT INTO Items (id, name, amount_left, amount_to_do) VALUES (?, ?, ?, ?)'''
        cursor_2.execute(ADD_ITEMS_SCRIPT, new_items_data)
        conn_items.commit()
        conn_items.close()

        todays_date = date.today().strftime('%d %m %Y')
        
        STR_IS_MORE_THAN_ONE_CHAR = len(username) > 1 and len(position) > 1 and len(item_name) > 1

        try: 
            # making sure inputs are integers
            amount_left = int(amount_left)
            amount_to_do = int(amount_to_do)
        except ValueError:
            amount_left = None
            amount_to_do = None

            # adding conditionals to inputs
        if amount_left and amount_to_do and STR_IS_MORE_THAN_ONE_CHAR:
            self.prep_list_section.insert_new_values(new_user_data[1], new_user_data[2], new_items_data[1], new_items_data[2], new_items_data[3], todays_date)
            return username, position, item_name, amount_left, amount_to_do, todays_date
        else:
            messagebox.showerror('Error','All inputs need to be at least one character long and (amount left) and (amount to do) need to be integers')

    def save(self):
        prep_list = self.receipt()
        # if a prep list is made
        if prep_list is not None:
            username, position, item_name, amount_left, amount_to_do, todays_date = prep_list
            # with opens and closes a file and also makes the file
            # this is to save all inputs into a text file
            with open('Prep-list.txt', 'a') as file:
                file.write(f'Employee name: {username}\n')
                file.write(f'Employee position: {position}\n')
                file.write(f'Item: {item_name}\n')
                file.write(f'Amount left: {amount_left}\n')
                file.write(f'Amount to do: {amount_to_do}\n')
                file.write(f'Date: {todays_date}\n===================\n')
            messagebox.showinfo('Success!','Prep list has been saved.')

    def new(self):
        # clearing any inputs on the entries
        self.users_section_1.Name_entry.delete(0, END)
        self.users_section_1.Position_entry.delete(0, END)

        self.items_section.item_name_entry.delete(0, END)
        self.items_section.amount_left_entry.delete(0, END)
        self.items_section.amount_to_do_entry.delete(0, END)

        self.prep_list_section.user_label.configure(text='')
        self.prep_list_section.position_label.configure(text='')
        self.prep_list_section.item_label.configure(text='')
        self.prep_list_section.item_amount_left.configure(text='')
        self.prep_list_section.item_amount_to_do.configure(text='')
        self.prep_list_section.date_label.configure(text='')

        

        
        

newApp = Myapp()
