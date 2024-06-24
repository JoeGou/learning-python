print("Please enter 2 numbers for add operation")
while True:
    
    number_1 = input('Please input number 1: ')
    if number_1 == "quit":
        break
    number_2 = input('Please input number 2: ')
    if number_2 == "quit":
        break
    else:
        try:       
            result = int(number_1) + int(number_2)
            print(f"The addition result is: {result}")
        except ValueError:
            print("Please enter a number, word can't be added")

        