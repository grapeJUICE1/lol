num = int(input("ur number"))
list= []

for i in range(2 , num):
    if num % i == 0:
        list.append(True)
    else:
        list.append(False)

if list.__contains__(True):
    print('Number not prime')
else:
    print('Number is prime')
