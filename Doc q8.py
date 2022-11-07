# Q8.Write a Python function that accepts a string and calculate the number of upper 
# case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def num(list):
    i=0
    upper=0
    lower=0
    c=0
    c1=0
    while i<len(list):
        if list[i]>="A" and list[i]<="Z":
            print(list[i],"uppercase")
            c=c+1
        elif list[i]>="a" and list[i]<="z":
            print(list[i],"lowercase")
            c1=c1+1
        i=i+1
    print(c)
    print(c1)
num("The quick Brow Fox")
