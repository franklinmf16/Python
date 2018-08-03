import json

filename = 'user.json'

def add_username(username_input):
    with open(filename, 'a') as file_object:
        json.dump(username_input, file_object)
        print("Welcome " + username_input + " we'll remember you next time")

def greet_user(username_input):
    try:
        with open(filename) as file_object:
            file_info = json.load(file_object)
    except FileNotFoundError:
        add_username(username_input)
    else:
        print(file_info)
        # if file_info == username_input:
        #     print("Welcome back, " + file_info) 
        # else:
        #     add_username(username_input)

username = input("what's your name ")
greet_user(username)




