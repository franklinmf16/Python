class User():
    def __init__ (self, first_name, last_name, *other_info):
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info
    
    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.other_info)
    
    def greet_user(self):
        print("Welcome back " + self.last_name + "!")

class Privilege():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("privileges are", end = ' ')
        for privilege in self.privileges:
            print(privilege, end = ' ')    

class Admin(User):
    def __init__(self, first_name, last_name, *other_info):
        super().__init__(first_name, last_name, *other_info)
        self.privileges = Privilege()
    

new_user = User('Andy', 'Tim', 'tim@gmail.com', '23 years old' )
new_admin = Admin('Bok', 'BB', 'Bok@gmail.com', '26 years old' )

# new_user.describe_user()
# new_user.greet_user()

new_admin.describe_user()
new_admin.privileges.show_privileges()








