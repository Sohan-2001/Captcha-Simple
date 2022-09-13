import random
import string
def func():
    print("Here's the Captcha: ",end="")
    a,b,c,d=random.randint(0,9),random.randint(0,9),random.choice(string.ascii_letters),random.choice(string.ascii_letters)
    print(a,b,c,d)
    CAP=str(a)+str(b)+c+d
    inp=input("\nEnter the Captcha: ")
    if inp!=CAP:
        print("\nTry Again\n")
        func()
    else:
        print("\nLoggin In\n")

func()
    
        


    



