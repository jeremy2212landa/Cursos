import requests as r

encontrar = 'Retos_Hacking'

lista = ['hola','que_te_parece','chorizo','Retos_Hacking']

urlBase = 'https://github.com/jeremy2212landa'


for fuzz in lista:
    x = r.get(f'{urlBase}/{fuzz}')
    print(x.status_code)
    if x.status_code == 200:
        print(f'Pagina encontrada con la palabra {fuzz}')