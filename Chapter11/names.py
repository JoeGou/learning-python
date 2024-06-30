from name_function import get_formmated_name as gfn

print("Enter 'q' at any time to quit")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break

    last = input("Please give me a last name: ")
    if first == 'q':
        break

    formatted_name = gfn(first, last)
    print(f"Neatly formmated name: {formatted_name}")
