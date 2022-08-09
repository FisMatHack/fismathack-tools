#!/bin/bash
#defino un cartel como inicio 
function banner {
   echo -e " \e[31m
=====================================================================================
______     |------                            _______                       ______                                 
|       |  |            /\      /\        /\     |      |      |     /\     |       |  /        
|-----  |  |______     /  \    /  \      /  \    |      |______|    /  \    |       | /          
|       |        |    /    \  /    \    /____\   |      |      |   /____\   |       | \          
|       |  ______|   /      \/      \  /      \  |      |      |  /      \  |_____  |  \  
                                                                       
=====================================================================================                                                                 
\e[0m   
   "
}
#creo la ayuda de la herramienta
function help_fismathack {
  echo -e "\nclear -> clear console\nbanner -> show banner\nattack-site-web -> attacks for sites web\nexit -> exit console fismathack\nbash -> open console bash \nnmap-scanner -> open the tool nmap"
}  

function attack_web_wordlist {
   #variables locales 
   #verificar que Python esta instalado
   if [ -e "/usr/bin/python" ]; then 
      echo "Starting process..."
      #opciones 
      local options="wordlist url verbose SaveFile TimeSleep"
      echo -n "to configure this it is necessary to enter the corresponding data, in case you do not want to add any command you can skip it with a no-add."
      echo -n "Path de fismathack-attack-web-wordlist:"
      read path_fismathack_attack_wordlist
      command_attack_web_wordlist="python $path_fismathack_attack_wordlist"
      #comenzando a leer, para establecer la configuración.
      for x in $options
      do 
        echo -n "$x >> "
        read configure_options 
        if [[ -n $configure_options && $configure_options != "no-add" ]]; then   
         command_attack_web_wordlist+="--$x $configure_options "
        fi
      echo -n "Command:\n$command_attack_web_wordlist"
      done 
      command $command_attack_web_wordlist 
   else    
      apt-get install python
      echo "python installed."
   fi    
   
}
#función para escanear con la herramienta nmap
function scanner_nmap {
  local options="scan-verbose(-sV) scan-system(-O)"
  select option in $options 
  do 
    if [ -e "/usr/bin/nmap" ]; then 
      if [ $option = "scan-verbose(-sV)" ]; then 
         echo -n "IP:"   
         read target_nmap 
         echo "Starting scan with nmap..."
         nmap -sV $target_nmap
      else 
         apt-get install nmap
      fi 
    fi    
  done 
}


#creo las utilidades en caso de seleccionar atacar sitio web 
function attack_siteweb {
   local options
   #opciones
   options="attack-web-wordlist clear back"
   select option in $options;
   do
     if [ $option = "attack-web-wordlist" ]; then 
       #llamando el ataque de diccionario 
       attack_web_wordlist 
     elif [ $option = "clear" ]; then 
        clear
     elif [ $option = "back" ]; then 
         home     
     fi  
   done
}

#llamando el cartel
banner
#función para mostrar la consola principal
function home {
while true
do 
  #leyendo la entrada
  echo -n "FisMatHack>>" 
  read  command_option 
  #ayuda
  if [ $command_option = "help" ]; then 
     help_fismathack;
  #cartel
  elif [ $command_option = "banner" ]; then 
      clear
      banner    
  #ataque web
  elif [ $command_option = "attack-site-web" ]; then 
      attack_siteweb     
  #limpiar consola
  elif [ $command_option = "clear" ]; then 
      clear   
  #salir 
  elif [ $command_option = "exit" ]; then
      break   
  elif [ $command_option = "bash" ]; then 
     echo "Bash open."
     bash    
  elif [ $command_option = "nmap-scanner" ]; then 
      scanner_nmap   
  fi
done
}
#llamando la función
home 
