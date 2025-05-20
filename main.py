## SNIFFER ##

import argparse
from scapy.all import ARP, Ether, IP, ICMP, srp, sr1



parser = argparse.ArgumentParser(prog='~ SNIFFER ~',
                               description='Proyecto personal para crear un sniffer con Python/Scapy')


#store_true hace que la opción sea booleana, es decir, si se usa == True, y si no == False
parser.add_argument('-s', '--scan', action='store_true', help='Escanear la red en busca de dispositivos activos')
parser.add_argument('-r', '--range', type=str, help='Rango en el que se realizará el escaneo')
parser.add_argument('-p', '--ping', action='store_true', help='Enviar un paquete ICMP')
parser.add_argument('-t', '--target', type=str, help='Target para enviar el paquete ICMP')

args = parser.parse_args()


#Lo primero que quiero hacer es un escaneo de mi red para ver que dispositivos están activos, por lo que la primera funcionalidad
#será hacer un escaneo de red. La opción elegida será enviar un ARP y ver que respuestas tengo.
def escaneo():

        arp = ARP(op=1, pdst=red) #op=1 == who-has, op=2 == it-at
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        paquete = ether / arp

        dispositivos = []

        escaneo_red = srp(paquete,verbose=0,timeout=5)[0]

        for enviado, recibido in escaneo_red:
                dispositivos.append(recibido.psrc)

        print(f'{dispositivos} Dispositivos encontrados en la red.')

def ping():

        ip = IP(dst=objetivo)
        paquete = ip / ICMP()
        print(f'Enviando ping a {objetivo}')
        respuesta = sr1(paquete)

        if respuesta[0]:
                print(f'Respuesta de {objetivo} ')
        else:
                print(f'{objetivo} no responde.') #NO FUNCIONA SI HAGO PING A UNA DIRECCIÓN QUE NO EXISTE

if args.scan:
        if args.range:
                red = args.range
                escaneo()
        else:
                print('Falta argumento -r, --range para escanear la red.')
elif args.ping:
        if args.target:
                objetivo = args.target
                ping()
        else:
                print('Falta argumento -t, --target para enviar ICMP.')
else:
        parser.print_help()
                                
