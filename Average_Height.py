student_height = input('Enter Height List: ').split()
#print(student_height[0])
sum_all_the_height = 0
iterator = 0
average = 0
#we can also use sum function

for iterator in range(0,len(student_height)):
    convert_student_height = int(student_height[iterator])
    sum_all_the_height = sum_all_the_height + convert_student_height
    #print(iterator)
average = sum_all_the_height/(iterator+1)
print(average)