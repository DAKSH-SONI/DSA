arr = [15,6,8,10,5,8,654,45,1,2,3,4,9,5,6,4,64,64,1,3,1,32]
n = len(arr)
# slection sort
def selction_sort(arr):
    for i in range(0,n-1):
        mid_index = i
        for j in range(i+1,n):
            if arr[j]<arr[mid_index]:
                mid_index = j
        arr[i],arr[mid_index] = arr[mid_index],arr[i]
        
selction_sort(arr)
print(arr)

