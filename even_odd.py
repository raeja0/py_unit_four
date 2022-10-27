
def even_or_odd(number):
    if number % 2 == 0:
        return (str(number) + " is even")
    else:
        return (str(number) + " is odd")

def main():
    number = int(input("Please enter your desired number >> "))
    print(even_or_odd(number))
    pass

if __name__ == '__main__':
    main()