from tkinter import *
import os
window = Tk()
window.title("fismathack-tools")
window.geometry("700x500")
class FMHT:
 #función para limpiar todos los botones principales 
  def clear_home(self):
    button_scanner.pack_forget()
#función para llamar al scanner
  def scanner(self):
    self.input_gateway_scanner.pack_forget()
    self.input_mask_scanner.pack_forget()
    self.button_send_scanner.pack_forget()
    print(f"python fismathack-scanner.py --IP {self.varying_gateway_scanner} --SM {self.varying_mask_scanner}")
#función para llamar la configuración del scanner
  def scanner_settings(self):
    self.varying_gateway_scanner = StringVar()
    self.input_gateway_scanner = Entry(window,textvariable=self.varying_gateway_scanner)
    self.input_gateway_scanner.pack(pady=13)
    self.varying_mask_scanner = StringVar()
    self.input_mask_scanner = Entry(window,textvariable=self.varying_mask_scanner)
    self.input_mask_scanner.pack(pady=13)
    self.button_send_scanner = Button(window,text="Scanner",command=self.scanner)
    self.button_send_scanner.pack(pady=13)
fmht = FMHT()    
button_scanner = Button(window,text="Scanner",command=fmht.scanner_settings)
button_scanner.pack(pady=13)     
window.mainloop()
