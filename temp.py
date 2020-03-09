import sys
def gcd(a,b): 
    if (b == 0): 
         return a 
    return gcd(b, a%b)
def inv(a, m):
    if(gcd(a,26)!=1):
        sys.exit("key not have inverse")
    for i in range(26):  
        if((a*i)%26==1):
            return i
        
def encrypt(cipher_type,operation_type,input_file,output_file,k):
    with open(input_file,'r') as reader:
        mess=reader.read();    
    cipher_type=cipher_type.lower()
    operation_type=operation_type.lower()
    result = "" 
    if (operation_type=="encrypt"):
        if (cipher_type=="shift" ):
            if (len(k)!=1):
                sys.exit("not valid :only one key")
            k[0]=int(k[0])
            for i in range(len(mess)): 
                char = mess[i]
                if(char==" "):
                    result +=" "
                elif (char.isupper()): 
                    result += chr((ord(char) + k[0] - 65) % 26 + 65)  
                else: 
                    result += chr((ord(char) + k[0] - 97) % 26 + 97)
        elif (cipher_type=="affine"):
            if (len(k)!=2):
                sys.exit("not valid :must two key a and b")
            k[0]=int(k[0])
            k[1]=int(k[1])
            for i in range(len(mess)): 
                char = mess[i]
                if(char==" "):
                    result +=" "
                elif (char.isupper()): 
                    result += chr(( ((ord(char) * k[0]) + k[1] )- 65) % 26 + 65)  
                else: 
                    result += chr(( ((ord(char) * k[0]) + k[1] )- 97) % 26 + 97)
        elif (cipher_type=="vigenere"):
            if (len(k)!=1):
                sys.exit("not valid :only one string key")
            key=k[0]
            if len(mess) != len(key):  
                for i in range(len(mess)-len(key)):
                    key+=key[i % len(k[0])]
            for i in range(len(mess)): 
                char = mess[i]
                if(char==" "):
                    result +=" "
                elif (char.isupper()): 
                    result += chr((ord(mess[i])+ord(key[i])) % 26 + 65)  
                else: 
                    result += chr((ord(mess[i])+ord(key[i])) % 26 + 97)
        else:
            print("invalid input")
    elif (operation_type=="decrypt"):
        if (cipher_type=="shift"):
            if (len(k)!=1):
                sys.exit("not valid :only one key")
            k[0]=int(k[0])
            for i in range(len(mess)): 
                char = mess[i]
                if(char==" "):
                    result +=" "
                elif (char.isupper()): 
                    result += chr((ord(char) - k[0] - 65) % 26 + 65)  
                else: 
                    result += chr((ord(char) - k[0] - 97) % 26 + 97)
        elif (cipher_type=="affine"):
            if (len(k)!=2):
                sys.exit("not valid :must two key a and b")
            k[0]=int(k[0])
            k[1]=int(k[1])
            a=inv(k[0] , 26)
            b=26-k[1]
            for i in range(len(mess)):
                char=mess[i]
                if(char==" "):
                    result +=" "
                elif (char.isupper()):
                    result += chr(( ((a*(ord(char)+b))- 65) % 26 + 65))
                else:
                    result += chr(( ((a*(ord(char)+b))- 97) % 26 + 97))
        elif (cipher_type=="vigenere"):
            if (len(k)!=1):
                sys.exit("not valid :only one string key")
            key=k[0]
            if len(mess) != len(key):  
                for i in range(len(mess)-len(key)):
                    key+=key[i % len(k[0])]
            for i in range(len(mess)): 
                char = mess[i]
                if(char==" "):
                    result +=" "
                elif (char.isupper()): 
                    result += chr((ord(mess[i])-ord(key[i])) % 26 + 65)
                else: 
                    result += chr((ord(mess[i])-ord(key[i])) % 26 + 97)
        else:
            print("invalid input")
    else:
        print("invalid input")
    with open (output_file,'w') as writer:
        writer.write(result)
    return result 


if(len(sys.argv)==6):
    encrypt(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],[sys.argv[5]])
elif(len(sys.argv)==7):
    encrypt(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],[sys.argv[5],sys.argv[6]])
