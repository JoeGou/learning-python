number = input("Enter a number, i will tell you whether it's even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")