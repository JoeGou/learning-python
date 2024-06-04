from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
my_lottery = []

for i in range(4):
    number_word = choice(lottery)
    my_lottery.append(number_word)
    print(f"- you pulled the {number_word}...")
    if number_word == 4:
        print("Congratulations! You won!") 
        break

# print(my_lottery)

# for n_w in my_lottery:
#     if n_w == 4:
#         print("Congratulations! You win the big prize!") 
