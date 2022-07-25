import re
url = input("\tIngrese el url: ")

'''separators = "//", "."
def custom_split(sepr_list, str_to_split):
    # create regular expression dynamically
    regular_exp = '|'.join(map(re.escape, sepr_list))
    return re.split(regular_exp, str_to_split)
print(custom_split(separators, url))'''

b = re.split('//', url)
print (b)

if b[0] == 'http:':
    print('Esta pagina esta usando un protocolo sin capa de seguridad SSL')
elif b[0] == 'https:':
    print('Esta pagina esta usando un protocolo con capa de seguridad SSL')

