que= ["How many continents are there?","What is the capital of India?",
                "NG mei kaun se course padhaya jaata hai"]
option= [["1.Four", "2.Nine", "3.Seven", "4.Eight"],
              ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
              ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution = [3, 4, 1] 
lifeline = [
['1.Four','3.seven'],
['2.Bhopal','4.Delhi'],
['1.Software Engineering','2.Counseling']]
print("Welcome to KBC")
money=0
life_line=2
def ques():
    if len(que)>0:
        i=0
        while i<1:
            print(que[i])
            que.remove(que[i])
            i=i+1
        opt()
    else:
        print("Take your prise",money)
        print("THANK YOU")
        
        
def opt():
    j=0
    while j<1:
        for i in option[j]:
            print(i)
        option.remove(option[j])
    
        j=j+1
    lif()
def ans():
    global money
    answer=int(input("enter answer"))
    if answer==1 or answer==2 or answer==3 or answer==4:
        k=0
        while k<1:
            if answer==solution[k]:
                money+=1000
                solution.remove(solution[k])
                ques()
            else:
                solution.remove(solution[k])
                print("wrong answer")
                print("answer is",solution)
                ques()
            k=k+1
    else:
        print("enter valid answer in 1,2,3,4")
        ans()
def lif():
    global life_line
    if life_line>0:
            l=0
            while l<=1:
                life=input("enter the lifeline")
                if life =="yes":
                    life_line-=1
                    for i in (lifeline[l]):
                        print(i)
                    lifeline.remove(lifeline[l])
                    ans()
                elif life=="no":
                    lifeline.remove(lifeline[l])
                    ans()
                else:
                    print("tell answer yes or no")
                    lif()
    else:
        print("you can't take lifeline")
    
        ans()
ques()    



str='ram rahim sona juju'
i=0
a=str.split()
f=[]
while i<len(a):
    if "sona"!=a[i]:
        f.append(a[i])
    i=i+1
print(f)


    