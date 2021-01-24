# %3 print "Fizz"
# %5 print "Buzz"
# %3&5 print "FizzBuzz"
number = 0
for n in range(1,101):
    if n %(3*5) == 0 :     # n%3 == 0 and n%5 == 0 也可以
        print("FizzBuzz")
    elif n %3 == 0:
        print("Fizz")
    elif n %5 == 0:
        print("Buzz")
    else:
        print(n)