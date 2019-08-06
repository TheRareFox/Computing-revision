from create_list import create_list_sorted

def linear_search(arr,search):
    for i in arr:
        if i == search:
            return "Search is True"
    return "Search is False"

arr = create_list_sorted(100)
search = int(input())
#print(arr)
#print(search)
print(linear_search(arr,search))
