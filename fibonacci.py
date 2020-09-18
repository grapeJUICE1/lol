list = [0 , 1]

l = int(input('fibonacci for how many nums???'))

for i in range(1 , l+1):
    if i > 2 :
        list.append(sum(list))

print(list)
print(len(list))
