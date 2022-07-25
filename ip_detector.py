import re

ip = str(input('Escriba una direccion ip: '))
i = 0
#match
#search

ipmatch = re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ip) 			# IP ADDRESS REGULAR EXPRESSION.

if not ipmatch:
	print(f"La IP = {ip} Colocada no tiene un formato correcto.")
else:
    ip_valida = ip.split('.')
    for octeto in ip_valida:
        num = int(octeto)
        if num >= 0:
            if num < 256:
                i+=1
                print(f'[-] octeto {num} correcto')
            else:
                print(f'[-] octeto {num} fuera de rango')

    if i == 4:
        print (f'[-] La Direccion IP es valida.')
    else:
        print (f'[-] La Direccion IP es no valida.')
  