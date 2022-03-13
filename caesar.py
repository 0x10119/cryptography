# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#
# def encrypt(current, key):
#     return (current + key) % 26
#
# def decrypt(current, key):
#     return (current - key) % 26
#
# plaintext = input("Please input plaintext: ")
# key = int(input("Input key: "))
#
# cipher_text = []
# for i in plaintext:
#     curr = alphabet.index(i)
#     # print(curr)
#     new_position = encrypt(curr, key)
#     cipher_text.append(alphabet[new_position])
#
# print(f"Ciphertext is {''.join(cipher_text)}")
#
# plain_text = []
# for j in cipher_text:
#     curr = alphabet.index(j)
#     new_position = decrypt(curr, key)
#     plain_text.append(alphabet[new_position])
#
# print(f"Plaintext is {''.join(plain_text)}")
class CaesarCipher:
    def encrypt(self, string, key):
        result = ''
        for char in string:
            if char == " ":
                result += " "
                continue
            if ord(char) > 96:
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += chr((ord(char) + key - 65) % 26 + 65)
        return result

    def decrypt(self, string, key):
        result = ''
        for char in string:
            if char == " ":
                result += " "
                continue
            if ord(char) > 96:
                result += chr((ord(char) - key - 97) % 26 + 97)
            else:
                result += chr((ord(char) - key - 65) % 26 + 65)
        return result

# plain_text = "hello"
# key = 3
# cipher_text = CaesarCipher.encrypt(plain_text, key)
# print(cipher_text)

