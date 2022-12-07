f=open("abc.txt","w")
f.write("abcd\n")
f.write("ABCDEF\n")
f.write("0123456789\n")
f.write("india is an asian country\n")
f.close()

f1=open("pqr.txt","w")
with open("abc.txt","r") as ab:
    data=ab.read()
    for x in data:
        f1.write(x)
f1.close()

with open("pqr.txt","r") as ab:
    print(ab.read())

with open("abc.txt","r")as ax:
    data=ax.read()
    UPL=0
    LWL=0
    INT=0
    for x in data:
        if ord(x)>=65 and ord(x)<=90:
            UPL+=1
        elif ord(x)>=97 and ord(x)<=122:
            LWL+=1
        elif ord(x)>=48 and ord(x)<=57:
            INT+=1
        else:
            pass
print("number of upper case letter",UPL)
print("number of lower case letter",LWL)
print("number of integers",INT)

with open("abc.txt","r") as ax:
    data=ax.read()
    vowel=0
    for x in data:
        if x=="a" or x=="A" or x=="e" or x=="E" or x=="I" or x=="i" or x=="o" or x=="O" or x=="u" or x=="U":
            vowel=vowel+1
print("no of vowels are=",vowel)



