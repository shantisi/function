# Q33. Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi > 30 return "Obese"
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"

def list():
    bmi=int(input("enter no "))
    if bmi >=30: 
        return "obese"
    elif bmi<=18.5:
        return "underweight"
    elif bmi<=25.0:
        return "normal"
    elif bmi<30:
        return "overweight"
a=list()
print(a)


