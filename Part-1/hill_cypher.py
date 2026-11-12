import numpy as np

class hillcipher:
    def __init__(self,key):
        self.key = np.array(key)
        self.MOD = 26
        self.inverted_key = self.invert_matrix(self.key)

    def text_to_numbers(self,text):
        return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

    def numbers_to_text(self,nums):
        return "".join(chr(int(n)+ord('A')) for n in nums)

    def invert_matrix(self,matrix):
        det = round(np.linalg.det(matrix))

        try:
            inverse_det = pow(det%self.MOD,-1,self.MOD)
        except:
            raise ValueError("The key is invalid, so the hillcipher cannot be performed")
        
        adj = (det*np.linalg.inv(matrix)).astype(int)

        return (inverse_det*adj) % self.MOD

    def _process(self,text,matrix):
        nums = self.text_to_numbers(text)
        n = len(self.key)

        nums.extend([ord('X')-ord('A')] * (-len(nums)%n))
        processed = (np.array(nums).reshape(-1,n) @ matrix.T) % self.MOD

        return self.numbers_to_text(processed.flatten())

    def encrypt(self,text):
        return self._process(text,self.key)

    def decrypt(self,text):
        return self._process(text,self.inverted_key)

key = [
    [1,2,3,4],
    [0,1,2,3],
    [0,0,1,2],
    [1,0,0,1]
]
hillcipher_obj = hillcipher(key)
text = input("Enter the text: ")
encrypted = hillcipher_obj.encrypt(text)
decrypted = hillcipher_obj.decrypt(encrypted)

print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted}")
print(f"Decrypted Text: {decrypted}")