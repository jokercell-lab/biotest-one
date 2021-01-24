import random
test_seed = int(input("Enter a seed number: "))
random.seed(test_seed)

names_csv = input("Give everybody's name: ")
names = names_csv.split(",")

# x = len(names)
# y = random.randint(0, x-1)
y = random.choice(names)
print(y)

