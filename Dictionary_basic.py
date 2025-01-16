student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#print(student_scores["Harry"])
#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[key]
    if 90<score<101:
        student_grades[key] = "Outstanding"
    elif 80<score<91:
        student_grades[key] = "Exceeds Expectations"
    elif 70<score<81:
        student_grades[key] = "Acceptable"
    elif 60<score<71:
        student_grades[key] = "Fail"
    else:
        print("Wrong")

# 🚨 Don't change the code below 👇
print(student_grades)





