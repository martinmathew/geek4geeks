from src.tree.Tree import Tree


class Kth:

    def __init__(self,k):
        self.count = k

    def kth(self,root:Tree.Node)-> Tree.Node:
        if root is None or self.count == 0:
            return None



        self.kth(root.right)
        if(self.count == 1):
            return root
        else:
            self.count -=1
            return self.kth(root.left)

if __name__ == "__main__":
    nums = [20, 22, 8, 12, 4, 10, 14]
    tree = Tree()
    tree.insert(nums)
    kth = Kth(7)
    print(kth.kth(tree.root).val)
