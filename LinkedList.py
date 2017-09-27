# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_nodes(self):
        if not self.head:
            print(self.head)
        node = self.head
        while node:
            end = " -> " if node.next else "\n"
            print(node.val, end=end)
            node = node.next

    def at(self, index):
        count = 0
        node = self.head
        while node:
            if count == index:
                return node.val
            count += 1
            node = node.next

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(value)

    def insert(self, index, value):
        if index >= self.size():
            self.append(value)
            return
        count = 0
        node = self.head
        previous = None
        while node:
            if count == index:
                if previous:
                    new_node = ListNode(value, previous.next)
                    previous.next = new_node
                else:
                    self.head = ListNode(value, node)
                return
            count += 1
            previous = node
            node = node.next

    def removePos(self, index):
        count = 0
        node = self.head
        previous = None
        while node:
            if count == index:
                if previous:
                    previous.next = node.next
                    node = node.next
                else:
                    self.head = node.next
                    node = self.head
                return
            else:
                previous = node
                node = node.next

    def remove(self, val, all=False):
        node = self.head
        previous = None
        while node:
            if node.val == val:
                if previous:
                    previous.next = node.next
                    node = node.next
                else:
                    self.head = node.next
                    node = self.head
                if not all:
                    return
            else:
                previous = node
                node = node.next

    def indexOf(self, value):
        node = self.head
        count = 0
        while node:
            if node.val == value:
                return count
            count += 1
            node = node.next

    def clear(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count