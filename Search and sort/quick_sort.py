from create_list import create_list_random

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

#arr = create_list_random(100)
#print(quick_sort(arr))
