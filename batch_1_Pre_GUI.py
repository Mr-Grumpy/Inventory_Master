import os, random, asyncio, time, datetime, openpyxl, pprint, sys, queue, dotenv
import datetime, time;
from sys import exit


##Open and read an Excel with inventory list and count of inventory by product and cost

##Define a function to write a negative (deduction) to the count of an inventory item by Product Number

##Define a function to write an addition to the count of an inventory item by Product Number

##Define a function locked by phrase to add or remove inventory products 

##Define a search function that will parse the Excel with Product Name, Product Number, or Product Description to return, Name/description/part#

functions_list = ["Sign In", "Sign Out", "Close App", "List Active Jobs"]
workbook = openpyxl.load_workbook('invMaster.xlsx')
task = []
job_hold = []
dt = datetime.datetime.now()
date_now = dt.strftime("%b, %d")

##item_hold = []

def start_up():
    
    try:
        print("Open excel sheet: " + str(workbook.active))
        print("List of tasks:")
        for i in range(0, len(functions_list)):
            print("-" + functions_list[i])
        main()
            
    except:
        print("No open excel sheet. Goodbye.")
        sys.exit()


def main():
    o = input("What task would you like to preform?\n").lower()
    if o == "sign out":
        task.append(o)
        job_check()
    elif o == "sign in":
        task.append(o)
        job_check()
    elif o == "close app":
        close_app()
    elif o == "list active jobs":
        active_jobs()
    else:
        print("I do not recognize this task.\n")
        main()

def job_check():
    x = input("What job would you like to " + task[0] + " items for?\n")
    job_ = x + '\n'
    with open('Job Numbers.txt') as f:
        if job_ in f.readlines():
            if task[0] == "sign out":
                job_hold.append(job_)
                f.close()
                task.clear()
                sign_out()
            elif task[0] == "sign in":
                job_hold.append(job_)
                f.close()
                task.clear()
                sign_in()
##            elif task[0] == "close app":
##                job_hold.append(job_)
##                f.close()
##                task.clear()
##                close_app()
##            elif task[0] == "list active jobs":
##                job_hold.append(job_)
##                f.close()
##                task.clear()
##                active_jobs()
        else:
            print("Please enter a valid job number.")
            job_check()
    



def sign_in():
    sheet = workbook.active
    item_ = input("What item would you like to return against " + job_hold[0].replace('\n','') + "?\n")
    for n in range(1, 600):
        valid_ = True
        if item_ == str(sheet['A'+str(n)].value):
            break
        else:
            valid_ = False
        
    if valid_ == True:
        quantity_ = input("How many?\n")
        print("Returned " + quantity_ + "pc's of "  + item_ + " back against " + job_hold[0])
        file_name = (date_now + ".txt")
        time_stamp = open(file_name, "a+")
        time_stamp.write("Returned " + quantity_ + "pc's of " + item_ + " (" + str(sheet['B'+str(n)].value) + ")" + " against " + job_hold[0])
        time_stamp.close()
        o = input("Is there anything else you'd like to charge against " + job_hold[0] + "?\n" + "Y/N.").lower()
        if o == "y":
            sign_in()
        else:
            task.clear()
            job_hold.clear()
            main()
    else:
        print("Not a valid item.")
        sign_in()
    

def sign_out():
    sheet = workbook.active
    item_ = input("What item would you like to sign out against " + job_hold[0].replace('\n','') + "?\n")
    for n in range(1, 600):
        valid_ = True
        if item_ == str(sheet['A'+str(n)].value):
            break
        else:
            valid_ = False
        
    if valid_ == True:
        quantity_ = input("How many?\n")
        print("Signed out " + quantity_ + "pc's of "  + item_ + " against " + job_hold[0])
        file_name = (date_now + ".txt")
        time_stamp = open(file_name, "a+")
        time_stamp.write("Signed out " + quantity_ + "pc's of " + item_ + " (" + str(sheet['B'+str(n)].value) + ")" + " against " + job_hold[0])
        time_stamp.close()
        o = input("Is there anything else you'd like to charge against " + job_hold[0] + "?\n" + "Y/N.").lower()
        if o == "y":
            sign_out()
        else:
            task.clear()
            job_hold.clear()
            main()
    else:
        print("Not a valid item.") 
        sign_in()



def close_app():
    x = input('Are you sure you wish to close the program?\n' + 'Y/N.\n').lower()
    if x == 'y':
        sys.exit()
    else:
        main()


def active_jobs():
    with open('Job Numbers.txt') as f:
         list_jobs = f.readlines()
         for line in list_jobs:
             print(line)
    f.close()
    main()


                    
if __name__ == "__main__":
    start_up()
