#mode by default is r ( read only) to write use w
# a to add
    # file = open("my_file.txt")
    # file.close()
# in w mode, if file does not exist it creates it

with open("new_file.txt", mode="a") as file: # using ass incase you forget to close file


    file.write("\nNew Text to write in addition to old text")

 






 



