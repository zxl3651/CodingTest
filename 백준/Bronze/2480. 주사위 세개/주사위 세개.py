arr = list(map(int, input().split()))
arr.sort()
if max(arr) == min(arr):
    print(10000 + max(arr)*1000)
else:
    if min(arr) == arr[1]:
        print(1000 + min(arr) * 100)
    elif max(arr) == arr[1]:
        print(1000 + max(arr) * 100)
    else:
        print(max(arr) * 100)