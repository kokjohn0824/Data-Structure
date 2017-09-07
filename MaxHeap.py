class MaxHeap():
    def __init__(self):
        self.heap = [0]
        self.current_size = 0

    def print_heap(self):
        for index in range(1, self.current_size + 1):
            print(self.heap[index], end=" ")
        print()
    
    def push(self, value):
        self.heap.append(value)
        self.current_size += 1
        self.__moveup(self.current_size)

    def __moveup(self, index):
        while index // 2:
            if self.heap[index] > self.heap[index // 2]:
                self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index //= 2

    def pop(self):
        if self.isEmpty():
            return
        self.__movedown()
        self.current_size -= 1

    def __movedown(self):
        index = 1
        while index:
            i = self.find_max(index)
            if i:
                self.heap[index] = self.heap[i]
            index = i

    def find_max(self, index):
        if index * 2 + 1 <= self.current_size:
            return index * 2 if self.heap[index * 2] >= self.heap[index * 2 + 1] else index * 2 + 1
        elif index * 2 <= self.current_size:
            return index * 2
        else:
            return None

    def isEmpty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size