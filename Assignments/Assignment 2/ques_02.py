def prob(char,text):
    return(text.count(char)/len(text))

def caesar_decrypt(text,shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) - 65 - shift) % 26 + 65)
    return result

def caesar_stat_decrypt(text):
    strcharacters=("".join(set(text)))
    frequencies=[0.080,0.015,0.030,0.040,0.130,0.020,0.015,0.060,0.065,0.005,0.005,0.035,0.030,0.070,0.080,0.020,0.002,0.065,0.060,0.090,0.030,0.010,0.015,0.005,0.020,0.002]
    correlation= [0]*26
    for i in range(26):
     for j in strcharacters:
       c=ord(j) - 65
       p=prob(j,text)
       if(c-i <0):
        k=c-i+26
       else:
        k=c-i
       correlation[i]+= p*(frequencies[k])

    return (sorted(range(len(correlation)), key=lambda i: correlation[i])[-5:])

text = input("Please Enter Cipher Text:").replace(" ","")
top_shifts = caesar_stat_decrypt(text)
for x in top_shifts:
    print(caesar_decrypt(text,x))
