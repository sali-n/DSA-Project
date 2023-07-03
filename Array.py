import timeit
from sys import getsizeof as gof       
#Project-----------------------------------------------------------------------
def mergeSort(array):
    if len(array) > 1:

        r = len(array)//2
        
        L = []
        for i in range(r):
            L.append(array[i])
        M = []
        for i in range(r,len(array)):
            M.append(array[i])
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            
values = [1000,10000,100000,1000000]
for p in range(len(values)):
    data = []
    with open(f'data_{values[p]}.txt','r') as f:
        for k,line in enumerate(f):
            if k>1:
                a = line.split('\t')
                data.append([int(a[0]),[str(a[1]),str(a[2]),str(a[3].split('\n')[0])]])
   
    print(f'For {values[p]} records:')
    a = []
    b = timeit.default_timer()
    for i in data:
        a.append(i)
    e = timeit.default_timer()
    print(f"Insert\t\t\t\t\tExecution Time:\t{round(e-b, 7)}s\t\tMemory Consumption:\t{gof(data)/1024} KB")   
    
    if p<3:
        r = timeit.default_timer()
        mergeSort(a)
        t = timeit.default_timer()
        print(f"Traversal\t\t\t\tExecution Time:\t{round(t-r, 7)}s\t\tMemory Consumption:\t{(gof(data))/1024} KB")
    
    b = timeit.default_timer()
    o = 0
    for i in data:
        if o%2==0:
            i in data
        o += 1
    e = timeit.default_timer()             
    print(f"Find\t\t\t\t\tExecution Time:\t{round(e-b, 7)}s\t\tMemory Consumption:\t{gof(data)/1024} KB") 
    
    b = timeit.default_timer()
    o = 0
    for i in data:
        if o%2==0:
            data.remove(i)
        o += 1
    e = timeit.default_timer()
    
    print(f"Deletion\t\t\t\tExecution Time:\t{round(e-b, 7)}s\t\tMemory Consumption:\t{gof(data)/2024} KB",'\n')