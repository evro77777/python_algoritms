def bubble_sort(arr):
    for bypass in range(1,len(arr)):
        for k in range(0,len(arr)-bypass):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr




print(bubble_sort([0,1,1,2,3,4,5,44,7,8,9,10]))
