#8-6
# def city_country(city, country):
#     message = f"{city.title()} {country.title()}"    
#     return message

# pair1 = city_country('san diego', 'US')
# pair2 = city_country('shanghai', 'china')
# pair3 = city_country('suzhou', 'china')

# pairs = [pair1, pair2, pair3]

# for pair in pairs:
#     print(pair)
    
    
#8-7
# def make_album(singer, album, music_number = None):
#     album_info = {'singer': singer.title(), 'album': album.title(), 'music_number': music_number}
    
#     if music_number:
#         album_info['music_number'] = music_number
    
#     return album_info

# while True:
#     print(f"\nPlease enter the album info: ")
#     print(f"(Please enter 'q' if you want to exit)")
    
#     singer_name = input("Enter the singer name: ")
#     if singer_name == 'q':
#         break
    
#     album_name = input("Enter the album name: ")
#     if album_name == 'q':
#         break
    
#     music_number = input("Enter the music number: ")
#     if music_number == 'q':
#         break
    
#     album_info = make_album(singer_name, album_name, music_number)
#     print(album_info)    


#8-9.8-10

# def send_messages(show_messages, sent_messages):
#      while show_messages:
#         current_message = show_messages.pop(0)
#         sent_messages.append(current_message)
#         print(f"{current_message.title()}")
        
# def show_messages(sent_messages):
#     for message in sent_messages:
#         print(f"\n {message.title()} has been sent")
        
# messages = ['A+b', 'C+d', 'D+e', 'f+g']
# sent_message = []

# send_messages(messages[:], sent_message)
# show_messages(sent_message)

# print(messages)
         
         
#8-12
# def sandwich_message(*toppings):
#     print("The sandwich is made with the following ingredients:  ")
#     # for topping in toppings:
#     #     print(f"\n{topping.title()}")
#     print(toppings)
        
# sandwich_message('mushrooms', 'cheese', 'carrots', 'ham')
# sandwich_message('nothing', 'one')


#8-13
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('Gou', 'zhuang',
#                              location = 'suzhou',
#                              field = 'engineer',
#                              hobby = 'hiking')

# print(user_profile)

#8-14

def make_Car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_Car('porsche', 'Taycan', 
               color = 'green',
               price = '$200_000',
               accessories = 'hub'
                )

print(car)
    