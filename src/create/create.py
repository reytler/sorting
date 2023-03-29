import random

def createList(length):
    x = range(length)
    list = []
    for n in x:
        list.append(random.randrange(0,200))
    
    return list