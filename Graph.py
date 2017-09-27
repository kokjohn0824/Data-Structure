class ListNode(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Graph(object):
    def __init__(self, numOfnodes):
        self.adj_list = [None] * numOfnodes

    def add_edge(self, tail, head):
        if not self.adj_list[tail]:
            self.adj_list[tail] = ListNode(head)
        elif not self.exist_edge(tail, head):
            self.adj_list[tail] = ListNode(head, self.adj_list[tail])            
        
        if not self.adj_list[head]:
            self.adj_list[head] = ListNode(tail)
        elif not self.exist_edge(head, tail):
            self.adj_list[head] = ListNode(tail, self.adj_list[head])
            
    def delete_edge(self, tail, head):
        if not self.adj_list[tail] or not self.adj_list[head]:
            return
        
        previous = None
        node = self.adj_list[tail]
        while node:
            if node.value == head:
                if previous:
                    previous.next = node.next
                else:
                    self.adj_list[tail] = self.adj_list[tail].next
                break
            previous = node
            node = node.next

        previous = None
        node = self.adj_list[head]
        while node:
            if node.value == tail:
                if previous:
                    previous.next = node.next
                else:
                    self.adj_list[head] = self.adj_list[head].next
                break
            previous = node
            node = node.next

    def exist_edge(self, tail, head):
        node = self.adj_list[tail]
        while node:
            if node.value == head:
                return True
            node = node.next
        return False
    
    def print_all(self):
        for i, n in enumerate(self.adj_list):
            print(i, end=': ')
            while n:
                print(n.value, end=" ")
                n = n.next
            print()

    def DFS(self, start):
        self.visited = [False] * len(self.adj_list)
        self.order = []
        self.recursive_dfs(start)
        return self.order

    def recursive_dfs(self, vertex):
        self.visited[vertex] = True
        self.order.append(vertex)
        node = self.adj_list[vertex]
        while node:
            if not self.visited[node.value]:
                self.recursive_dfs(node.value)
            node = node.next

    def BFS(self, vertex):
        from collections import deque
        order = []
        q = deque()
        visited = [False] * len(self.adj_list)
        order.append(vertex)
        visited[vertex] = True
        q.append(vertex)
        while q:
            vertex = q.popleft()
            node = self.adj_list[vertex]
            while node:
                if not visited[node.value]:
                    order.append(node.value)
                    q.append(node.value)
                    visited[node.value] = True
                node = node.next
        return order

    def connected(self):
        visited = [False] * len(self.adj_list)
        connected_components = []
        for i in range(len(self.adj_list)):
            if not visited[i]:
                connected_components.append(self.DFS(i))
        return connected_components