from random import choice

my_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
win_flag = True
times = 0

while win_flag:
    number_word = choice(my_ticket)
    print(f"- you pulled {number_word}...")
    times += 1
    if number_word == 4:
        print(f"Congratulations! You won!\n You has attempted {times} times")
        win_flag = False
        