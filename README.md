# fismathack-tools
a store with different codes dedicated to hacking

La herramienta cuenta con más herramientas en las cuáles puedes realizar ataques web,realizar escaneos(utilizó nmap) y probablemente más adelante saque más!.
añado scripts por lo menos una vez a la semana.

<h1>DETALLES SOBRE fismathack-tools y como configurar</h1>

cd fismathack-tools

al usted haber clonado el repositorio tendrá algunos archivos.

puede ejecutar directamente algunas de las herramientas que ofresco o puede ver más utilidades en el archivo fismathack-tools.sh.

para evitar problemas con acceso de superusuario recomiendo realizar:

sudo su

Otorgemosle permisos de ejecución al archivo principal, esto se hace con:

chmod +x fismathack-tools.sh

<h1>EJECUCIÓN DE fismathack-tools</h1> 

para ejecutar hacemos:

./fismathack-tools.sh

veremos una consola el cuál dice FisMatHack.

al colocar el comando "help" obtendremos comando con su respectiva ayuda.

seleccionemos:
attack-site-web

al seleccionar attack-site-web se nos desplego un menu en el cuál nos brinda 3 opciones 
1) attack-web-wordlist
2) clear
3) back 

seleccionamos 1 

después de seleccionar la opción uno nos pedira un archivo para comenzar a buscar el cuál puedes especificar la ruta del archivo que deja un mensaje "Path of fismathack-attack-web-wordlist:" 
en este caso ese archivo lo tengo situado en /home/fismathack/Escritorio/fismathack-tools/fismathack-attack-web-wordlist.py.

después nos pide un wordlist el cuál yo indique esté
/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt

ULR:https://example.com/ 
or
URL:http://example.com/

nos pide si será una salida verbosa, en caso de querer una salida verbosa dar cualquier palabra sin espacios o un simple número.

en penultimo lugar nos pide si será guardado en un archivo, en este caso colocare output.txt.

en ultimo lugar nos pide un tiempo de espera por cada solicitud.
las consecuencias de dejarlo en cero es que hara mucho ruido

