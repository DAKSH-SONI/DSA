arr = [1,4,4,3,4,5]
def func(arr, i, j):
    if i>=j:
        return
    arr[i], arr[j] = arr[j], arr[i]
    func(arr, i+1, j-1)
func(arr, 0, len(arr)-1)    
print(arr)

i = 0
j = len(arr) - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
print(arr)