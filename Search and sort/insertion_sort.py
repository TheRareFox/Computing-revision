from create_list import create_list_random

#time notation O(n^2)

def insertion_sort(arr):
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
    return arr

if __name__=="__main__":
    arr = create_list_random(10)
    print(insertion_sort(arr))
