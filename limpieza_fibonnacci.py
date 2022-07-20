
serie = [0,82,1,51,1,116,2,48,3,32,5,72,8,52,13,99,21,75,34,49,55,110,89,71]

x = 0
for num in serie:
    if (num > x):
        x = num
#print(x)


fibb1 = 1
fibb2 = 1
result = 1

#numTerms = 999 #int(input("How many terms of Fibonacci sequence to print? "))

listabasura = {0}
listafibonacci = {1}

for i in range(999):
    #print (result)

    for num in serie:
        if num == result:
            listafibonacci.add(num)
        else:
            listabasura.add(num)

    
    result = fibb1 + fibb2
    fibb1 = fibb2
    fibb2 = result
    if result > x:
        break
    
print (listafibonacci)
for i in listafibonacci:
    listabasura.remove(i)
print (listabasura)




#max