num = [3,5,1,4,5,8,9,1]
def func(num):
   n = len(num)
   for i in range(1,n):
    key = i
    j = i-1
    while j>=0 and num[j]>key:
        num[j+1] = num[j]
        j -= 1

    num[j+1] = key 
sorted_list = func(num)
print(num)    
