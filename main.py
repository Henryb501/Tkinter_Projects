<<<<<<< Updated upstream
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Henry')
=======
from tkinter import *
import sqlite3

# Create the database and set up the cursor for you
conn = sqlite3.connect('Tutorial.db')
cu = conn.cursor()

app = Tk()
app.title("My Address Book")
app.geometry("500x500")

# all DATABASE functions go at the top of your program
def create_table():
    cu.execute("CREATE TABLE IF NOT EXISTS people(name TEXT,age INTEGER,height TRAL)")

def data_entry(name, age, height):
    cu.execute('INSERT INTO people VALUES(?,?,?)', (name, age, height))
    conn.commit()
    # add treeview row insert here

def get_data():
    cu.execute('SELECT rowid, * FROM people')
    data = cu.fetchall()
    for d in data:
        print(d)
        # Here need to reload the treeview here
        # new code
def update():
    cu.execute('UPDATE people SET age = 30 WHERE rowid = 1')
    conn.commit()
    get_data()

def delete():
    cu.execute('DELETE FROM people WHERE rowid = 1')
    conn.commit()
    get_data()

# all other functions go here


# Add your program here

get_data()
app.mainloop()
conn.close()
>>>>>>> Stashed changes
