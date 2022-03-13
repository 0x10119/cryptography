from caesar import CaesarCipher
from vigenere import VigenereCipher

if __name__ == '__main__':
    should_continue = True
    while should_continue:
        choice = input("Caesar or Vigenere? Type 'c' or 'v' or 'y' to exit ")
        if choice == "y":
            should_continue = False
        if choice == "c":
            user_input = input("Input your message: ")
            key = int(input("Key: "))
            crypto = CaesarCipher()
            cipher_text = crypto.encrypt(user_input, key)
            plain_text = crypto.decrypt(cipher_text, key)
            print(f"Cipher text is {cipher_text}")
            print(f"Plain text is {plain_text}")
        elif choice == "v":
            user_input = input("Input your message: ").upper()
            keyword = input("Keyword: ").upper()
            crypto = VigenereCipher()
            key = crypto.generateKey(user_input, keyword)
            cipher_text = crypto.encrypt(user_input, key)
            plain_text = crypto.decrypt(cipher_text, key)
            print(f"Cipher text is {cipher_text}")
            print(f"Plain text is {plain_text}")

