try:
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))

    if width == length:
        exit("That is a square.")
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number: ")