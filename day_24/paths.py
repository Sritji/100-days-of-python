# Relative path: ./new_file.txt
# Absolute path: /Users/yilkudiritji/Desktop/development/Python 100/day_24/new_file.txt 
with open("/Users/yilkudiritji/Desktop/development/Python 100/day_24/new_file.txt") as file:
    content = file.read()
    print(content)