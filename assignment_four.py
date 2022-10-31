import random
def addition(num1, num2, user_response):
    print((num1),"+",(num2))
    addition_answer = num1 + num2
    if user_response == addition_answer:
        print("That's correct!")
    else:
        print("Oops... Better luck next time")
    return addition_answer

def subtraction(num1, num2, user_response):
    print((num1), "-", (num2))
    addition_answer = num1 - num2
    if user_response == addition_answer:
        print("That's correct!")
    else:
        print("Oops... Better luck next time")
    return addition_answer

def multiplication(num1, num2, user_response):
    print((num1), "*", (num2))
    addition_answer = num1 * num2
    if user_response == addition_answer:
        print("That's correct!")
    else:
        print("Oops... Better luck next time")
    return addition_answer

def type(equation):
    if equation == addition :
        addition()
    elif equation == subtraction:
        subtraction()
    else:
        multiplication()

def main():
    equation = input("Would you like to try addition, subtraction, or multiplication")
    max_num = int(input("What is the largest number you would like to use within your equation?"))
    min_num = int(input("What is the smallest number you would like to use within your equation?"))
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    user_response = int(input("Answer >> "))
    return num1, num2, equation, user_response