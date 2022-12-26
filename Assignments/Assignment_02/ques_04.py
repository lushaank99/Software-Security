keynumber = 0
path = r"C:/Users/lusha/Downloads/"
def keyGenerate(string, key):
    global keynumber 
    keynumber+=1
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def decipher(string, text):
    length_key=0
    file = open(path+ text + ".txt", 'w')
    file.close()
    for i in range(26): 
      key = chr(i+65)
      key_string = keyGenerate(string, key)
      if(decipher_function(string, key, key_string, text) == 1):
                 return

    for i in range(26): 
      for j in range(26):
          key = chr(i+65)+ chr(j+65)
          key_string = keyGenerate(string, key)
          if(decipher_function(string, key, key_string, text) == 1):
                 return

    for i in range(26): 
      for j in range(26):          
          for k in range(26):
                key = chr(i+65) + chr(j+65) + chr(k+65)
                key_string = keyGenerate(string, key)
                if(decipher_function(string, key, key_string, text) == 1):
                    return
    return

def decipher_function(string, key, key_string, text):
    original_text = []
    file= open(path+ text + ".txt", 'a')
    for i in range(len(string)):
        x = (ord(string[i]) - ord(key_string[i]) + 26) % 26
        x += ord('A')
        original_text.append(chr(x))
    original_text = "" . join(original_text)
    if text == original_text:
        file.write("Shown below are the details: \n" + "Key Number: " + str(keynumber) + '\n' + ("Key : " + key +"\n" "Original Text: " + original_text +"\n"))
        file.close()
        return(1)
    file.write (("Key: " + key +", " "Original Text: "+ original_text +"\n"))
    file.close()
    return

ciphered_text=input("Please Enter The Ciphered Text:")
text = input("Please Enter The Plain Text:")
decipher(ciphered_text, text)
