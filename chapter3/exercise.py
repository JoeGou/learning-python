# #3-1
# names = ["Zhang san", "Li si", "WANG WU", "zhao liu", "ma qi"]
# print(names[0].title())
# print(names[1].title())
# print(names[2].title())
# print(names[3].title())
# print(names[4].title())

#3-2
# print(f"Hello, {names[0].title()}, are you ok?")
# print(f"Hello, {names[1].title()}, are you ok?")
# print(f"Hello, {names[2].title()}, are you ok?")
# print(f"Hello, {names[3].title()}, are you ok?")
# print(f"Hello, {names[4].title()}, are you ok?")

#3-3
# commuting = ["railway", "car", "bicycle", "airplane", "boat"]
# print(f"I would like to own my {commuting[0].title()}")

#3-4
guests =["Elon Musk", "Jim keller", "Steven"]
# print(guests[0].title())
# print(guests[1].title())
# print(guests[2].title())

#3-5
absense = guests.pop(2)
guests.append("Jensen")
# print(guests[0].title())
# print(guests[1].title())
# print(guests[2].title())

#3-6
guests.insert(0, "Jin")
guests.insert(2, "gates")
guests.append("Lisa")
print(guests)
print(f"{guests[0].title()}, welcome to my dinner")
print(f"{guests[1].title()}, welcome to my dinner")
print(f"{guests[2].title()}, welcome to my dinner")
print(f"{guests[3].title()}, welcome to my dinner")
print(f"{guests[4].title()}, welcome to my dinner")
print(f"{guests[5].title()}, welcome to my dinner")

print("\nSorry, my table can't send in time, so i only can invite two members to my dinner")

guests_5 = guests.pop()
print(f"\n{guests_5.title()}, I am so sorry")

guests_4 = guests.pop()
print(f"\n{guests_4.title()}, I am so sorry")

guests_3 = guests.pop()
print(f"\n{guests_3.title()}, I am so sorry")

guests_2 = guests.pop()
print(f"\n{guests_2.title()}, I am so sorry")

print(f"{guests[0].title()}, welcome to my dinner")
print(f"{guests[1].title()}, welcome to my dinner")

del guests[0]
del guests[0]

print(guests)

