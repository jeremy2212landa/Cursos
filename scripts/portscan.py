#usr/bin/python3

import socket
import sys

ip_addr = '127.0.0.1'
portList = (21,22,23,25,53,59,79,80,110,110,113,135,139,143,443,445,1080,3306,3389,5000,5432,8000,8080)
for port in portList:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"Puerto: {port} - OPEN")
        else:
            print(f"Puerto: {port} - CLOSED")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")    
        sys.exit()

        