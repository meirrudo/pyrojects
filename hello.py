'''
x = 5

if ( 3 % 2 == 0):
    print("hello1")
else:
    print("hello2")

'''
devidingBy = False
count = 0

for i in range(2,1001):
    devidingBy = False
    for j in range(2,i-1):
        if  i % j == 0:
            devidingBy = True
            break

    if not devidingBy:
        print(i)
        count = count +1

print(count)





print ("hello {0}".format("python"))