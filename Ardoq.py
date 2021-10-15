
def partition(list, low, high):
    i = (low-1)
    pivot = list[high]
    for x in range(low, high):
        if list[x] <= pivot:
            i = i+1
            list[i], list[x] = list[x], list[i]
    list[i+1], list[high] = list[high], list[i+1]
    return (i+1)

def quicksort(list, low, high):
    if len(list) == 1:
        return list
    if low < high:
        pi = partition(list, low, high)
        quicksort(list, low, pi-1)
        quicksort(list, pi+1, high)
    return list

def largestproduct(list):
    list = quicksort(list, 0, len(list)-1)
    prod1 = list[0]*list[1]*list[len(list)-1]
    prod2 = list[len(list)-1]*list[len(list)-2]*list[len(list)-3]

    if prod1 > prod2: return prod1
    else: return prod2 


arr = [5, 6, 7, -10, -12, -3]
print(largestproduct(arr))


        

    

