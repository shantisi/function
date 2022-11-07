from curses import has_ic


# Apko max function ka use karke diye hue list me se sabse bada value print karvani hai.
# number[3,5,7,34,2,89,2,5]

def max(num):
    i=0
    max=0
    while i<len(num):
        if num[i]>max:
            max=num[i]
        i=i+1
    print("max number=",max)
max([3,5,7,34,2,89,2,5])

# Q4.Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".

def reverse(list):
    i=0
    while i<len(list):
        d=(list[::-1])
        i=i+1
    print(d)
reverse("1234abcd")