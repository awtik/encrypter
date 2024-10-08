import cryptography.fernet
Fernet = cryptography.fernet.Fernet

class Cipher:
    def __init__(self):
        pass
    def encrypter(self, text):
        """Method for encrypt"""
        cipher_key = Fernet.generate_key()
        cipher = Fernet(cipher_key)
        encrypted_text = cipher.encrypt(text)
        return cipher_key, encrypted_text
    def decrypter(self, key, text):
        """Method for decrypt"""
        cipher = Fernet(key)
        decrypted_text = cipher.decrypt(text)
        return decrypted_text