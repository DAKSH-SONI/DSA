num = [3,2,1,4,5,8,9,1]
def func(num):
    n = len(num)
    key =0
    for i in range(0,n-1):
        if i>key:
            key = i
        for j in range(i+1,n-1):
            if num[key]>num[j]:
                num[key],num[j] = num[j] ,num[key]
sorted_list = func(num)
print(sorted_list)                
