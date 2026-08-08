#list to store many pieces of related data
states_of_nigeria = ["Plateau", "Abuja", "Imo"]
print(states_of_nigeria)

#Replace something on the list
states_of_nigeria[1] = "Ekiti"
print(states_of_nigeria)

#Append a list - Add an item to a list
states_of_nigeria.append("Jos")
print(states_of_nigeria)

#Extend a list - Add a list to a list
states_of_nigeria.extend(["One", "Two"])
print(states_of_nigeria)

num_of_states = len(states_of_nigeria)
print(states_of_nigeria[num_of_states - 1])

