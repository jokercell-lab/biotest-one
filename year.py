year = int(input("Enter the year you want to check: "))

x1 = year%4
x2 = year%100
x3 = year%400
if x1 == 0 :
    print(f"{year} It is a leap year! ")
else:
    print(f"{year} It is not leap year! ")