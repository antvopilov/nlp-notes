table_dict = {"e": "m"}
table = str.maketrans(table_dict)

s = "one"
r = s.translate(table)
print(r)  # onm
