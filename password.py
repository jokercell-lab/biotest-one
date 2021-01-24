#password Generator
import random
letter = ['a','b','c','d','e','f','g',
'h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z','A','B','C',
'D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z',]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','∂','ç','©','å','∫']

print("Welcome to the Generator!!! ")
want_letter = int(input("How many letters do you want?\n"))
want_number = int(input("How many numbers do you want?\n"))
want_symbol = int(input("How many symbols do you want?\n"))

x = ""
for L in range(0, want_letter) :
    ran = random.choice(letter)
    x += ran
    # x += random.choice(letter)
#print(x)

y = ""
for N in range(0, want_number):
    num = random.choice(numbers)
    y += num
    # y += random.choice(numbers)
#print(y)

z = ""
for S in range(0, want_symbol):
    sym = random.choice(symbols)
    z += sym
    # z += random.choice(symbols)
#print(z)

# passwords = ""                          # teacher writing
# for char in range(1, want_letter+1):
#     passwords += random.choice(letter)
# for char in range(1, want_number+1):
#     passwords += random.choice(numbers)
# for char in range(1, want_symbol+1):
#     passwords += random.choice(symbols)
# print(passwords)

x = []
for L in range(0, want_letter) :
    x.append(random.choice(letter))
y = []
for N in range(0, want_number):
    y.append(random.choice(numbers))
z = []
for S in range(0, want_symbol):
    z.append(random.choice(symbols))

# x = []
# for L in range(0, want_letter) :
#     x.append(random.choice(letter))
# for L in range(0, want_number):
#     x.append(random.choice(numbers))
# for L in range(0, want_symbol):
#     x.append(random.choice(symbols))

pre_pass  = x + y + z
random.shuffle(pre_pass)
print(pre_pass)

final_pass = ""
for n in pre_pass:
    final_pass = final_pass + n
print(f"your password is: {final_pass}")

# wrong below
# final_pass = ''
# for F in range(0, len(pre_pass)):
#     xx = pre_pass[F]
    
# print(xx)
    # final_pass = random.choice(xx)

# print(final_pass)