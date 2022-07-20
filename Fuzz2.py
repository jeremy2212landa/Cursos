import argparse
import requests as r

parser = argparse.ArgumentParser(description='Script en python para hacer fuzzing a una pagina web')
parser.add_argument('-w', type=str, help='Coloca una wordlist')
parser.add_argument('-attack', type=str, help='Pagina web a atacar, con la palabra "FUZZ" al intercambiar en el fuzzing')

args = parser.parse_args()

#print(args.attack)

urlBase = args.attack # 'https://www.google.com' #args.attack #'https://github.com/jeremy2212landa/FUZZ'

encontrar = 'Retos_Hacking'

lineas = [line.rstrip('\n') for line in open(args.w)]
#print(lineas)

# with open('wordlist.txt') as archivo:
#     lineas = archivo.readlines()
#     print(lineas)





for fuzz in lineas:
    url = urlBase.replace('FUZZ', fuzz)
    x = r.get(url)
    print(x.status_code)
    if x.status_code == 200:
        print(f'Pagina encontrada con la palabra {fuzz}')