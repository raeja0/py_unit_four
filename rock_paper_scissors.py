import random
def who_wins(user, computer):
    if (user == 1 and computer == 1) or (user == 2 and computer == 2) or (user == 3 and computer == 3):
        return "It's a draw!"
    elif (user == 2 and computer == 1) or (user == 3 and computer == 2) or (user == 1 and computer == 3):
        return "You Win!"
    else:
        return "You lose!"


def main():
    print("Welcome to rock, paper, scissors!")
    print("Choose your weapon! 1 is rock, 2 is paper, 3 is scissors. Remember, no guns allowed!")
    user = int(input(">>"))
    computer = random.randint(1,3)
    print(user)
    print(computer)
    print(who_wins(user, computer))

if __name__ == '__main__':
    main()