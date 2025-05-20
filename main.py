## SNIFFER ##

import argparse
from scapy.all import ARP, Ether, srp

parser = argparse.ArgumentParser(prog='~ SNIFFER ~',
                               description='Proyecto personal para crear un sniffer con Python/Scapy')

parser.add_argument('-s', '--scan', action='store_true', help='Escanear la red en busca de dispositivos activos')
        #store_true hace que la opción sea booleana, es decir, si se usa == True, y si no == False

args = parser.parse_args()

#Lo primero que quiero hacer es un escaneo de mi red para ver que dispositivos están activos, por lo que la primera funcionalidad
#será hacer un escaneo de red. La opción elegida será enviar un ARP y ver que respuestas tengo.
def escaneo():

        arp = ARP(op=1, pdst="10.22.0.0/16") #op=1 == who-has, op=2 == is-at
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        paquete = ether / arp
#La información que contiene paquete, si lo utilizamos con Scapy, podemos verla con paquete[0].show() y paquete[1].show()
# [0] es la capa de Ethernet y [1] la capa ARP
  
        dispositivos = []

        escaneo_red = srp(paquete,verbose=0,timeout=5)[0]
        for enviado, recibido in escaneo_red:
                dispositivos.append(recibido.psrc)

        print(f'{dispositivos} Dispositivos encontrados en la red.')


if args.scan:
        escaneo()
else:
        print("Necesitas especificar -s para escanear")

