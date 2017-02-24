#18 feb 2018
#Write a program to count the number of strings
#where the string lenght is 2 or more and the
#first and the last character are same for a given
#stirng

def stringcheck(words):
    counter = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter +=1
    return counter
print(stringcheck(['ana','are','elenele']))