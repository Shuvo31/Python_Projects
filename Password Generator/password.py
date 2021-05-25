import string
import random
def generate():
    s1=string.ascii_uppercase
   
    s2=string.ascii_lowercase
    
    s3=string.digits
    
    s4=string.punctuation

    passwordlength=int(input("Enter the password length:"))

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    
    password =("".join(s[0:passwordlength]))
    print(password)
generate()