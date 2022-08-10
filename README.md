# fismathack-tools
a store with different codes dedicated to hacking

La herramienta cuenta con más herramientas en las cuáles puedes realizar ataques web,realizar escaneos(utilizó nmap) y probablemente más adelante saque más!.
añado scripts por lo menos una vez a la semana.

<h1>Detalles sobre fismathack-tools y como configurar</h1>

cd fismathack-tools

Al usted haber clonado el repositorio tendrá algunos archivos.

Puede ejecutar directamente algunas de las herramientas que ofrezco o puede ver más utilidades en el archivo fismathack-tools.sh.

Para evitar problemas con acceso de superusuario recomiendo realizar:

sudo su

Otorgemosle permisos de ejecución al archivo principal, esto se hace con:

chmod +x fismathack-tools.sh

<h1>Ejecución de fismathack-tools mediante el archivo ./fismathack-tools.sh(GNU/LINUX)</h1> 

para ejecutar hacemos:

./fismathack-tools.sh

Veremos una consola el cuál dice FisMatHack.

Al colocar el comando "help" obtendremos comando con su respectiva ayuda.

seleccionemos:
attack-site-web

Al seleccionar attack-site-web se nos desplego un menu en el cuál nos brinda 3 opciones 
1) attack-web-wordlist
2) clear
3) back 

Seleccionamos 1. 

Después de seleccionar la opción uno nos pedira un archivo para comenzar a buscar el cuál puedes especificar la ruta del archivo que deja un mensaje "Path of fismathack-attack-web-wordlist:" 
En este caso ese archivo lo tengo situado en /home/fismathack/Escritorio/fismathack-tools/fismathack-attack-web-wordlist.py.

Después nos pide un wordlist el cuál yo indique esté: /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt

Después nos pide la URL del sitio web.
ULR:https://example.com/ 
or
URL:http://example.com/

Nos pide si será una salida verbosa, en caso de querer una salida verbosa dar cualquier palabra sin espacios o un simple número.

En penultimo lugar nos pide si será guardado en un archivo, en este caso colocare output.txt.

En ultimo lugar nos pide un tiempo de espera por cada solicitud.
Las consecuencias de dejarlo en cero es que hara mucho ruido.

Lo siguiente esta en proceso...

<h1>Ejecución de fismathack-tools mediante el archivo EXE(Windows)</h1>

El archivo EXE no viene instalado por defecto por lo que lo puedes descargar desde: 


<h1>Ejecución de fismathack-tools mediante el código fuente</h1>

En caso de que cuentes con una Mac OS u otro sistema operativo, puedes descargar el código fuente de la GUI desde:

La configuración y proceso es casi identico a "Ejecución de fismathack-tools mediante el archivo EXE(Windows)".

Al tener el código instalado tienes que ejecutar el archivo.

fismathack-tools-GUI-code 

python fismathack-tools-GUI-code

