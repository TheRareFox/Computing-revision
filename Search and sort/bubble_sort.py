from create_list import create_list_random

#time notation O(n^2)

def bubble_sort(arr):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                sorted = True
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

if __name__=="__main__":
    arr = create_list_random(10)
    print(bubble_sort(arr))
