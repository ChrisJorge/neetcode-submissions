class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.li = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.li[i]

    def set(self, i: int, n: int) -> None:
        self.li[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.li[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.li[self.length]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        self.newLi = [0] * self.capacity
        for i in range(self.length):
            self.newLi[i] = self.li[i]
        self.li = self.newLi

    def getSize(self) -> int:
       return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
