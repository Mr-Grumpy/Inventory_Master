import os, random, asyncio, time, datetime, openpyxl, pprint, sys, queue, dotenv
from sys import exit

##Open and read an Excel with inventory list and count of inventory by product and cost

##Define a function to write a negative (deduction) to the count of an inventory item by Product Number

##Define a function to write an addition to the count of an inventory item by Product Number

##Define a function locked by phrase to add or remove inventory products 

##Define a search function that will parse the Excel with Product Name, Product Number, or Product Description to return, Name/description/part#

active_job = []
action = []
work_book = openpyxl.load_workbook('invMaster.xlsx')
retain = []
quantity = []

def main():
    action.clear()
    
    task = input("What can I do for you, boss?\n")
    if task == 'signout':
        action.append(task)
        job_number_()
    elif task == 'signin':
        action.append(task)
        job_number_()
    elif task == 'close':
        safe_close()
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

def loading():    
    try:
        print("loading work")
        print(work_book)
        return True
    except:
        return False


def job_number_():
    active_job.clear()
    retain.clear()
    query = input('What job would you like to check items out for?\n')
    job_number = query + '\n'
    retain.append(query)
    with open('Job Numbers.txt') as f:
            if job_number in f.readlines():
                active_job.append(job_number)
                if action[0] == "signout":
                    sign_out()
                elif action[0] == "signin":
                    sign_in()
                                 
            else:
                print("Please enter a valid or active job number.")
                job_number_()

def sign_in():
    sheet = work_book.active
    print(sheet)
    item_query = input("What would you like to put back for " + retain[0] + "?\n")
    for n in range(1, 600):
        if item_query == str(sheet['A'+str(n)].value):
            quantity.clear()
            x = input("How many " + item_query + " would you like to put back against " + retain[0] + "\n")
            quantity.append(x)
            print("Signed in " + quantity[0] + " - " + item_query)
            y = input("Is there anything else you'd like to put back against " + retain[0])
            if y == "yes":
                quantity.clear()
                sign_in()
            elif y == "no":
                active_job.clear()
                retain.clear()
                quantity.clear()
                action.clear()
                main()
        else:
            print("I couldn't find that item, please try again:\n")
            sign_in()
          
def sign_out():
    sheet = work_book.active
    print(sheet)
    item_query = input("What would you like to charge against " + retain[0] + "?\n")
    for n in range(1, 600):
        if item_query == str(sheet['A'+str(n)].value):
            quantity.clear()
            x = input("How many " + item_query + " would you like to charge against " + retain[0] + "\n")
            quantity.append(x)
            print("Signed out " + quantity[0] + " - " + item_query)
            y = input("Is there anything else you'd like to sign out against " + retain[0])
            if y == "yes":
                quantity.clear()
                sign_out()
            elif y == "no":
                active_job.clear()
                retain.clear()
                quantity.clear()
                action.clear()
                main()
        else:
            print("I couldn't find that item, please try again:\n")
            sign_out()

def safe_close():
    print("Ight, fuck you then I guess? Buh-bye!")
    sys.exit()
                    
if __name__ == "__main__":
    start_up()


##    for column in range(sheet.ncolumns):
##        column_value = sheet.column_values(column)
##        if column_value[n]
