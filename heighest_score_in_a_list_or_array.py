student_score = input('Enter Score: ').split()
for iterator in range(0,len(student_score)):
    student_score[iterator] = int(student_score[iterator])
heighest = student_score[0]
for student in student_score:
    if(heighest<student):
        heighest = student
print(heighest)