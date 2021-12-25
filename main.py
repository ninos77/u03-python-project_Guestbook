
class User():
    def __init__(self,id,name, email):
        self.id = id
        self.name = name
        self.email = email


import csv

#We have to install Pandas--> https://pandas.pydata.org/docs/getting_started/install.html
import pandas as pd


#to check if users have entered an integer
def check_user_input_int(question):
    while True:
        try:
            int_input = int(input(question))
            break
        except ValueError:
            print('You have to enter an integer')
            pass
        
    return int_input

#to check if users have entered string not empty 
def check_user_input_str(question):
    while True:
        str_input = input(question)
        if str_input and str_input.strip():
            break
        else:
            print('Your input is empty, you have to enter somthing ')
            pass   
    return str_input

#create ID  when users write a post in guestbook
def generate_user_id():
    df = pd.read_csv('data.csv', delimiter=',')
    list_of_rows = [list(row) for row in df.values]
    user_id = len(list_of_rows) + 1  
    for row in list_of_rows:
        if user_id == row[0]:
            user_id = list_of_rows[-1][0]+1
    return user_id

# print csv file contents
def print_csv_data():
    print("==================== ALl Messages ==========================================")
    file_csv = pd.read_csv('data.csv',index_col=0)
    if not file_csv.empty:
        print(file_csv)
    else:
        print("")
        print("                 THERE IS NO MESSAGES     \n")    
    print("============================================================================ \n")
