# creating a class
class User:
    def __init__(self,first_name , last_name, age,occupation) -> None:
        self.fname = first_name
        self.lname = last_name
        self.age= age
        self.occupation = occupation
        
    def describe_user(self):
        print("The details of user", self.fname + " " + self.lname , "is as follows : ")
        print("Age :" , self.age)
        print("Occupation : ", self.occupation)
        
    def greet_user(self):
        print("Welcome ! " , self.fname + " " + self.lname)

user1 = User("Kanwal", "Mehreen", 23 , "Student")
user1.greet_user()
user1.describe_user()

# Working with Classes & Instances
class User:
    def __init__(self,first_name , last_name, age,occupation) -> None:
        self.fname = first_name
        self.lname = last_name
        self.age= age
        self.occupation = occupation
        self.login =1 
        
    def describe_user(self):
        print("\nThe details of user", self.fname + " " + self.lname , "is as follows : ")
        print("Age :" , self.age)
        print("Occupation : ", self.occupation)
        
    def greet_user(self):
        
        print("Welcome ! " , self.fname + " " + self.lname)

    def login_attempts(self):
        self.login+=1
    
    def reset_login_attempts(self):
        self.login = 0
    
user1 = User("Kanwal", "Mehreen", 23 , "Student")
user1.greet_user()
print("The count of login attempt is : ", user1.login)
print("\nSuppose the user has logged in again\n")
user1.login_attempts()
print("The updated count of login attempt is : ", user1.login)
print("\nReset the login attempts\n")
user1.reset_login_attempts()
print("The count of login attempt after reset is : ", user1.login )
user1.describe_user()

# Inheritance
class Admin(User):
    def __init__(self, first_name, last_name, age, occupation, priviliges) -> None:
        super().__init__(first_name, last_name, age, occupation)
        self.priviliges = priviliges
        
    def show_priviliges(self):
        print("The priviliges of Admin are as follows:")
        for privilige in self.priviliges:
            print("Admin can :" , privilige)

admin1 = Admin("Kanwal", "Mehreen", 23, "Student", ["Can Add Post", "Can Delete Post","Can Ban User"])
admin1.show_priviliges()
        
        






    