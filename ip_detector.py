import re

ip = str(input('Escriba una direccion ip: '))

ipmatch = re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ip) 			# IP ADDRESS REGULAR EXPRESSION.

if not ipmatch:
	print(f"La IP = {ip} Colocada no tiene un formato correcto.")
else:
    print(f"La IP = {ip} Colocada es correcta.")