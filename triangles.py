def is_triangle(side1, side2, side3):
    if ((side1 + side2) < (side3)) or ((side1 + side3) < side2) or ((side2 + side3) < side1):
        return "That's not a triangle!"
    else:
        return "Wow, that's totally triangular bro!"

def main():
    side1 = int(input("What is your first side length?"))
    side2 = int(input("What is your second side length?"))
    side3 = int(input("What is your third side length?"))
    print(is_triangle(side1, side2, side3))

if __name__ == '__main__':
    main()

