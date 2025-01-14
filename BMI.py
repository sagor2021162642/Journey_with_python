height = float(input("Height: "))
weight = float(input("Weight: "))


bmi = weight/(height*height)

if bmi<18.5:
    print("You are under weight")
elif 18.5 < bmi < 25:
    print("Normal")
else:
    print("Not Okay")