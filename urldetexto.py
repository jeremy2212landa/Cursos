import re

url= input('introducir url: ')
#https://github.io/jeremy2212landa/Pentest/blob/main/OWASP.md?control=99
urlmodificada= url.split('/')
sud= list()
sud2=""
print(urlmodificada)
for index, u in enumerate(urlmodificada):
    if index== 0:
        if u== 'https:':
            print('protocolo seguro, port 443') 
        elif u== 'http:': 
            print('protocolo inseguro, port 80')
        else:
            print('urlinvalido')
    if index== 2:
        lit= re.search(r"\.\w{2,3}", u)
        s = lit.start()
        e = lit.end()
        print(f'Su dominio es: {u}\n')
        print(f'el tipo de dominio es: {u[s+1:e]}\n')
        #if lit:
        #    split = u.split('.')
        #    print(f'el tipo de dominio es: {u[6:10]}\n')
    if index >=3:
        print(u,end='/')
        var_match = re.search(r'\?', u)
        if var_match:
            splitt = u.split('?')
            break 
print(f'\ntu variable es {splitt[1]}')
