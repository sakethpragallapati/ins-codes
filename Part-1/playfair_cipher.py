import matplotlib.pyplot as plt
import numpy as np

class playfaircipher:
    def __init__(self,key):
        self.key = key
        self.matrix = self.generate_matrix(self.key)

    def generate_matrix(self,key):
        seen_set = []
        global_text = key+'abcdefghijklmnopqrstuvwxyz'
        pointer = 0
        matrix = []
        for i in range(5):
            row = []
            j = 0
            while j < 5:
                if(pointer>=len(global_text)):
                    break
                c = global_text[pointer]
                if c == 'j':
                    c = 'i'
                if c not in seen_set:
                    row.append(c)
                    seen_set.append(c)
                else:
                    j -= 1
                j += 1
                pointer += 1
            matrix.append(row)
        return matrix

    def find_index(self,letter):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == letter:
                    return (i,j)

    def encrypt(self,text):
        pair_matrix = []
        pointer = 0
        result = ""
        while pointer < len(text):
            if pointer == len(text)-1:
                pair_matrix.append([text[pointer],'x'])
                break

            first_letter = text[pointer]
            second_letter = text[pointer+1]

            if first_letter == second_letter:
                pair_matrix.append([first_letter,'x'])
                pointer += 1
            else:
                pair_matrix.append([first_letter,second_letter])
                pointer += 2

        for pair in pair_matrix:
            first_letter_index = self.find_index(pair[0])
            second_letter_index = self.find_index(pair[1])
            
            if first_letter_index[0] == second_letter_index[0]:
                result += (self.matrix[first_letter_index[0]][(first_letter_index[1]+1)%5]+self.matrix[second_letter_index[0]][(second_letter_index[1]+1)%5])
            elif first_letter_index[1] == second_letter_index[1]:
                result += (self.matrix[(first_letter_index[0]+1)%5][first_letter_index[1]]+self.matrix[(second_letter_index[0]+1)%5][second_letter_index[1]])
            else:
                result += self.matrix[first_letter_index[0]][second_letter_index[1]]
                result += self.matrix[second_letter_index[0]][first_letter_index[1]]

        return result

    def decrypt(self,text):
        pointer = 0
        result = ""
        while pointer<len(text):
            first_letter = text[pointer]
            second_letter = text[pointer+1]

            first_letter_index = self.find_index(first_letter)
            second_letter_index = self.find_index(second_letter)

            if first_letter_index[0] == second_letter_index[0]:
                result += (self.matrix[first_letter_index[0]][(first_letter_index[1]-1)%5]+self.matrix[second_letter_index[0]][(second_letter_index[1]-1)%5])
            elif first_letter_index[1] == second_letter_index[1]:
                result += (self.matrix[(first_letter_index[0]-1)%5][first_letter_index[1]]+self.matrix[(second_letter_index[0]-1)%5][second_letter_index[1]])
            else:
                result += self.matrix[first_letter_index[0]][second_letter_index[1]]
                result += self.matrix[second_letter_index[0]][first_letter_index[1]]

            pointer += 2

        return result

class graphclass:
    def draw_bar_graph(self,x,y1,y2):
        x_temp = np.arange(len(x))
        w = 0.35

        plt.bar(x_temp-w/2,y1,w,label='Plain Text')
        plt.bar(x_temp+w/2,y2,w,label='Cipher Text')

        plt.title("Play-Fair Cipher Comparision")
        plt.xticks(x_temp,x)
        plt.xlabel("Words")
        plt.ylabel("Length (bytes)")
        plt.legend()
        plt.show()

keys = ["qwertyuiop","asdfg","zxcvbnm"]
plain_texts = ["saketh","anand","prathik"]
cipher_texts = []
for i in range(3):
    
    playfaircipher_object = playfaircipher(keys[i])

    encrypted_text = playfaircipher_object.encrypt(plain_texts[i])
    decrypted_text = playfaircipher_object.decrypt(encrypted_text)
    print(f"Original text: {plain_texts[i]}")
    print(f"Encrypted text: {encrypted_text}")
    print(f"Original text: {decrypted_text} \n")
    cipher_texts.append(encrypted_text)

graphclass_object = graphclass()
graphclass_object.draw_bar_graph(plain_texts,[len(text) for text in plain_texts],[len(text) for text in cipher_texts])