# Defining the function
def display_message():
    """Displays what you are learning
    """
    print("I am learning deep learning")

display_message()

# Passsing Values to the Argument
def describe_city(city, country = "Pakistan"):
    print(city, "is in ", country)

describe_city("Karachi")
describe_city("Kabul", "Afghanistan")
describe_city("Delhi", "India")

# Returning Values
def make_album(artist_name, album_title,no_of_tracks = 0):
    if no_of_tracks>0:
        album = {'Artist Name': artist_name, 'Album Title': album_title, "No of Tracks": no_of_tracks}
    else:
         album = {'Artist Name': artist_name, 'Album Title': album_title}
    return album

print(make_album("Fyez Irfan", "Dosti"))
print(make_album("Furqan", "Yeh Zindigi",2))

# Passing the list
magician_list = ["Alexander", "Olivia", "Peter", "Anna"]
def show_magicians(magicians):
    print("The magicians are:")
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for i in range(0,len(magicians)):
        magicians[i] = magicians[i] + " the Great"
    return magicians
new_list = make_great(magician_list[:])
show_magicians(new_list)
print("\nThe original list is below \n")
show_magicians(magician_list)

# Using arbitrary no of arguments
def user_profile(first_name , last_name , **user_description):
    profile = {'First Name ' : first_name , 'Last name' : last_name}
    for key,value in user_description.items():
        profile[key] = value
    return profile

print(user_profile("Kanwal", "Mehreen", age=23 , dept="Software Eng" , Interest= "AI"))
