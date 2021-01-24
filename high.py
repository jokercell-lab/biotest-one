#print the hightest score without max()

student_score = input("Enter student score: ").split()
student_score = [int(n) for n in student_score]
print(student_score)

h_score = 0
for x in student_score:
    if x > h_score:
        h_score = x




print(f"the highest score in the class : {h_score} ")