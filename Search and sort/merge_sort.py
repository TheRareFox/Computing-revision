from create_list import create_list_random

#time notation O(nlog(n))

def merge_sort(arr):
    if len(arr) > 1:
        half = len(arr)//2
        left = arr[:half]
        right = arr[half:]
        merge_sort(left)
        merge_sort(right)

        # -- sorting occurs here --
        
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i] <right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k+=1

        # -- only one of this will execute --
            
        while i<len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j<len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
#arr = create_list_random(100)
#print(merge_sort(arr))
