


class LinkedList:
    head = None

    class Node:

        def __init__(self,val):
            self.val = val
            self.next = None




    def insert(self,val)->Node:
        newNode = LinkedList.Node(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            parent = None
            while temp.next is not None:
                temp = temp.next

            temp.next = newNode
    def len(self,head:Node):
        temp = head;
        count = 0
        while temp is not None:
            temp = temp.next
            count +=1

        return count


    def checkIfPalindrome(self,head:Node)->Node:
        if head is not None:
            parent = None;
            temp = head
            temp_jump = head;
            count = 1
            length = self.len(head)
            while temp_jump is not None and temp_jump.next is not None:
                parent = temp;
                temp = temp.next
                temp_jump = temp_jump.next
                temp_jump = temp_jump.next
                count+=1
            parent.next = None;
            tail = None
            if length%2 == 1:
                tail = self.reverse(temp.next)
            else:
                tail = self.reverse(temp)
            tmp = head
            ttmp = tail
            while ((tmp is not None and ttmp is not None) and tmp.val == ttmp.val):
                tmp = tmp.next
                ttmp = ttmp.next
            return tmp is None and ttmp is None


    def reverse(self,head:Node)->Node:
        temp = head;
        parent = None;
        while temp is not None:
            temp1=temp.next;
            temp.next = parent;
            parent = temp
            temp = temp1
        return parent
if __name__ == "__main__":
    ll = LinkedList()
    nums = ['a','a']
    for num in nums:
        ll.insert(num)
    print(ll.checkIfPalindrome(ll.head))




