alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
plain_text = 'meetmeatnight'.upper()
keyword = 'hello'.upper()
class VigenereCipher:
    def generateKey(self, string, key):
        if len(plain_text) == len(key):
            return key
        else:
            for i in range(len(plain_text) - len(key)):
                key += key[i % len(key)]
        return key

    def encrypt(self, string, key):
        result = ''
        for i in range(len(string)):
            # x = (ord(string[i]) + ord(key[i])) % 26
            # x += ord('A')
            result += chr(((ord(string[i]) + ord(key[i])) % 26) + ord('A'))
        return result

    def decrypt(self, string, key):
        result = ''
        for i in range(len(string)):
            x = (ord(string[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            result += chr(x)
        return result

# crypto = VigenereCipher()
# key = crypto.generateKey(plain_text, keyword)
# print(key)
# cipher_text = crypto.encrypt(plain_text, key)
# print(cipher_text)
# plaintext = crypto.decrypt(cipher_text, key)
# print(plaintext)
