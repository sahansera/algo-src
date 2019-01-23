'''
Find the middle of a linked list
Very often, linked list questions need to have O(n) time complexity, but not necessarily true
and space: O(1)

Technique - Fast and Slow Pointer
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        curNode = self.head
        while(curNode.next != None):
            curNode = curNode.next
        curNode.next = Node(val)

    def printLinkedList(self):
        curNode = self.head
        while(curNode != None):
            print(curNode.val)
            curNode = curNode.next

    def getMiddle(self):
        # check for empty
        if self.head == None:
            return self.head

        slow = self.head
        fast = self.head

        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        return slow

linkedlist = SinglyLinkedList()
linkedlist.head = Node(0)
linkedlist.add(1)
linkedlist.add(2)
linkedlist.printLinkedList()
middlePtr = linkedlist.getMiddle()
print('middle is=', middlePtr.val)
