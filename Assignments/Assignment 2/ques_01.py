def caesar_encrypt(text,shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char)-65) % 26 + shift + 65)
    return result


text = input("Please Enter Plain Text:")
shift = int(input("Please Enter Key Value:"))

print ("Plain Text is : " + text)
print ("Shift pattern is : " + str(shift))
print ("Caesar Cipher is : " + caesar_encrypt(text,shift))