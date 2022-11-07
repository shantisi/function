# Q37. Consider an array/list of sheep where some sheep may be missing from their place. We
# need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True, True, True, False,
# True, True, True, True ,
# True, False, True, False,
# True, False, False, True ,
# True, True, True, True ,
# False, False, True, True]

def func(list):
    i=0
    c=0
    c1=0
    while i<len(list):
        if list[i]==True:
            c=c+1
        
        i=i+1
    print(c,"Ture")
    
func([True, True, True, False,True, True, True, True ,
True, False, True, False,True, False, False, True ,
True, True, True, True ,False, False, True, True])