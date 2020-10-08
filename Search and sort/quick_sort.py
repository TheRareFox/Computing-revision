from create_list import create_list_random

#time notation O(nlog(n)) worse case O(n^2)

def quick_sort(arr):
    less = []
    more = []
    equal = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i>pivot:
                more.append(i)
            elif i<pivot:
                less.append(i)
            else:
                equal.append(i)
        return quick_sort(less) + equal + quick_sort(more)
    
def quicksortb(elements):
    if len(elements) == 0:
        return []
    else:
        return quicksortb([i for i in elements[1:] if i < elements[0]]) + [elements[0]] + quicksortb([i for i in elements[1:] if i >= elements[0]])

#arr = create_list_random(100)
#print(quick_sort(arr))
