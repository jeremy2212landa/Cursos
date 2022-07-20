import re

url = input("\tIngrese el url: ")

'''separators = "//", "."

def custom_split(sepr_list, str_to_split):
    # create regular expression dynamically
    regular_exp = '|'.join(map(re.escape, sepr_list))
    return re.split(regular_exp, str_to_split)

print(custom_split(separators, url))'''

b = re.split('//.', url)
print (b)
for i in range(len(b)):
    

