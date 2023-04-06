# Making and printing a dictionary
glossary = {
    "variable" : "A box to store a value",
    "list" : " Collection of items in a particular order",
    "string" : "Series of Character",
    "comment" : "Allows you to write notes in English",
    "float" : "Any number with a decimal point"
}

print("Here is the list of glossary : \nVariable :", glossary["variable"],"\nList :", glossary["list"],"\nString :", glossary["string"],"\nComment :", glossary["comment"],"\nFloat :", glossary["float"])

# Looping throught dictionary
river_data = {
    "Nile" : "Egypt",
    "Indus" : "Pakistan",
    "Ganges" : "India"
}

for river,country in (river_data.items()):
    print("The " + river + " runs through "+ country)

#Looping with condition
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

selected_people = ['jen','kanwal','phil','qasim']
for people in selected_people:
    if (people not in favorite_languages.keys()):
        print(people, ", Please take our poll")
    else:
        print(people, ", Thank you for taking our poll")
       

# Nested Dictionaries
cities = {
    "Karachi" : {
        "country" : "Pakistan",
        "population" : "14.91 million" ,
        "Fact" : "Largest Economic Hub"
        
    },
    "Islamabad" : {
        "country" : "Pakistan",
        "population" : "1.015 million" ,
        "Fact" : "Capital of Pakistan"
        
    },
    "Lahore": {
        "country" : "Pakistan",
        "population" : "11.13 million" ,
        "Fact" : "Famous for Food"
        
    }
} 

for city,info in cities.items():
    print("-------",city, "-------")
    for label,data in info.items():
        print( label , " : " , data )
    
