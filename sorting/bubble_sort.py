num = [1,7, 5, 4, 6, 8, 9] #list0
def func(num): #function    
    arr = len(num) #length of list
    for i in range(arr-2,-1,-1): #loop start from n-2 index means start from 5 and  decrement bt -1
        is_swapped = False # inital swappped is false
        for j in range(0,i+1): # another loop start from 0 and gfo to the i+1
            if num[j]>num[j+1]: # if j is greter than j+1 so swaped
                num[j],num[j+1] = num[j+1] , num[j]
                is_swapped = True # this mean we maek swapped
        if not is_swapped:#if any swaapped no happen mean list already swapped
            break
    return num
sorted_list = func(num) 
print(sorted_list)

             