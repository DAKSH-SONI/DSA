n = [1,1,2,3,4,5,5,6,5,4,8,9,10,]
m = [1,111,2,3,4,5,6,88,44,6,10]

hash_list = [0]*11
for i in n:
    hash_list[i] += 1
print(hash_list)
hash_list = [0]*11
for i in m:
    if i<1 or i>10:
        pass
    else:
        hash_list[i] += 1
print(hash_list)
