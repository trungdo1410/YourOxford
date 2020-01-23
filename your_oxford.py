import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3

### UNDER SKIN PROCESS
class WordProcess():
    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.CheckInput()
        self.root.title("Your Oxford")
    
    def CheckInput(self):
        #id
        Id = Label(self.root, text= "Id")
        Id.grid(row=0, column=0)

        self.Entry_id = Entry(self.root)
        self.Entry_id.grid(row=0, column=1)

        # Original word
        Ogw = Label(self.root, text = "Original Words(En)") #Field to enter the word you found or wondered about
        Ogw.grid(row=1, column=0)
        #Tkinter String variable(original string)
        self.Entry_original_word = Entry(self.root, bd=5)
        self.Entry_original_word.grid(row=1, column=1)

        # Translated word
        Tw = Label(self.root, text = "Translated Words(Vn)") #Field to enter translated word
        Tw.grid(row=2, column=0)
        #Tkinter String variable(translated string)
        self.Entry_translated_word = Entry(self.root, bd=5,)
        self.Entry_translated_word.grid(row=2, column=1)

        # Save button
        self.save_button = ttk.Button(self.root, text="Save", command=self.DbConnection)
        self.save_button.grid(row=4, column=1, padx=(0, 60))
        # Reset button
        self.reset_button = ttk.Button(self.root, text="Reset", command=self.clear_entries)
        self.reset_button.grid(row=4, column=1, padx=(100,0))
    def clear_entries(self):
        self.Entry_original_word.delete(0,END)
        self.Entry_translated_word.delete(0,END)
    
    def get_text(self):
        self.word_id = int(self.Entry_id.get())
        self.string1 = self.Entry_original_word.get()
        self.string2 = self.Entry_translated_word.get()
        self.clear_entries()

    def get_string(self):
        return self.string1, self.string2, self.word_id

    def wait_for_input(self):
        self.root.mainloop()

    def DbConnection(self):
        #Connect to db
        conn = sqlite3.connect("test.db")
        create_table = """CREATE TABLE DICTIONARY
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ORIGINAL_WORD  CHAR(50) NOT NULL,
                        TRANSLATED_WORD CHAR(50) NOT NULL); """
        # conn.execute(create_table)
        # print("Table created successfully")
        #Add to db
        self.get_text()
        insert_word = f"INSERT INTO DICTIONARY (ID, ORIGINAL_WORD,TRANSLATED_WORD) VALUES ('{self.word_id}','{self.string1}', '{self.string2}'); "
        conn.execute(insert_word)
        conn.commit()
        print("Words Added")
        #Get data from db
        # data = conn.execute("SELECT ID,ORIGINAL_WORD,TRANSLATED_WORD FROM DICTIONARY;")
        # for d in data:
        #     print(f"ID: {d[0]} \n" + f"OW: {d[1]} \n" + f"TW: {d[2]}")
        conn.close()
def GetText():
    word_master = WordProcess()
    word_master.wait_for_input()
    # word_master.DbConnection()
GetText()