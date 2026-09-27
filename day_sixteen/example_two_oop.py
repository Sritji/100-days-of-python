from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name (Male)", ["Peter", "Paul", "John"])
table.add_column("Name (Female)", ["Mary", "Esther", "Deborah"])

table.align = "r"

print(table)