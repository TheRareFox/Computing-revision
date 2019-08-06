import random
def create_list_random(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(1,1000))
    return arr

def create_list_sorted(length):
    arr = []
    for i in range(length):
        arr.append(i)
    return arr
