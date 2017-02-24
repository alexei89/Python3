#19 feb 2017
#Write a program that remove duplicates from a list
def remove_duplicates(my_list):
    dup_items = set()
    uniq_items = []
    for x in my_list:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    
    return dup_items

print(remove_duplicates([10, 20, 30, 20, 10, 55, 60, 40, 50, 80, 60, 40]))
