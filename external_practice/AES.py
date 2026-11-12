from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import secrets
import os
import matplotlib.pyplot as plt
import numpy as np

class filemodule:
    def __init__(self,folder_name):
        self.folder_name = folder_name
        self.file_names = os.listdir(self.folder_name)

    def extract_texts(self):
        text_contents = []
        for filename in self.file_names:
            file_path = os.path.join(self.folder_name,filename)
        
            with open(file_path,"r") as file:
                text = file.read()
                text_contents.append(text)
        return text_contents

class aes:
    def __init__(self,key):
        self.key = key
        self.cipher = AES.new(key,AES.MODE_ECB)

    def encrypt(self,texts):
        encrypted_texts = []
        for text in texts:
            encrypted_text = self.cipher.encrypt(pad(text.encode('utf-8'),16))
            encrypted_texts.append(encrypted_text)
        return encrypted_texts

    def decrypt(self,encrypted_texts):
        texts = []
        for encrypted_text in encrypted_texts:
            text = unpad(self.cipher.decrypt(encrypted_text),16)
            texts.append(text.decode('utf-8'))
        return texts

class graphclass:
    def draw_bar_graph(self,filenames,y1,y2):
        x = np.arange(len(filenames))
        w = 0.35

        plt.bar(x-w/2, y1, w, label="Plaintext")
        plt.bar(x+w/2, y2, w, label="Ciphertext")

        plt.xticks(x, filenames)
        plt.xlabel("File names")
        plt.ylabel("Length (bytes)")
        plt.legend()
        plt.show()

key = secrets.token_bytes(16)
file_path = "textfiles_folder"

aes_object = aes(key)
filemodule_object = filemodule(file_path)
graph_obj = graphclass()

file_texts = filemodule_object.extract_texts()
encrypted_texts = aes_object.encrypt(file_texts)
decrypted_texts = aes_object.decrypt(encrypted_texts)

print("Encrypted Texts:")
for encrypted_text in encrypted_texts:
    print(f"{encrypted_text.hex()} \n")

print(f"Is Original equal to decrypted? : {file_texts == decrypted_texts}")

graph_obj.draw_bar_graph(filemodule_object.file_names,[len(text) for text in file_texts],[len(encrypted_text) for encrypted_text in encrypted_texts])