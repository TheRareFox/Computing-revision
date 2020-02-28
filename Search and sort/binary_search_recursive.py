from create_list import create_list_sorted

#time notation O(n^2)


def binary_search_recursive(arr,target):
    half = len(arr)//2
    #print(half)
    #print(arr)
    if target == arr[half]:
        return "Found {}".format(target)
    elif len(arr) == 1:
        return "Not found"
    elif target< arr[half]:
        return binary_search_recursive(arr[:half],target)
    elif target>arr[half]:
        return binary_search_recursive(arr[half:],target)


arr = create_list_sorted(1000)
print(binary_search_recursive(arr,241))
