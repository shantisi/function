# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"


def num():
    bmi=int(input("enter no"))
    if bmi <= 18.5:
        print("Underweight")
    elif bmi >=18.5 and bmi <= 25.0:
        print("Normal")
    elif bmi>=25.0 and bmi <= 30.0:
        print("Overweight")    
    elif bmi > 30:
        print("Obese")
num()