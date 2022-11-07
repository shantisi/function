# Q20.What is the output of the following code snippet?
# num = 1
# def func():
# num = 3
# print(num)
# func()
# print(num)
# A. 1 3
# B. 3 1
# C. The program has a runtime error because x is not defined.
# D. 1 1
# E. 3 3
# ans: B



num = 1
def func():
    num = 3
    print(num,end=" ")
func()
print(num)
