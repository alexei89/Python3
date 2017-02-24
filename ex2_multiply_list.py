#14 feb 2017
#Write a python program to multiply all items in a list.

def multiply_list(items):
    m_list = 1
    for x in items:
        m_list = m_list * x
    return m_list

print(multiply_list([2,3,11]))