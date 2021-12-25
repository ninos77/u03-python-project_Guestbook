
class User():
    def __init__(self,id,name, email):
        self.id = id
        self.name = name
        self.email = email


import csv

#We have to install Pandas--> https://pandas.pydata.org/docs/getting_started/install.html
import pandas as pd

#a constant list with 3 choice. Will used to(write,update,delete) and (name,email,message)
OPTIONS = [1,2,3]


#verify right option
def is_options(value):
    try:
        int_val = int(value)
        if int_val in OPTIONS:
            return True
        else:
            return False
    except ValueError:
      return False


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


#create ID when users write a post in guestbook
def generate_user_id():
    df = pd.read_csv('data.csv', delimiter=',')
    list_of_rows = [list(row) for row in df.values]
    user_id = len(list_of_rows) + 1  
    for row in list_of_rows:
        if user_id == row[0]:
            user_id = list_of_rows[-1][0]+1
    return user_id

# get all id from csv.file to use it in another functions
def get_id_list():
    data = pd.read_csv("data.csv")
    list_id = []
    for i in data['id']:
        list_id.append(i)
    return list_id 


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


# write a post in guestbook(csv.file) with (name,email,message)
def insert_data():
    with open('data.csv', 'a+') as f:
        w = csv.writer(f)
        save = "y"
        while save == "y":
            user= User(generate_user_id(),check_user_input_str("Enter your name: ")
            ,check_user_input_str("Enter Email: "))
            message = check_user_input_str("Write your message: ")
            save = input("Would you like to save? Y/N: ").lower()
            if save == "y":
                w.writerow([user.id,user.name,user.email,message])
                print("---Your data has been saved---")
                save = "no"

# delete post from csv.file by id number
def delete_data():
    while True:
        row_to_delete = check_user_input_int("Enter Id number for the record you want to delete: ")
        if row_to_delete in get_id_list():
            data = pd.read_csv("data.csv")
            data = data.drop(data.index[data['id']==row_to_delete])
            print("\n---Your data has been deletet---\n")
            data.to_csv('data.csv',index=False)
            print_csv_data()
            break
        else:
            print("There is no record for this id") 

# update the post based on your choice(email,name,message)
def update_data():
    while True:
        row_to_update = check_user_input_int("Enter Id number for the record you want to update: ")
        if row_to_update in get_id_list():
            print('choose one from options below')
            print('1.Update name')
            print('2.Update email')
            print('3.Update message')
            choice = check_user_input_int("Enter your choice: ")
            while is_options(choice) == False:
                choice = check_user_input_int(f"Please make your right choice between ({str(OPTIONS[0])}-{str(OPTIONS[-1])}): ")      
            data = pd.read_csv("data.csv")
            index_to_update = data.index[data['id']==row_to_update]
            if choice == 1:
                name = check_user_input_str("Enter name: ")
                data.loc[index_to_update,"name"] = name
            elif choice == 2:
                email = check_user_input_str("Enter email: ")
                data.loc[index_to_update,"email"] = email
            elif choice == 3:
                message = check_user_input_str("Enter message: ")
                data.loc[index_to_update,"message"] = message        
            data.to_csv('data.csv',index=False)
            print("\n---Your data has been updated---\n")
            print_csv_data()
            break
        else:
            print("There is no record for this id ") 
 
print_csv_data()
#insert_data()
#delete_data()
#update_data()
#print_csv_data()