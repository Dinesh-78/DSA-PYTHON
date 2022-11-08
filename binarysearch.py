
def BinarySearch(arr,key):
    left=0
    right=len(arr)-1

    while(left<=right):
        mid = (left + right) // 2
        if arr[mid]>key:
            right = mid - 1
        elif arr[mid]==key:
            return "KEY ELEMENT FOUND"
        else:
            left = mid + 1

    return "KEY ELEMENT NOT FOUND"






arr=[40,77,81,89,92]
key=77
k=BinarySearch(arr,key)
print(k)

#Time Complexity -- O(log n)