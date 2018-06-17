


class Tree:
    root = None
    class Node:

        def __init__(self,val):
            self.left = None
            self.right = None
            self.val = val


    def insert(self,arr):
        for num in arr:
            if self.root is None:
                self.root = self.Node(num)
            else:
                temp = self.root
                parent = None
                while temp is not  None:
                    parent = temp
                    if temp.val <= num:
                        temp = temp.right
                    else:
                        temp = temp.left

                new_node = self.Node(num)
                if parent.val <=num:
                    parent.right = new_node
                else:
                    parent.left = new_node


def getMaxNode(node:Tree.Node,parent:Tree.Node) -> (Tree.Node,Tree.Node):
    if node is not None and node.right is not None:
        return getMaxNode(node.right,node)
    else:
        return (node,parent)


def findKth(node:Tree.Node,parent:Tree.Node,k:int)->Tree.Node:
    if node is not None:
        max,maxPar = getMaxNode(node,parent)
        if k==1:
            return max
        elif k==2:
            return maxPar
        else:
            return findKth(maxPar.left,maxPar,k-2);




if __name__ == "__main__":
    nums = [20,22,8,12,4,10,14]
    tree = Tree()
    tree.insert(nums)
    node = findKth(tree.root,None,7)
    print(node.val)
