import os
from cryptLib import Cipher

c = Cipher()
def cryption():
    os.system('cls')
    text = input('Insert text to encrypt:\n: ')
    text = text.encode()
    os.system('cls')
    key, encriptedText = c.encrypter(text)
    print(f'''Key to decrypt: {key}\nEncrypted text: {encriptedText}''')
    wait = input('\nSuccesful! You can copy this data!\nTo continue press Enter!')
def decryption():
    os.system('cls')
    text = input('Insert text to decrypt:\n: ')
    text = text.encode()
    key = input('Insert key to decrypt:\n: ')
    key = key.encode()
    os.system('cls')
    print(c.decrypter(key, text))
    wait = input('\nSuccesful! You can copy this data!\nTo continue press Enter!')
while(1):
    os.system('cls')
    command = input('Insert command:\n: ')
    if command == 'crypt':
        cryption()
    elif command == 'decrypt':
        decryption()
    elif command == 'exit':
        exit()