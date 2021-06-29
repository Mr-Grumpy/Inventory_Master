import os, random, asyncio, time, datetime, openpyxl, pprint, sys, queue, dotenv
from sys import exit

##Open and read an Excel with inventory list and count of inventory by product and cost

##Define a function to write a negative (deduction) to the count of an inventory item by Product Number

##Define a function to write an addition to the count of an inventory item by Product Number

##Define a function locked by phrase to add or remove inventory products 

##Define a search function that will parse the Excel with Product Name, Product Number, or Product Description to return, Name/description/part#

active_job = []
query_item = False
wb = 'invMaster.xlsx'

def main():
    task = input("What can I do for you, boss?\n")
    if task == 'signout':
        sign_out()
    elif task == 'signin':
        sign_in()
    else:
        print("Command not recognized;")
        main()
    
def start_up():
    result = loading()
    
    if result is True:
        print("Opening Inventory Master...")
        main()
    else:
        print("Failed to start application.")
        sys.exit()

##def open_wb():
##    wb = openpyxl.load_workbook('invMaster.xlsx', {'constant_memory': True})
##    
def loading():    
    try:
        WorkBook = openpyxl.load_workbook(wb)
        return True
    except:
        return False


def sign_out():
    active_job.clear()
    query = input('What job would you like to check items out for?\n')
    job_number = query + '\n'
    with open('Job Numbers2.txt') as f:
            if job_number in f.readlines():
                active_job.append(job_number)
##                item_query = input("What would you like to charge against " + query + "?")
                WorkBook = openpyxl.load_workbook(wb)
                print(WorkBook.sheetnames)
##                if item_query in sheet["A"]:
##                    input("How many of this item?")
                    
                    
            else:
                print("Please enter a valid or active job number.")
                sign_out()

def sign_in():
    wb = open_wb()    


if __name__ == "__main__":
    start_up()
