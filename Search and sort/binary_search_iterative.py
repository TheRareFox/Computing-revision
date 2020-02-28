from create_list import create_list_sorted

#time notation O(n^2)


def binary_search_iterative(arr,target):
    half = len(arr)//2
    while target is not arr[half]:
        if len(arr) == 1:
            return "Not found"
        elif target>arr[half]:
            arr = arr[half:]
            half = len(arr)//2
        elif target <arr[half]:
            arr = arr[:half]
            half = len(arr)//2
    return "Found {}".format(target)

arr = create_list_sorted(1000)
print(binary_search_iterative(arr,102))
