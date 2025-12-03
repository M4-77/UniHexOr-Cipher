# basically an xor cipher that converts the string into its unicode value before applying the xor cipher and it finishes in hexadecimal, leaving it looking neat and compact i guess

# the entire code is just a really fancy version of this xor cipher

# text = 'A'.encode()   where 'A' becomes 65
# key = 'B'.encode()    and 'B' becomes 66
# print(text[0] ^ key[0])  which is basically just XOR 65 ^ 66

# above is a single letter XOR encryption, this is just that with added iteration so it can do whole strings and a hexadecimal output
# oh yeah we also have random key gen so thats nice i guess

# credits to this guy for teaching me how to do it https://www.youtube.com/watch?v=P8Mc2DtxHq0

import random

def xor_bytes(data_bytes, key_bytes): # i couldve done it individually but i saw someone on stackoverflow use a function for it, decided why not as it looks clean
    return bytes([data_bytes[i] ^ key_bytes[i] for i in range(len(data_bytes))])

def main():
    mode = input("E to encrypt and D to decrypt").strip().upper()
    if mode == 'E':
        text = input("enter a message to encrypt: ").encode('utf-8')
        textlength = len(text)
        key_choice = input("do you want to provide a key? must match message length, if you say no then one will be provided for you. (Y/N): ").strip().upper()
        if key_choice == 'Y':
            key_hex = input("paste your key in hex: ")
            key = bytes.fromhex(key_hex)
            if len(key) != len(text):
                print("error: key length must match message length.")
                return
        else:
            key = bytes([random.randint(0, 255) for _ in range(textlength)])
            print("generated key (hex):", key.hex())
        cipher = xor_bytes(text, key)
        print("cipher (hex):", cipher.hex())
    elif mode == 'D':
        cipher_hex = input("enter cipher in hex: ")
        key_hex = input("enter key in hex: ")
        cipher = bytes.fromhex(cipher_hex)
        key = bytes.fromhex(key_hex)
        if len(cipher) != len(key):
            print("error: cipher length and key length must match.")
            return
        decrypted_bytes = xor_bytes(cipher, key)
        try:
            decrypted_text = decrypted_bytes.decode('utf-8')
            print("decrypted message:", decrypted_text)
        except UnicodeDecodeError:
            print("decrypted bytes (could not decode to UTF-8 probably because it was an invalid input you are so good at this wow):", decrypted_bytes) # i dont really know how you would get this error but i saw it on stackoverflow and stuff so i made this just in case
    else:
        print("Invalid choice. Literally can't make it any clearer. Either type in E or D its not that hard.")

if __name__ == "__main__":
    main()
