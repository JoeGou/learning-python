# message = input("Tell me something, and i will repeat it back to you")
# print(message)


prompt = "\nTell me something, and i will repeat it back to you"
prompt += "Enter 'quit' to end the program:  "

message = ''
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)