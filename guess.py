import random
def guess(x,y):
    if y != x:
        print("Damn bro... that's not my number... stupid")
        print("My number was "+str(x))
    else:
        print("WOW! How'd you know?")
def main():
    x = random.randint(1, 10)
    y = int(input("Guess my number! >> "))
    guess(x,y)
main()