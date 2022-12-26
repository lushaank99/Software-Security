def keyGenerate(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 94
        x += 33
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

text = input("Please Enter Plain Text:")
keyword = input("Please Enter Keyword:")
key = keyGenerate(text, keyword)
cipher_text = cipherText(text,key)
print("Vigenere Ciphered Text is", cipher_text)