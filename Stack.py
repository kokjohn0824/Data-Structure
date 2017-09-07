class StackNode():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None


class Stack():
    def __init__(self, top=None):
        self.top = top

    def print_nodes(self):
        current = self.top
        while current:
            end = " -> " if current.next else "\n"
            print(current.value, end=end)
            current = current.next
    
    def push(self, value):
        old_top = self.top
        self.top = StackNode(value, old_top)
        self.top.next = old_top
    
    def pop(self):
        if self.isEmpty():
            print("Pop nothing, the stack is empty!")
            return
        self.top = self.top.next

    def top_value(self):
        if self.isEmpty():
            return "Nothing at the top, the stack is empty!"
        return self.top.value

    def search(self, value):
        count = 0
        current = self.top
        while current:
            if current.value == value:
                return count
            count += 1
            current = current.next

    def isEmpty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count