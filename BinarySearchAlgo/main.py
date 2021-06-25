def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


arr = [2, 3, 4, 10, 20, 21, 22, 25, 30, 31, 34, 37, 40]

print("Your array is " , str(arr))
print("Which element you wanna search ? ")

x = int(input())

result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
