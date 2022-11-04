import random
def addition(num1, num2):
    print((num1),"+",(num2))
    addition_answer = num1 + num2
    user_response = int(input("Answer >> "))
    if user_response == addition_answer:
        return "That's correct!"
    else:
        return "Oops... Better luck next time"

def subtraction(num1, num2):
    print(num1, "-", num2)
    addition_answer = num1 - num2
    user_response = int(input("Answer >> "))
    if user_response == addition_answer:
        return "That's correct!"
    else:
        return "Oops... Better luck next time"

def multiplication(num1, num2):
    print((num1), "*", (num2))
    addition_answer = num1 * num2
    user_response = int(input("Answer >> "))
    if user_response == addition_answer:
        return "That's correct!"
    else:
        return "Oops... Better luck next time"
def type(equation, num1, num2):
    if equation == "multiplication":
        print(multiplication(num1, num2))
    elif equation == "subtraction":
        print(subtraction(num1, num2))
    else:
        print(addition(num1, num2))

def main():
    equation = str(input("Would you like to try addition, subtraction, or multiplication"))
    max_num = int(input("What is the largest number you would like to use within your equation?"))
    min_num = int(input("What is the smallest number you would like to use within your equation?"))
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    type(equation, num1, num2)

main()