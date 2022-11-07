# Jacob Rae - 11/06/2022
# This program will allow the user to practice simple math equations, and the numbers they would like to use
import random
def addition(num1, num2):
    '''
    If the user selects addition
    :param num1: First number generated
    :param num2: Second number generated
    :return: Tells user if their answer was correct or incorrect.
    '''
    print((num1),"+",(num2))
    addition_answer = num1 + num2
    user_response = int(input("Answer >> "))
    if user_response == addition_answer:
        return "That's correct!"
    else:
        return "Oops... Better luck next time!"

def subtraction(num1, num2):
    '''
    If the user selects subtraction
    :param num1: First number generated
    :param num2: Second number generated
    :return: Tells user if their answer was correct or incorrect.
    '''
    print(num1, "-", num2)
    addition_answer = num1 - num2
    user_response = int(input("Answer >> "))
    if user_response == addition_answer:
        return "That's correct!"
    else:
        return "Oops... Better luck next time"

def multiplication(num1, num2):
    '''
    If the user selects multiplication
    :param num1: First number generated
    :param num2: Second number generated
    :return: Tells user if their answer was correct or incorrect.
    '''
    print((num1), "*", (num2))
    addition_answer = num1 * num2
    user_response = int(input("Answer >> "))
    if user_response == addition_answer:
        return "That's correct!"
    else:
        return "Oops... Better luck next time"
def type(equation, num1, num2):
    '''
    Runs whichever function the user chooses, based on which equation they picked
    :param equation: The user's chosen type of equation
    :param num1: First number generated
    :param num2: Second number generated
    :return: Returns the equation chosen
    '''
    if equation == "multiplication":
        print(multiplication(num1, num2))
    elif equation == "subtraction":
        print(subtraction(num1, num2))
    else:
        print(addition(num1, num2))

def main():
    '''
    Runs the random number generator, and receives input from user.
    :return: Sends all inputs to the other functions
    '''
    equation = str(input("Would you like to try addition, subtraction, or multiplication "))
    max_num = int(input("What is the largest number you would like to use within your equation? "))
    min_num = int(input("What is the smallest number you would like to use within your equation? "))
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    type(equation, num1, num2)

main()