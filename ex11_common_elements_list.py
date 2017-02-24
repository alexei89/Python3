#21 feb 2017
#write a python function that takes two lists
#and returns TRUE if the have at least 1 
#element in common.

def list_compare(mylist1, mylist2):
    counter = 0
    for i in mylist1:
        for j in mylist2:
            if i==j:
                counter+=1
    print("listele au ",counter,' elemnte comune')

list_compare([1,2,3,4,5],[6,7,8,9,1,3])