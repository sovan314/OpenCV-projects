import random
import math

#genrating random number and showing rules
x=random.randint(0,10)
score = 100
print("\t\t\t\t\t****************Rules*****************")
print("\t\t\t\t  The Number is between 0 and 10 ")
print("\t\t\t\t\t\t\t you've only maximun of 7 chances to guess the integer")

#HINTS
multiples = [x*3,x*5,x*7]
greater = x+10
less = x-10
if x > 1:
    for i in range (2,int(x/2)+1):
        if (x % i) == 0:
            prime = "it is not a prime number"
            break
        else:
            prime = "it is a prime number "
factors=[]
def get_factors(x):
    factors.clear()
    for i in range(1,int(x/2)):
        if x % i == 0:
         factors.append(i)
    if x>10:
         factors.remove(1)


def hint1():
    print("Hint 1")
    print("multiples of number are :",multiples)
    print("\n")
def hint2():
    print("Hint 2")
    print("number is greater than :",less)
    print("\n")
def hint3():
    print("Hint 3")
    print("number is less than :",greater)
    print("\n")
def hint4():
    print("Hint 4")
    print(prime)
    print("\n")
def hint5():
    print("Hint 5")
    if prime == "it is not a prime number":
        get_factors(x)
        print("its some factors are :",factors)
    print("\n")


def show_hints(x , i ,y):
    if x != y and i==1:
        hint1()
    if x != y and i==2:
        hint2()
    if x != y and i == 3:
        hint3()
    if x != y and i == 4:
        hint4()
    if x != y and i == 5:
        hint5()

#GUESSES
for i in range (7):
    print("\n")
    print("this is your",i + 1,"try.")
    print("\n")
    if i > 0  and i < 6:
        show_hints(x, i, y)
    try:
        y = int(input("guess a number:-"))
    except ValueError:
        print("the input was not a valid integer")
    if x==y:
        print("\n")
        print("************congratulations you did it in",i + 1 , " try **************")
        print("your score is :",score)
        print("thanks for playing")
        print("\n")
        break
    if x> y+20:
        print("you gussed too small")
        score-=10
    if x<y-20:
        print("you gussed too high")
        score-=10
    if x>y and x<y+10:
        print("you gussed very close just a little bit higher")
        score -=10
    if x<y and x>y-10:
        print("you guessed very close little bit lower")
        score -=10

if y != x:
    print("\n\n")
    print("you failed to guess the number in 7 tries the number was ",x)
    print("your score is:",score)
    print("better luck next time!")
    print("thanks for playing!")
    print("\n")
