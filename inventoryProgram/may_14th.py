import os, random, asyncio, time, datetime, openpyxl, pprint, sys
from sys import exit
import tkinter as tk

##Open and read an Excel with inventory list and count of inventory by product and cost

##Define a function to write a negative (deduction) to the count of an inventory item by Product Number

##Define a function to write an addition to the count of an inventory item by Product Number

##Define a function locked by phrase to add or remove inventory products 

##Define a search function that will parse the Excel with Product Name, Product Number, or Product Description to return, Name/description/part#

def main():
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "Hello World\n(click me)"
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="top")

            self.quit = tk.Button(self, text="QUIT", fg="red",
                                  command=self.master.destroy)
            self.quit.pack(side="bottom")

        def say_hi(self):
            print("hi there, everyone!")

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

def start_up():
    result = loading()
    
    if result is True:
        print("Opening Inventory Master...")
        main()
    else:
        print("Failed to start application.")
        sys.exit()

def loading():    
    try:
        wb = openpyxl.load_workbook('invMaster.xlsx')
        sheet = wb['inventory']
        return True
    except:
        return False 



if __name__ == "__main__":
    start_up()
