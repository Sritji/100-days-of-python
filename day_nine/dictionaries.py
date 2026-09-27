human = {
    "Rotshak": {
        "name": "Rotshak", 
        "class": "JSS1", 
        "age":10 , 
        "hobbies": ["hoby1", "hoby2", "hoby3"]
        }
    }

#getting and printing from dictionary by keys
name = human["Rotshak"]["name"]
print(name)

#add to the list
human["Rotshak"]["hobbies"].append("reading")

#print from the list
hobibies = human["Rotshak"]["hobbies"][3]
print(hobibies)

# Add to dictionary
human["Rotshak"]["school"] = "Greenfield School"

# printing the dictionary
print(human)

#edit item in dictionary
human["Rotshak"]["class"] = "JSS2"
print(human["Rotshak"]["class"])

#looping through a dictionary with normal loops
print("===============================")
for key in human["Rotshak"]:
    print(key)
    print(human["Rotshak"][key])
