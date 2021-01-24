
food_in = ['banana', 'apple', 'grava', 'sigma']
coun_t  = ['600', '700', '800', '900', '450', '555']
num = len(food_in)

# x = 0
# for x in range(0,num):
#     x = x + 1
# print(x)
xxx = [int(n) for n in coun_t]

print(xxx)

s = 0
for s in range(0, len(coun_t)):
    coun_t[s] = int(coun_t[s]) + int(coun_t[s])
    
print(s)
print(coun_t)

nummm = 0
for n in range(1,100):
    print(n)