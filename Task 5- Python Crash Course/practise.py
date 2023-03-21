# Enumerate Function
food_items = ['banana','apple','pizza','juice']
print("Looping through enumerate function:")
for item_no ,food in enumerate(food_items):
    print("Item No:",item_no, " is " , food)
    
#Timing your code

import time
start = time.perf_counter()
food_items = ['banana','apple','pizza','juice']
print("Looping through enumerate function:")
for item_no ,food in enumerate(food_items):
    print("Item No:",item_no, " is " , food)
    
end = time.perf_counter()  # A few seconds later
print(f"Performed the task in {end - start:0.4f} seconds")

# User Inputs
number = int(input("Enter a number to check if its multiple of 10 or not : "))
if number%10 ==0: print("Yes the Number is Multiple of 10")
else: print("No the Number is not a Multiple of 10")

# Conditionals
age = int(input("Enter your age:" ))
if age < 2: print("You are a baby")
elif age >=2 and age<4 : print("You are a toddler")
elif age >=4 and age<13 : print("You are a kid")
elif age >=13 and age<20 : print("You are a teenager")
elif age >=20 and age<65 : print("You are an adult")
else: print("You are an elder")

#Introducing sets 
set1 = {"abc", 34, True, 40, "male"}
print(" The given set has", len(set1), " elements and are as follows:")
print(set1)

# Set Operations
set2 = {"apple", "banana", "cherry"}
set3 = {"google", "microsoft", "apple"}
print("The original sets are as follows:")
print("SET1 :", set2)
print("SET2 :", set3)
union_set = set2.union(set3)
intersection_set = set2.intersection(set3)
difference_set = set2.difference(set3)
symmetric_diff = set2.symmetric_difference(set3)

print("The union of set is :", union_set)
print("The intersection of set is :", intersection_set)
print("The difference of set is :", difference_set)
print("The symmetric difference of set is :", symmetric_diff)

#Making Data Unique with Sets
age_list = [10,11,13,12,11,10,9,8,14,15,15]
print("Suppose we have a age_list of kids who played a game as follows :", age_list)
unique_age = set(age_list)
print("Using set() to find the unique ages of kids that participated :", unique_age)

