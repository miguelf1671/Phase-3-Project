import sqlite3

def create_tables():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS Users''')
    cursor.execute('''DROP TABLE IF EXISTS Items''')
 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id TEXT PRIMARY KEY,
            username TEXT,
            position TEXT)''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Items (
           id TEXT PRIMARY KEY,
           name TEXT,
           amount_left INTEGER,
           amount_to_do INTEGER)''')
    
    conn.commit()
    conn.close()

def insert_items():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()

    items_data = [
        ('I1', 'ground beef', 10, 3),
        ('I2', 'scallions', 3, 5),
        ('I3', 'duck sauce', 5, 5)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Items (id, name, amount_left, amount_to_do) VALUES (?, ?, ?, ?)', items_data)

    users_data = [
        ('U1', 'miguel', 'garde manger'),
        ('U2', 'robert', 'sous chef'),
        ('U3', 'andrew', 'line cook')
    ]

    cursor.executemany('INSERT OR IGNORE INTO Users (id, username, position) VALUES (?, ?, ?)', users_data)

    conn.commit()
    conn.close()

def get_product_amounts():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name FROM Items')
    item_name = [row[0] for row in cursor.fetchall()]

    cursor.execute('SELECT amount_left FROM Items')
    item_amount_left = [row[0] for row in cursor.fetchall()]

    cursor.execute('SELECT amount_to_do from Items')
    item_amount_to_do = [row[0] for row in cursor.fetchall()]

    cursor.execute('SELECT username FROM Users')
    user_name = [row[0] for row in cursor.fetchall()]

    conn.close()
    return item_name, item_amount_left, item_amount_to_do, user_name
    
create_tables()
insert_items()





