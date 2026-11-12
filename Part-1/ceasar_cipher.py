class Caesar:
    def encrypt(self, text, key):
        result = ""
        for c in text:
            if c.isalpha():
                result += chr((ord(c.upper())-ord('A')+key)%26 + ord('A'))
            else:
                result += c
        return result
    
    def decrypt(self, text, key):
        return self.encrypt(text, -key)

text = input("Enter text: ")
key = int(input("Enter key: "))

obj = Caesar()

encrypted = obj.encrypt(text, key)
decrypted = obj.decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)