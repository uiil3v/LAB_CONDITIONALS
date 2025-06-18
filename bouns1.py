
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))


BMI = weight / (height * height)

print(f"Your BMI is: {round(BMI,2)}")

if BMI > 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif 18.5 <= BMI <= 25:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")
