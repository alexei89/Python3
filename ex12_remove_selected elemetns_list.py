#23 feb 2017
#Write a Python program to print a specified list after removing the
# 0th, 2nd, 4th and 5th elements.

lista = ['red', 'green', 'white', 'black', 'pink', 'yellow']

def remove_elements(mylist):
    editedlist = []
    for i in range(0,len(mylist)-1):
        if i not in (0,4,5):
            editedlist.append(mylist[i])
    return editedlist

print(remove_elements(lista))
