class TreeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self, root=None):
        self.root = root
    
    def isEmpty(self, node):
        return node is None

    def left_child(self, node):
        if self.isEmpty(node):
            return
        return node.left

    def right_child(self, node):
        if self.isEmpty(node):
            return
        return node.right

    def get(self, node):
        if self.isEmpty(node):
            return
        return node.data

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def iterInorder(self, node):
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack:
                break
            node = stack.pop()
            print(node.data, end=" ")
            node = node.right

    def levelorder(self, node):
        if not node:
            return
        from collections import deque
        queue = deque()
        queue.append(node)
        while queue:
            node = queue.popleft()
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Return a Pointer to a same data from original node
    def copy(self, node):
        if node:
            return TreeNode(node.data, self.copy(node.left), self.copy(node.right))
        return None

    @staticmethod
    def equal(first, second):
        return (not first and not second) or \
    (first and second and (first.data == second.data) \
    and BinaryTree.equal(first.left, second.left) and BinaryTree.equal(first.right, second.right))