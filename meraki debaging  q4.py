def greet(*names):
    for name in names:
        print("Welcome", name)
greet("Rinki", "Vishal", "Kartik", "Bijendar")

def info(name, age ):
       print(name + " is " + age + " years old")

info("Sonu","5")
info("Sana", "17")
info("Umesh", "18")


def studentDetails(name,currentMilestone,mentorName):
    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


studentDetails("Nilam","loop","pooja")


def students(name):
    print("I am here")
    print("my name is ",name)
    print("I am co founder of Nvgurukul")
students("priya")


def stu_name(*names):
    i=0
    b=[]
    while i<len(names):
        d="priya","rani","kajal","rakhi"
        b.append(d)
        i=i+1
    print(b)
stu_name("names")



n=[1,2,3,4,[2,5,5,6]]
i=0
b=[]
while i<len(n):
    if type (n[i])==list:
        j=0
        k=1
        while j<len(n[i]) and k<len(n[i]):
            if n[i][j]==n[i][k]:
                b.append(n[i][j])
                print(b)
            j=j+1
            k=k+1
    
        else:
            b.append([i])    
    i=i+1


a=int(input("enter no"))
i=0
max=0
min=0
b=[]
while i<a:
    n=int(input("enter no"))
    j=0
    b.append(n)
    i=i+1
print(b)

a=int(input("enter no"))
i=0
max=0
b=[]
while i<a:
    n=int(input("enter no"))
    b.append(n)
    i=i+1
print(b)
j=0
max=0
min=b[0]
while j<len(b):
    if b[j]>max:
        max=b[j]
    if b[j]<min:
        min=b[j]
    j=j+1
print(b)
print(max,min)
a=[2,3,4,5,[3,4,5],4,5,6]
i=0
sum=0
while i<len(a):
    if type (a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)

    