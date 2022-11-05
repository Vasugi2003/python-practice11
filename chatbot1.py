
from random import randint

def greet_random():
    quit_msg = ['quit','bye','exit']
    greetings=["hi","hellow","vanakkam","welcome","hey","yo"]
    n = randint(0,len(greetings))
    return(greetings[randint(0,n-1)])

greeting = greet_random()
print(greeting,',',"iam a simple chatbot i can do simple calcs")


while True:
    quit_msg = ['quit','bye','exit']
    greetings=["hi","hellow","vanakkam","welcome","hey","yo"]
    msg = input()
    split_msg=msg.split()
    print(split_msg)
    p1=float(split_msg[1])
    p2 = float(split_msg[2])
    
    if msg in quit_msg:
        print("THANKYOU!!!!")
        break
    elif "add" in msg:
        print(msg)
        print("You are going to perform addition")
        print(p1+p2)
        
    elif "mul" in msg:
        print(msg)
        print("You are going to perform multiplication")
        print(p1*p2)

    elif "sub" in msg:
        print(msg)
        print("You are going to perform subtraction")
        print(p1-p2)

    elif "div" in msg:
        print(msg)
        print("You are going to perform division")
        print(p1/p2)


    elif "expo" in msg:
        print(msg)
        print("You are going to perform exponential")
        print(p1**2)

    elif "modulo" in msg:
        print(msg)
        print("You are going to perform modulo")
        print(p1%p2)
