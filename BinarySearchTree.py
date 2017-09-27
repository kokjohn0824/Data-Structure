class TreeNode():
    def __init__(self, data=None, key=None, left=None, right=None):
        self.data = data
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print("{}({})".format(node.data, node.key), end=" ")
            self.inorder(node.right)

    def levelorder(self, node):
        if not node:
            return
        from collections import deque
        queue = deque()
        queue.append(node)
        while queue:
            current = queue.popleft()
            print("{}({})".format(current.data, current.key), end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def search(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        print("Key {} is not in the tree.".format(key))

    def insert(self, data, key):
        if not self.root:
            self.root = TreeNode(data, key)
            return
        current = self.root
        while current:
            if key < current.key:
                if not current.left:
                    current.left = TreeNode(data, key)
                    return
                current = current.left                
            else:
                if not current.right:
                    current.right = TreeNode(data, key)
                    return
                current = current.right

    def delete(self, key):
        node, parent, direction = self.__search_for_node_and_its_parent(key)
        if not node:
            print("Key {} not in the tree.".format(key))
            return

        if not node.left and not node.right:
            if direction == "left":
                parent.left = None
            else:
                parent.right = None
            return
        elif not node.left or not node.right:
            if node.left:
                if direction == "left":
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                if direction == "left":
                    parent.left = node.right
                else:
                    parent.right = node.right
            return
        else:
            successor, parent = self.find_successor_and_its_parent(node)
            node.data, node.key = successor.data, successor.key
            parent.left = successor.right

    def find_successor_and_its_parent(self, node):
        previous = node
        node = node.right
        if node.left:
            previous = node
            node = node.left
        return node, previous

    def __search_for_node_and_its_parent(self, key):
        previous = None
        direction = None
        current = self.root
        while current:
            if key == current.key:
                return current, previous, direction
            elif key < current.key:
                previous = current
                current = current.left
                direction = "left"
            else:
                previous = current
                current = current.right
                direction = "right"