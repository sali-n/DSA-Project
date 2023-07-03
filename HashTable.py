import timeit   #for finding the time execution
from sys import getsizeof as gof   #for finding sizes

class HashTable:
    def __init__(self,sizex=0):
        self.size = sizex
        self.sizea = self.size
        self.slots = [None]*self.size
        self.data = [None]*self.size
        self.length = 0
        self.memory = 0
        
    def has(self,key,j=0):
        return ((key+(j*j))%self.sizea)   #quadractic hashing
    
    def __getitem__(self,key):  
        ogindex = self.has(key)
        if self.slots[ogindex] == key:
            return self.data[ogindex]
        else:
            i = 1
            index = ogindex
            while self.slots[index] is not None:
                index = self.has(ogindex,i)
                if self.slots[index] == key:
                    return self.data[index]
                i += 1
        raise ValueError(f'{key} item not getted')
            
    def __len__(self):
        return self.length
    
    def hash_function(self,key,value):
        ogindex = self.has(key)
        if self.slots[ogindex] is None or self.slots[ogindex] == 'DELETED':
            self.slots[ogindex] = key
            self.data[ogindex] = value
            self.length +=1  
            return
        else:
            index = 0
            i = 1
            while (index <= self.size):
                index = self.has(ogindex,i)
                if self.slots[index] is None or self.slots[index] == 'DELETED':
                    self.slots[index] = key
                    self.data[index] = value
                    self.length +=1  
                    return 
                i += 1
            if index >= self.size:
                raise IndexError('not inputted')
                
    def __delitem__(self,key):
        ogindex = self.has(key)
        if self.slots[ogindex] != key:
            i = 1
            index = ogindex
            while self.slots[index] is not None:
                index = self.has(ogindex,i)
                if self.slots[index] == key:
                    ogindex = index
                    break
                i += 1
            if self.slots[ogindex] != key: 
                raise IndexError(f'{key} - cannot be deleted')
        self.slots[ogindex] = 'DELETED'    #puting a mark
        self.length -= 1
        
    def __str__(self):
        a = ""
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                a += str(self.slots[i]) + " " + str(self.data[i]) + " | "
        return a
    
    def inordertraverse(self):
        a = [x for x in self.slots if x is not None] 
        a = list(filter(lambda x: x != 'DELETED',a))  #creating a seperate list to be ordered
        self.memory += gof(a)
        while len(a) != 0:
            b = min(a)
            k = str(b) + "," + str(self.__getitem__(b))
            a.remove(b)
            
#Project:----------------------------------------------------------------------          

values = [1000,10000,100000,1000000]
sizes = [1201,14389,141277,1278397]   

for i in range(len(values)):
    data = []
    with open(f'data_{values[i]}.txt','r') as f:
        for k,line in enumerate(f):
            if k>1:
                a = line.split('\t')
                data.append([int(a[0]),[str(a[1]),str(a[2]),str(a[3].split('\n')[0])]])
    print(f'For record {values[i]}:')
    a = HashTable(sizes[i])
    
    b = timeit.default_timer()
    for l in data :
        a.hash_function(l[0],l[1])
    e = timeit.default_timer()
    print(f"Insert\t\t\t\t\tExecution Time:\t{round(e-b, 7)}s\t\tMemory Consumption:\t{(gof(a.size) + gof(a.sizea) + gof(a.slots) + gof(a.data) + gof(a.length))/1024} KB")

    if i<3:
        b = timeit.default_timer()
        a.inordertraverse()
        e = timeit.default_timer()
        print(f"Traversal\t\t\t\tExecution Time:\t{round(e-b, 7)}s\t\tMemory Consumption:\t{(gof(a.size) + gof(a.sizea) + gof(a.slots) + gof(a.data) + gof(a.length) + a.memory)/1024} KB")
        
    b = timeit.default_timer()
    for l in range(len(data)):
        if l%2==0:
            k = a[(data[l])[0]]
    e = timeit.default_timer()
    print(f"Find\t\t\t\t\tExecution Time:\t{round(e-b, 7)}s\t\tMemory Consumption:\t{(gof(a.size) + gof(a.sizea) + gof(a.slots) + gof(a.data) + gof(a.length))/1024} KB")
    
    b = timeit.default_timer()
    for l in range(len(data)):
        if l%2 != 0:
            del a[(data[l])[0]]
    e = timeit.default_timer()
    print(f"Deletion\t\t\t\tExecution Time:\t{round(e-b, 7)}s\t\tMemory Consumption:\t{(gof(a.size) + gof(a.sizea) + gof(a.slots) + gof(a.data) + gof(a.length))/1024} KB",'\n')
# #------------------------------------------------------------------------------      