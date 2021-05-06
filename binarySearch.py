def left_bound(arr, key):
    left = -1
    right = len(arr)
    while right - left > 1:
        middle = (left+right)//2
        if arr[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(arr, key):
    left = -1
    right = len(arr)
    while right - left > 1:
        middle = (left+right)//2
        if arr[middle] <= key:
            left = middle
        else:
            right = middle
    return right


print("right",right_bound([1,2,3,4,5,6,7,8,9,10],9))
print("left",left_bound([1,2,3,4,5,6,7,8,9,10],9))
print(binary_search([1,2,3,4,5,6,7,8,9,10],10))