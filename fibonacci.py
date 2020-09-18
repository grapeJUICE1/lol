# ----solution 1 ---- myway

def fibonacci(occ):
    a = 0
    list = [0 , 1]
    l = occ
    if l <= 0:
        return 0
    elif l == 1:
        return [0]
    else:
        for i in range(1 , l+1):
            if i > 2 :
                list.append(list[a] + list[len(list)-1])
                a+=1

        return list

print(fibonacci(24))


#----solution 2 ------

def fibo(n):
    a = 0
    b = 1

    if n == 1:
        return 0
    else:
        print(a)
        print(b)

        for i in range(2 , n):
            c = a + b
            a = b
            b = c
            print(c)

fibo(24)
