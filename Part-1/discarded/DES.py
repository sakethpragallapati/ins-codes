class DES:
    def xor(self,a,b):
        return "".join(str(int(x)^int(y)) for x,y in zip(a,b))

    def F(self,right,key):
        x = self.xor(right+right[:16],key)
        return "".join(format(int(x[i:i+6],2),"04b") for i in range(0,48,6))

    def des(self, text, key):
        key = (key * 48)[:6]
        key = "".join(format(ord(c), "08b") for c in key)

        result = ""

        for i in range(0, len(text), 8):
            block = text[i:i+8].ljust(8, " ")
            block = "".join(format(ord(c), "08b") for c in block)

            L, R = block[:32], block[32:]

            for j in range(16):
                L, R = R, self.xor(L, self.F(R, key))

            result += R + L

        return result

    def binary_to_text(self,bits):
        return "".join(chr(int(bits[i:i+8],2)) for i in range(0,len(bits),8))

plain_text = "Saketh"
key = "asxsc"
des_obj = DES()

cipher = des_obj.des(plain_text,key)

print(f"Plain Text: {plain_text}")
print(f"Encrypted: {cipher}")
print(f"Result: {des_obj.binary_to_text(cipher)}")