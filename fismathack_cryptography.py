#importar los modulos necesarios\
import argparse
import cryptocode
from colorama import init,Fore 
init()
#añadiendo los comandos
parse = argparse.ArgumentParser()
parse.add_argument("--EncryptText","-ET",help="Encrypt text")
parse.add_argument("--EncryptFile","-EF",help="Encrypt file")
parse.add_argument("--DecryptText","-DT",help="Decrypt text")
parse.add_argument("--DecryptFile","-DF",help="Desencrypt file")
parse.add_argument("--SaveKey",help="Save the key(example:key.key)")
parse.add_argument("--Password","-P",help="Password")
args = parse.parse_args()
class Cryptography: 
   def EncryptText(self,text,password,save_key):
     text_encrypt = cryptocode.encrypt(text,password)     
     print("\nText:",text,"\nEncrypted:",text_encrypt,"\nPassword:",password)
     with open(save_key,"w") as key:
        key.write(text_encrypt)
   def DecryptText(self,key_file,password):
       with open(key_file,"r") as key_read:     
         print(cryptocode.decrypt(key_read.read(),password))
   def EncryptFile(self,filename,password):
     #Leyendo el archivo para encriptar el texto que esta dentro
     with open(filename,"r") as filename_read:
        file_read = filename_read.read()   
    #encriptando
     file_encrypt = cryptocode.encrypt(file_read,password)
     #Escribiendo el key de encriptaciòn
     with open(filename,"w") as file_write:
         file_write.write(file_encrypt)
     print(Fore.BLUE + "Encryption!")    
   def DecryptFile(self,filename,password):
     #Leyendo el archivo
     with open(filename,"r") as filename_read:
        file_read = filename_read.read()
      #desencriptando  
     file_decrypt = cryptocode.decrypt(file_read,password)
     #Escribiendo el contenido real
     with open(filename,"w") as file_write:
        file_write.write(file_decrypt)
     print(Fore.BLUE + "Decrypted")      
cryptography = Cryptography()
try:
  if args.EncryptText and args.Password and args.SaveKey:
     cryptography.EncryptText(args.EncryptText,args.Password,args.SaveKey)   
          
  if args.DecryptText and args.Password:
      cryptography.DecryptText(args.DecryptText,args.Password)
     
  if args.EncryptFile and args.Password:
     cryptography.EncryptFile(args.EncryptFile,args.Password)
        
  if args.DecryptFile and args.Password:
     cryptography.DecryptFile(args.DecryptFile,args.Password)
except:
    print("Error of options.")
