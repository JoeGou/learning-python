def get_formatted_name(first_name, last_name, middle_name = ""):
    full_name = f"{first_name} {middle_name} {last_name}"

    return full_name.title()

while True:
    print("\nPlease tell me your name")
    print("\nenter 'q' at any time to quit")
    
    f_name = input("Enter your First Name: ")
    if f_name == 'q':
        break
    
    l_name = input("Enter your Last Name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHellow, {formatted_name}")