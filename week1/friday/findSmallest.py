arr = [2,3,45,12,234,5,6,789]

def find_smallest(arr):
    value = arr[0]
    for i in range(0,len(arr)):
        if i > 0 and arr[i] < value:
            value = arr[i]
    return value;

print("Find the smallest number in a given array")
print(arr)
print(find_smallest(arr))
