import random

# random.seed(123)
# random_integer = random.randint(1,13)
# print(random_integer)

# random_float = random.random()*9
# print(random_float)

test_seed = int(input("Enter a seed number: "))
random.seed(test_seed)
x = random.randint(0,1)
if x==1:
    print("Heads")
else:
    print("Tails")