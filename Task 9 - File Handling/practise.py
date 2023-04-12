#Reading the File
with open('learning_python.txt') as file_obj:
    lines = file_obj.readlines()
print("\nReading the learning_python.txt file --------")
for line in lines:
    print(line.rstrip())

# Replacing in File
print("Replacing the learning_python.txt file --------")
for line in lines:
    print(line.replace('Python', 'Java').rstrip())
 
# Writing into file
with open('guests.txt','w') as file_obj:
    name = input("Please Enter your Name or End to Exit:")
    while name!= 'End':        
        file_obj.write(name + "\n")
        name = input("Please Enter your Name or End to Exit:")


# Excepion Handling
print("Enter Two Numbers for Addition or Press 'q' to Quit")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can only add numbers")
    else:
        print("The result of addition is :" , answer)
