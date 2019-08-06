from create_list import create_list_sorted

def binary_search_iterative(arr,target):
    half = int(len(arr)//2)
    while target != arr[half]:
        if half == 1:
            return "Not found"
            break
        elif target>arr[half]:
            arr = arr[half:]
            half = int(len(arr)//2)
        elif target <arr[half]:
            arr = arr[:half]
            half = int(len(arr)//2)
        
    return "Found {}".format(target)

arr = create_list_sorted(1000)
print(binary_search_iterative(arr,102))
