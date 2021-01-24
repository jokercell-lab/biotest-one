x = [1,2,3,4,5,6,7,8,9]
y = [11,22,33,44,55,66,77]
z = ["a", "b", "c"]

nest1 = [x, y, z]
nest2 = [y, z, x]
nest3 = [z, x, y]
nest  = [nest1, nest2, nest3]
print(nest)
print(x+y+z)
print(z+y+x)