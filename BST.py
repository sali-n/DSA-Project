import timeit
import sys

class BSTNode:
    def __init__(self, key=None, name=None, city=None, cate=None):
        self.left = None
        self.right = None
        self.key = key
        self.name = name
        self.city = city
        self.cate = cate
        self.size = sys.getsizeof(self.name)+sys.getsizeof(self.city)+sys.getsizeof(self.cate)+sys.getsizeof(self.key)+sys.getsizeof(self.left)+sys.getsizeof(self.right)
        self.parent = None
    
    def tree_min(self):
        if self.left is None:
            return self
        else:
            return self.left.tree_min()  
        
    def get_size(self):
         left_size = 0
         right_size = 0
         if self.left: # nodes
              left_size = self.left.get_size()
         if self.right:
              right_size = self.right.get_size()
         return self.size + left_size + right_size     
             
    def insertKey(self, key, name, city, cate):
        if not self.key:
            self.key = key
            self.name = name
            self.city = city
            self.cate = cate
            return
        if self.key == key:
            return
        if key < self.key:
            if self.left:
                self.left.insertKey(key, name, city, cate)
                return
            self.left = BSTNode(key, name, city, cate)
            self.left.parent = self
            return
        if self.right:
            self.right.insertKey(key, name, city, cate)
            return
        self.right = BSTNode(key, name, city, cate)
        self.right.parent = self

    def inorder(self):
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
            
    def find(self,key):
        if self.key==key:  #key is node to find
             return
        if self.key<key:
            self.right.find(key)
        else:
            self.left.find(key)

def deleteNode(root, key):
	if root is None:
		return root
	if key < root.key:
		root.left = deleteNode(root.left, key)
	elif(key > root.key):
		root.right = deleteNode(root.right, key)
	else:
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		temp = root.right.tree_min()
		root.key = temp.key
		root.right = deleteNode(root.right, temp.key)

	return root

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
    
    lt=BSTNode()
    
    s = timeit.default_timer()
    for i in data_array:
        lt.insertKey(int(i[0]), i[1], i[2], i[3])
    e = timeit.default_timer()
    size = lt.get_size()
    print(f"Insert\t\t\t\t\tExecution Time:\t{round(e-s, 7)}s\t\tMemory Consumption:\t{size} bytes")
    
    s = timeit.default_timer()
    for i in range(0, len(data_array), 2):
        lt.find(int(data_array[i][0]))
    e = timeit.default_timer()
    print(f"Find\t\t\t\t\tExecution Time:\t{round(e-s, 7)}s\t\tMemory Consumption:\t{size} bytes")

    
    s = timeit.default_timer()
    lt.inorder()
    e = timeit.default_timer()
    print(f"Sorted Traversal\t\tExecution Time:\t{round(e-s, 7)}s\t\tMemory Consumption:\t{size} bytes")
    
    root = lt.left.parent
    s = timeit.default_timer()
    for i in range(1, len(data_array), 2):
       root = deleteNode(root,int(data_array[i][0]))
    e = timeit.default_timer()
    print(f"Delete\t\t\t\t\tExecution Time:\t{round(e-s, 7)}s\t\tMemory Consumption:\t{size} bytes\n")