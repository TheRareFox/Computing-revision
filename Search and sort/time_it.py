import time
from create_list import create_list_sorted,create_list_random
#sorting
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
random = create_list_random(1000)

t = time.time()
bubble_sort(random)
time1 = time.time()-t
print("efficiency of {} is {}s".format("bubble sort",time1))

t = time.time()
insertion_sort(random)
time1 = time.time()-t
print("efficiency of {} is {}s".format("insertion sort",time1))

t = time.time()
merge_sort(random)
time1 = time.time()-t
print("efficiency of {} is {}s".format("merge sort",time1))

t = time.time()
quick_sort(random)
time1 = time.time()-t
print("efficiency of {} is {}s".format("quick sort",time1))
