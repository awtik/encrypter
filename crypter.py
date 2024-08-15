import os
from cryptLib import Cipher

c = Cipher() # Initialization crypter class
os.system('cls') # Clear console
def cryption():
    """Function for crypt"""
    os.system('cls') # Clear console
    text = input('Insert text to encrypt:\n: ') # Get text for crypt
    text = text.encode() # Byting user's text
    os.system('cls') # Clear console
    key, encriptedText = c.encrypter(text) # Crypting text
    print(f'''Key to decrypt: {key}\nEncrypted text: {encriptedText}''') # Print result
    wait = input('\nSuccesful! You can copy this data!\nTo continue press Enter!')
    os.system('cls') # Clear console

def decryption():
    """Function for decrypt"""
    os.system('cls') # Clear console
    text = input('Insert text to decrypt:\n: ') # Get text for decrypt
    text = text.encode() # Byting user's text
    key = input('Insert key to decrypt:\n: ') # Get key for decrypt
    key = key.encode() # Byting user's text
    os.system('cls') # Clear console
    print(c.decrypter(key, text)) # Print result
    wait = input('\nSuccesful! You can copy this data!\nTo continue press Enter!')
    os.system('cls') # Clear console

def commands():
    """Function for showing commands list"""
    os.system('cls') # Clear console
    print("""             Command list
       crypt - Crypt your text
       decrypt - Decrypt your text with your cryption key
       exit - Close program
       help - Show this text\n""")

commands()
while(1):
    command = input('Insert command:\n: ') # Get command from user
    if command == 'crypt':
        cryption()
    elif command == 'decrypt':
        decryption()
    elif command == 'help':
        commands()
    elif command == 'exit':
        os.system('cls') # Clear console
        exit()