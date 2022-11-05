from random import randint
def greet_random():
    n=0
    greetings=["hi","hellow","vanakkam","welcome","hey","yo"]
    n = randint(0,len(greetings)-1)
    return(greetings[n])

greeting = greet_random()
print(greeting)
