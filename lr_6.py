alphabet = "abcdefghijklmnopqrstuvwxyz"
key=input("Input key : \n")
f=open('text.txt')
text=f.read()
f.close()
text=text.replace(' ', '')
text=text.replace('\n', '')
key=len(text)//len(key)*key+key[0:len(text)%len(key)]
def codding(text,key):
    code_text=""
    for i in range(len(text)):
        if alphabet.index(key[i])-alphabet.index(text[i])>=0:
            code_text+=alphabet[alphabet.index(key[i])-alphabet.index(text[i])]
        else:
            code_text+=alphabet[26+alphabet.index(key[i])-alphabet.index(text[i])]
    return code_text
def uncodding(code_text,key):
    new_text=""
    for i in range(len(code_text)):
        if alphabet.index(key[i])-alphabet.index(code_text[i])>=0:
            new_text+=alphabet[alphabet.index(key[i])-alphabet.index(code_text[i])]
        else:
            new_text+=alphabet[26+alphabet.index(key[i])-alphabet.index(code_text[i])]
    return new_text
chose=input("1 - code; 2 - uncode; \n")
f=open("code.txt","w")
if chose=="1":
    f.write(codding(text,key))
if chose=="2":
    f.write(uncodding(text,key))
f.close()
