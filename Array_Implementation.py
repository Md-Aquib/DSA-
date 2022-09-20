class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def push(self,item):
        self.data[self.length] = item
        self.length+=1

    def get(self,index):
        try:
            return self.data[index]
        except KeyError:
            return "Index out of range"
        
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return last_item

    def insert(self,index,item):
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i-1]
            print(self.data[i])
        self.data[index] = item
        self.length+=1


a = MyArray()
a.push(2)
a.push(6)
a.push(3)
a.push(4)
a.insert(1,5)
print(a)
print(a.get(1))
print(a.pop())


