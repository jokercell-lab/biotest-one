age = input("Enter your current age: ")
x = 90-int(age)
months = x*12
weeks  = x*52
days   = x*365
ans = f"You have {days} days, {weeks} weeks, {months} months left"
print(ans)