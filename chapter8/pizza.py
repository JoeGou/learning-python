def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for item in toppings:
        print(f"\n\t-{item.title()}")
