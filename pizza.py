print("Welcom to Pizza order system ")
size = input("what size pizza do you want? S, M, or L ")
add_pepper = input("do you want add pepper? Y or N ")
extra_cheese = input("do you want extra cheese? Y or N ")
price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25

if  add_pepper == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"your price is :${price}")