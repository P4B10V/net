## NET ##

import argparse
import random
import socket
from scapy.all import ARP, Ether, IP, ICMP, TCP, srp, sr1


parser = argparse.ArgumentParser(prog='~ SNIFFER ~',
                               description='Proyecto personal para crear un sniffer con Python/Scapy')


#store_true hace que la opción sea booleana, es decir, si se usa == True, y si no == False
parser.add_argument('-s', '--scan', action='store_true', help='Escanear la red en busca de dispositivos activos')
parser.add_argument('-r', '--range', type=str, help='Rango en el que se realizará el escaneo')
parser.add_argument('-i', '--icmp', action='store_true', help='Enviar un paquete ICMP')
parser.add_argument('-t', '--target', type=str, help='Target para enviar el paquete ICMP')
parser.add_argument('-p', '--port', type=int, help='Especificar el puerto')
parser.add_argument('-S', '--service', action='store_true', help='Analizar servicios de un host')

args = parser.parse_args()


#Lo primero que quiero hacer es un escaneo de mi red para ver que dispositivos están activos, por lo que la primera funcionalidad
#será hacer un escaneo de red. La opción elegida será enviar un ARP y ver que respuestas tengo.
def escaneo():

        arp = ARP(op=1, pdst=red) #op=1 == who-has, op=2 == it-at
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        paquete = ether / arp

        dispositivos = []

        escaneo_red = srp(paquete,verbose=0,timeout=1)[0]
        for enviado, recibido in escaneo_red:
                dispositivos.append(recibido.psrc)
        print(f'{dispositivos} Dispositivos encontrados en la red.')

def icmp():

        ip = IP(dst=objetivo)
        paquete = ip / ICMP()
        print(f'Enviando ping a {objetivo}')
        respuesta = sr1(paquete, timeout=2,verbose=0)

        if respuesta is None:
                print(f'{objetivo} no está en la red.')
                return

        if respuesta[0]:
                print(f'Respuesta de {objetivo} ')

def service():

  
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((objetivo, PORT))

        conexion = client.recv(1024)
        conexion = conexion.decode()

        print(f'En el puerto {PORT} se detecto: {conexion}')



if args.scan:
        if args.range:
                red = args.range
                escaneo()
        else:
                print('Falta argumento -r, --range para escanear la red.')
elif args.icmp:
        if args.target:
                objetivo = args.target
                icmp()
        else:
                print('Falta argumento -t, --target para enviar ICMP.')
elif args.service:
        if args.port:
                PORT = args.port
                if args.target:
                        objetivo = args.target
                        service()
                else:
                        print('Necesitas ingresar una ip: -t --target')
        else:
                print('Necesitas ingresar puerto -p --port y un objetivo -t --target')

else:
        parser.print_help()


## verbose=0 -> es necesario para que no ensucie la salida de la consola.
## timeout=n -> donde n son los segundos que esperará para parar.


                                                                     



                                
