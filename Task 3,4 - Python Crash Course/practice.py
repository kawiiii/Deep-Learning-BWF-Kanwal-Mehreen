
# ----- Chapter 2: Variables and Simple Data Types
# Variables
message = "This is a secret message"
print(message)
message = "New message"

#String
name = "Kanwal"
print("Hello",name, "! How are you ?")
print("Uppercase = " , name.upper())
print("Lowercase = " , name.lower())
print("Titlecase = " , name.title())
famous_person = "Albert Einstein"
print("\t",famous_person, 'once said, \x1B[0m “A person who never made a mistake never tried anything new."')
name_with_spaces = "      Kanwal         "
print("Name with rstrip", name_with_spaces.rstrip())
print("Name with lstrip", name_with_spaces.lstrip())
print("Name with strip", name_with_spaces.strip())


#Numbers
print("5 + 3 = ", 5+3)
print("4 * 2 = ", 4*2)
print("10 - 2 = ", 10 - 2)
print("16 / 2 = ", 16//2)
fav_number = 7
print("My fav number is ", fav_number)

#Lists
friends = ["Tom", "Peter", "Max", "Anna"]
print("My first friend from the list of friend is : ", friends[0])
print("My last friend from the list of friend is : ", friends[-1])
guests = ["Alex", "Anna", "Bob"]
print("Currently I have invited ", len(guests) , "guests to the party")
print("Lets invite Qasim too and add him at the end of the invite list")
guests.append("Qasim")
print("Also, add Prime Minister and send him invitation at first place")
guests.insert(0 , "Prime Minister")
print("Now I have", len(guests) , "guests that are invited to the party")
print("Sorting the guest list in alphabetical order" , sorted(guests))
guests.reverse()
print("Sorting the guest list in reverse alphabetical order" , guests )

food_items = ["apple", "cake" , "pizza", "shake"]
for food in food_items:
    print ("I love",food)

multiples = [num for num in range(3,31) if num%3==0]
print("Multiples of 3 from 3-30 using List Comprehension", multiples)

print("The first two elements in list are : " , food_items[0:2])
print("The last two elements in list are : " , food_items[-2:])


for friend in friends:
    for food in food_items:
        if friends.index(friend) == food_items.index(food): 
            print(friend," likes " , food)


# Tuples
simple_food = ('bread', 'butter' , 'chicken','juice')
print('The restaurant offers the following simple foods:')
for food in simple_food:
    print(food)

new_food = ('cake', 'pizza' , 'chicken','juice')
print('The modified food list is as follows:')
for food in new_food:
    print(food)

# Wring Styling

fav_number = 7  # Initializing my number
t          =  "My fav number is "  
print("5 + 3 = " , 5 + 3)
print("4 * 2 = " , 4 * 2)
print(t , fav_number)
    
# Correct Styling 
fav_number = 7  
text =  "My fav number is "  
print("5 + 3 = ", 5 + 3)
print("4 * 2 = ", 4 * 2)
print(text , fav_number)

