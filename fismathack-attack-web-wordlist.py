#librerias necesarias
import requests
import time
from colorama import init,Fore 
import argparse 
#definiendo las opciones
parse = argparse.ArgumentParser(description="Libreria para descubrir rutas de una url de un sitio web.")
parse.add_argument("--wordlist","-w",help="Añade una lista de palabras.",required=True)
parse.add_argument("--url","-u",help="URL del sitio web.",required=True)
parse.add_argument("--verbose",help="Salida verbosa(opción para mostrar todas las respuestas de codigó de estado).")
parse.add_argument("--SaveFile","-SF",help="Guardar los resultados.")
parse.add_argument("--TimeSleep",help="Especificar un tiempo de espera en segundos(defecto: 0).",type=int)
args = parse.parse_args()
init()
wordlist = args.wordlist
url = args.url 
#realizando una solicitud web usando get
request_web = requests.get(url)
print(f"Status code({url}):{request_web.status_code}")
#contador
count = 0
#tiempo de espera por solicitud web 
time_sleep = 0
#creando archivo en caso de que args.SaveFile = True
if args.SaveFile:
  with open(args.SaveFile,"w") as savefile:
       pass
while True: 
   try:
     with open(wordlist,"r") as url_search:
          request_siteweb = url_search.readlines(0)
     request_web = requests.get(url + request_siteweb[count].replace("\n",""))
     show_siteurl = request_siteweb[count].replace("\n","")      
     #enviar solo las respuestas 200 
     if request_web.status_code == 200: 
        print(Fore.YELLOW)
        print(f"Status code -> {request_web.status_code}\nURL -> {url}{show_siteurl}")
     #salida verbosa   
     if args.verbose:
       print(f"Status code -> {request_web.status_code}\nURL -> {url}")
     #guardar salida y codigos de estado en 200  
     if args.SaveFile and request_web.status_code == 200:
       with open(args.SaveFile,"a") as savefile:
          savefile.write(f"\nStatus code -> {request_web.status_code}\nURL -> {url}{show_siteurl}\n")
     #guardar archivo y con salida verbosa    
     if args.SaveFile and args.verbose:
       with open(args.SaveFile,"a") as savefile:
           savefile.write(f"\nStatus code -> {request_web.status_code}\nURL -> {url}{show_siteurl}\n")    
      #tiempo de espera por solicitud     
     if args.TimeSleep:
       time_sleep = args.TimeSleep                 
     count += 1 
     time.sleep(time_sleep)
   except:
       print(Fore.GREEN + "=====================================================")
       break
