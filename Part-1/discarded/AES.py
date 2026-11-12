class AES:
    def xor(self,a,b):
        return bytes(x^y for x,y in zip(a,b))

    def aes(self,text,key):
        key = key.encode()

        if len(key) not in [16,24,32]:
            raise ValueError("Key length is neither 16,24 nor 32")

        result = b""

        for i in range(0,len(text),8):

            block = text[i:i+16].encode().ljust(16,b" ")
            state = self.xor(block,key)
            rounds = {16:10,24:12,32:14}[len(key)]

            for r in range(rounds):

                state = bytes((x*7+r)%256 for x in state)

                state = (
                    state[0:4] +
                    state[5:8] + state[4:5] +
                    state[9:12] + state[8:9] +
                    state[13:16] + state[12:13]
                )

                round_key = bytes(key[(j+r)%len(key)] for j in range(16))

                state = self.xor(state,round_key)

            result += state

        return result.hex()

plaintext = "Saketh"
key = "1234567890123456"
aes_obj = AES()

print("Plaintext :", plaintext)
print("Key       :", key)
print("Encrypted :", aes_obj.aes(plaintext, key))