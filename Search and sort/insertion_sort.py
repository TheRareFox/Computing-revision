from create_list import create_list_random

#time notation O(n^2)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        pointer = i
        while arr[pointer]>arr[pointer-1] and pointer > 0:
            arr[pointer],arr[pointer-1] = arr[pointer-1],arr[pointer]
            pointer -= 1
    return arr

#arr = create_list_random(100)
#print(insertion_sort(arr))
