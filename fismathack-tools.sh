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
  echo -e "\nclear -> clear console\nbanner -> show banner\nattack-site-web -> attacks for sites web\nexit -> exit console fismathack\nbash -> open console bash \nnmap-scanner -> open the tool nmap\nscanner -> Scan hosts connected to your network\ncryptography -> tools of cryptography\ntool-ping -> see which devices accept ICMP traces\nspoofer -> spoofear\nsniffer -> sniffer\nattack-ssh -> Perform attacks on devices that have ssh open"
}  

function attack_web_wordlist {
   #variables locales 
   #verificar que Python esta instalado
   if [ -e "/usr/bin/python" ]; then 
      echo "Starting process..."
      #opciones 
      local options="wordlist url verbose SaveFile TimeSleep"
      echo -n "to configure this it is necessary to enter the corresponding data, in case you do not want to add any command you can skip it with a no-add."
      echo ""
      command_attack_web_wordlist="python fismathack-attack-web-wordlist "
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
#=====================Criptografía comentario abierto===============================



#función para encriptar un texto 
function encrypt_text {
#leyendo entradas 
     echo -n "Text:"
     read text_encrypt
     echo -n "Password:"
     read password_encrypt 
     echo -n "Save Key(yes/no):"
     read save_key_question
     #guardar la clave 
     if [ $save_key_question = "yes" ]; then
         echo -n "Name of archive key:"
         read save_key_name 
         commands_cryptography+=" --EncryptText $text_encrypt --Password $password_encrypt --SaveKey $save_key_name"
     elif [ $save_key_question = "no" ]; then 
        commands_cryptography+=" --EncryptText $text_encrypt --Password $password_encrypt"
     fi
     
    #correr comando
     command $commands_cryptography

}
#función para encriptar un archivo
function encrypt_file {
#leyendo entradas
     echo -n "Path of file:"
     read file_encrypt
     echo -n "Password:"
     read password_encrypt 
     echo -n "Save copy(yes/no):"
     read save_copy_question 
     if [ $save_copy_question = "yes" ]; then 
        cp $file_encrypt $file_encrypt
        commands_cryptography+="--EncryptFile $file_encrypt --password $password_encrypt"
     elif [ $save_copy_question = "no" ]; then 
        commands_cryptography+="--EncryptFile $file_encrypt --password $password_encrypt"
     fi
     command $commands_cryptography  
}
function decrypt_text {
  local commands_decrypt_text = "python fismathack_cryptography "
  echo -n "Path of key:"
  read key_decrypt 
  echo -n "Password:"
  read password_decrypt 
  commands_decrypt_text += "--DecryptText $key_decrypt --Password $password_decrypt"
  command commands_decrypt_text
}
function decrypt_file {
  local commands_decrypt_file = "python fismathack_cryptography " 
  echo -n "Path of file:"
  read file_decrypt 
  echo -n "Password"
  read password_decrypt
  commands_decrypt_file += " --DecryptFile $file_decrypt --Password $password_decrypt"
  command commands_decrypt_file  
  
}



#función de criptografía
function cryptography {
local options="Encrypt-Text Encrypt-File Decrypt-Text Decrypt-File"
commands_cryptography="python fismathack_cryptography.py "
echo "not recommended"
select option in $options
do 
  #encriptación de texto
  if [ $option = "Encrypt-Text" ]; then 
     #llamando a la función
     encrypt_text
  #encriptación de archivo
  elif [ $option = "Encrypt-File" ]; then
     encrypt_file 
  elif [ $option = "Decrypt-Text" ]; then 
    decrypt_text
  elif [ $option = "Decrypt-File" ]; then 
     decrypt_file
  fi
done
}


#===================Criptografía comentario cerrado=================================


#ataque hacia cuenta de ssh
function attack_ssh {
command python fismathack-attack-ssh.py
}


function scanner {
   local commands_scanner="python fismathack-scanner.py "
   echo -n "IP(gateway):"
   read gateway
   echo -n "subnet mask(without /):"
   read subnet_mask
   commands_scanner+="--IP $gateway --SM $subnet_mask"
   command $commands_scanner
}
#Función para enviar trazas ICMP hacia el rango de la dirección IP dentro de la Area Local(LAN)
function ping_range {
echo -n "IP to relizar trace ICMP(example:192.168.1):"
read IP_scan 
echo -n "first range(example:1):"
read range1
echo -n "two range(example:255):"
read range2
for i in $(seq $range1 $range2)
do
 timeout 1 bash -c "ping -c 1 $IP_scan.$i" &>/dev/null && echo "[+] Host $IP_scan.$i - ACTIVE" &

done
wait
}

function spoofer {
  local commands_spoofer="python fismathack-arp_spoofer.py "
  echo -n "IP to poisin:"
  read IP_victim 
  echo -n "IP of gateway:"
  read IP_gateway
  commands_spoofer+="--IP $IP_victim --Gateway $IP_gateway"
  command $commands_spoofer
}
function sniffer {
  local commands_sniffer="python fismathack-sniffer.py "
  echo -n "interface to monitor:"
  read interface 
  commands_sniffer+="--Interface $interface"
 
  command $commands_sniffer
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
  #abrir bash
  elif [ $command_option = "bash" ]; then 
     echo "Bash open."
     bash    
  elif [ $command_option = "scanner" ]; then
      scanner    
  elif [ $command_option = "attack-ssh" ];then
      attack_ssh
  elif [ $command_option = "cryptography" ]; then 
      cryptography     
  elif [ $command_option = "tool-ping" ]; then
      ping_range    
  elif [ $command_option = "spoofer" ]; then 
      spoofer
  elif [ $command_option = "sniffer" ]; then 
      sniffer        
  fi
done
}
#llamando la función
home 
