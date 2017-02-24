#21 feb 2017
#Write a python program to find the list
#of word that are longer than n from a given 
#list of words.

def words_lenght(mylist):
    n = int(input("Introduce-ti lungimea cuvintelor: ",))
    newlist=[]
    for word in mylist:
        if len(word)> n:
            newlist.append(word)
    return newlist

print(words_lenght(['ana','are','mere']))
