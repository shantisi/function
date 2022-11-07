# Q35. Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)
# 13 --> "drink toddy"
# 18 -->"drink coke"
# 20 --> "drink beer"
# 30 --> "drink whisky".

def function():
    age=int(input("enter the number:"))
    if age<=14:
        print("Children under","drink toddy")
    elif age >=14 and age<=18:
        print('Teens under',"drink coke")
    elif age>=18 and age<=30:
        print("Young under", "drink beer")
    elif age >=30:
        print("Adults have","drink whisky")
function()