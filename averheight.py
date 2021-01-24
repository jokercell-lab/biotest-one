
# x = input("number: ").split(" ")
# y = len(x) # y is an integre
# print(x)
# print(y)

student_height = input("Enter the height: ").split(" ")
#student_height = [int(n) for n in student_height]  #1 轉為list&int的語法
#student_height = list(map(int, student_height))   #2

for n in range(0, len(student_height) ):
    student_height[n] = int(student_height[n])
# print(student_height)
stu = 0
for std in student_height:     #len()
    stu = stu + 1 

sum_hi = 0                     #sum()
for x in student_height:
    sum_hi = sum_hi + x
    avr = sum_hi/stu
avr = round(avr,2)
print(f"The average height: {avr}")