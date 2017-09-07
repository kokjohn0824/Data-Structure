class QueueNode():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue():
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def print_queue(self):
        current = self.front
        while current:
            end = " -> " if current.next else "\n"
            print(current.value, end=end)
            current = current.next
    
    def add(self, value):
        if self.isEmpty():
            self.front = QueueNode(value)
            self.rear = self.front
        else:
            self.rear.next = QueueNode(value)
            self.rear = self.rear.next

    def delete(self):
        if self.isEmpty():
            print("Delete nothing, the queue is empty.")
        else:
            self.front = self.front.next

    def search(self, value):
        count = 0
        current = self.front
        while current:
            if current.value == value:
                return count
            count += 1
            current = current.next

    def top_value(self):
        if self.isEmpty():
            return "Nothing at the top, the stack is empty!"
        return self.front.value

    def end_value(self):
        if self.isEmpty():
            return "Nothing at the end, the stack is empty!"
        return self.rear.value

    def isEmpty(self):
        return self.front is None