import time
from sys import getsizeof as gof

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

class Node :
   def __init__(self,dat=None,name=None,city=None,cat=None):
       self.data=dat
       self.city=city
       self.name=name
       self.cat=cat
       self.next=None
       self.memory = gof(self.data) + gof(self.city) + gof(self.name) + gof(self.cat) + gof(self.next)

       
class Linked_list:
    def __init__(self):
        self.size=0
        self.head=None
        self.tail=None
    
    def __str__(self):
        l=[]
        current=self.head
        while current:
            l.append(current.data)
            current=current.next
        return f"{l}"
        
    def __len__(self):
        return self.size
    
    def __setitem__(self,index, data):
        if (index < 0) or (index > self.size - 1):
            raise IndexError("Index out of range.")
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.data = data
        
    def __getitem__(self, index):
        if (index < 0) or (index > self.size - 1):
            raise IndexError("Index out of range.")
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.data
        
    def append(self,dat,city,name,cat):
        if self.head is None:
            self.head=Node(dat,city,name,cat)
        elif self.tail is None :
            self.tail=Node(dat,city,name,cat)
            self.head.next=self.tail
        else:
            n=self.tail
            n.next=Node(dat,city,name,cat)
            self.tail = n.next
        self.size+=1
        
    def delete(self,data):
        if self.head.data == data:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current:
            if current.next.data == data:
                if current.next.next is None:
                    current.next = None
                    self.tail = current
                else:
                    current.next = current.next.next
                self.size -= 1
                return
            current = current.next
    
    def search(self,val):
        current=self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False
    
    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += current.memory
            current = current.next
        return size
    
for i in range(3, 7):
    data_array = []
    print("Number of records =", 10**i)
    file = open(f'./data_{10**i}.txt', 'r')
    t = 0
    for i in file:
        if t < 2:
            t += 1
            continue
        data_array.append(list(map(str, i.split())))
    
    lt=Linked_list()
    
    s = time.time()
    for i in data_array:
        lt.append(int(i[0]), i[1], i[2], i[3])
    e = time.time()
    size = lt.get_size()
    print(f"Insert\t\t\t\t\tExecution Time:\t{round(e-s, 7)}s\t\tMemory Consumption:\t{size} bytes")
    
    s = time.time()
    for i in range(0, len(data_array), 2):
        lt.search(data_array[i][0])
    e = time.time()
    print(f"Find\t\t\t\t\tExecution Time:\t{round(e-s, 7)}s\t\tMemory Consumption:\t{size} bytes")

    
    s = time.time()
    mergeSort(lt)
    e = time.time()
    print(f"Sorted Traversal\t\tExecution Time:\t{round(e-s, 7)}s\t\tMemory Consumption:\t{size} bytes")
    
    s = time.time()
    for i in range(1, len(data_array), 2):
        lt.delete(int(data_array[i][0]))
    e = time.time()
    print(f"Delete\t\t\t\t\tExecution Time:\t{round(e-s, 7)}s\t\tMemory Consumption:\t{size} bytes\n")