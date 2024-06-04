# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'red', 'points': 10}
# alien_2 = {'color': 'yellow', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)
    
# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5}
#     aliens.append(new_alien)
    
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = '10'
#         alien['speed'] = 'medium'
    
# for alien in aliens[:7]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = '10'
#         alien['speed'] = 'medium'
    
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['points'] = '15'
#         alien['speed'] = 'fast'
        
# for alien in aliens[:9]:
#     print(alien)
    
# print("...")


#6-7

# user_0 = {
#     'first': 'san',
#     'last': 'zhang',
#     'age': '20',
#     'city': 'shanghai'
# }

# user_1 = {
#     'first': 'si',
#     'last': 'li',
#     'age': '30',
#     'city': 'suzhou'
# }

# user_2 = {
#     'first': 'wu',
#     'last': 'wang',
#     'age': '40',
#     'city': 'hangzhou'
# }

# user_3 = {
#     'first': 'liu',
#     'last': 'zhao',
#     'age': '40',
#     'city': 'califonia'
# }

# peoples = [user_0, user_1, user_2, user_3]

# #错误实现方式
# # for user in peoples:
# #     for user_name, user_info in user.items():
# #         print(f"\tuser name: {user['first'].title()} {user['last'].title()}")
# #         print(f"\tuser age: {user['age'].title()} ")
# #         print(f"\tuser location: {user['city'].title()} ")
        
# for user in peoples:
#     print(f"\tuser name: {user['last'].title()} {user['first'].title()}")
#     print(f"\tuser age: {user['age'].title()} ")
#     print(f"\tuser location: {user['city'].title()} ")


#6-8
# pet_0 = {
#     'variety': 'dog',
#     'master':   'Jack'
# }

# pet_1 = {
#     'variety': 'cat',
#     'master':   'John'
# }

# pet_2 = {
#     'variety': 'panda',
#     'master':   'David'
# }

# pets = [pet_0, pet_1, pet_2]

# for pet in pets:
#     print(f"This pet is {pet['variety'].title()}, it's master is {pet['master'].title()}")

#6-9

# favorite_places = {
#     'Jack': ['paris', 'vienna', 'iceland'],
#     'David': ['Maldives', 'fiji', 'Bali'],
#     'Luci': ['bahama', 'mauritius', 'Norway']
# }

# for friend, places in favorite_places.items():
#     print(f"\n{friend.title()}'s favorites places are :")
#     for place in places:
#         print(f"\t{place.title()}")

#6-10

# favorite_numbers = {
#     'Jack': [1, 2, 3],
#     'David': [4, 5, 6],
#     'Luci': [8, 88, 888]
# }

# for friend , numbers in favorite_numbers.items():
#     print(f"\n{friend.title()}'s favorite numbers are:")
#     for number in numbers:
#         print(f"\t{number}")

#6-11

cities = {
    'Suzhou': {
        'country': 'China',
        'populations': 10727120,
        'fact': 'Know for its classical garden and silk industry'
    },
    
    'Shanghai': {
        'country': 'China',
        'populations': 24256800,
        'fact': 'Finacial hub of China'
    },
    
    'Silicon Valley': {
        'country': 'United states',
        'populations': 3912000,
        'fact': 'Silicon Valley is a global center for high technology and innovation'
    }
}

for city, description in cities.items():
    print(f"{city.title()} is a beautiful city which locates in  {description['country']} and has a population of {description['populations']}.\n\t{description['fact']} \n")