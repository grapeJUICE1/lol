import math

for i in range(1 ,51):
    b=str(math.sqrt(i))
    index = b.index('.')
    c = b[0:index+2]
    if  b == c:
        print(i)

# index = str(math.sqrt(4)).index('.')
# a = str(math.sqrt(4))[index + 1] ;
#
# print(
#     a == 0
#      ,
#     index,
#     a,
#     b[0:index+2] ,
#     # str(math.sqrt(4)),
#     len(str(math.sqrt(4)))
# )
