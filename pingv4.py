import sys
from scapy.all import *
import time
import random

# Obtener el mensaje desde la consola
if len(sys.argv) != 2:
    print("Uso: python enviar_paquetes.py <mensaje>")
    sys.exit(1)

mensaje = sys.argv[1]

# Crear una lista de paquetes ICMP
paquetes = []
for caracter in mensaje:
    # Convierte el caracter en su representación hexadecimal
    hex_caracter = hex(ord(caracter))[2:]
    
    # Construir el mensaje ICMP con el caracter en lugar de ??
    mensaje_icmp = bytes.fromhex(f"{hex_caracter} fc 01 00 00 00 00 00 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37")
    
    # Crear el paquete ICMP
    paquete_icmp = IP(dst="127.0.0.1") / ICMP() / mensaje_icmp
    
    # Agregar el paquete a la lista
    paquetes.append(paquete_icmp)

# Enviar los paquetes uno por uno
for idx, paquete in enumerate(paquetes, start=1):
    print(f"Enviando paquete {idx}: {paquete.summary()}")
    send(paquete)
    time.sleep(random.randint(1, 4))
