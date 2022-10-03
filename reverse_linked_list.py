class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, val):
        temp = Node(val)
        temp.next = None
        if self.size == 0:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

        self.size += 1

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next

    def size_of_list(self):
        return self.size
        # count = 0
        # temp = self.head
        # while(temp):
        #     count += 1
        #     temp = temp.next
        # return count

    def remove_first(self):
        if self.size == 0:
            return "List is empty"
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            # temp = self.head
            # temp.next = self.head.next
            # self.head = temp.next
            self.size -= 1
        return self.head

    def get_first(self):
        if self.size == 0:
            return -1
        else:
            return self.head.val

    def get_last(self):
        if self.size == 0:
            return -1
        else:
            return self.tail.val

    def get_at(self, idx):
        if self.size == 0:
            return -1
        elif idx <0 or idx >= self.size:
            return "Invalid Arguments"
        else:
            temp = self.head
            for i in range(idx):
                temp = temp.next
            return temp.val

    def add_first(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        if self.size == 0:
            self.tail = temp
        self.size += 1
        return self.head

    def get_node_at(self, idx):
        temp = self.head
        for i in range(idx):
            temp = temp.next
        return temp

    def add_at(self, idx, val):
        new_node = Node(val)
        new_node.next = None
        if idx ==0:
            self.add_first(val)
        elif idx == self.size:
            self.add_last(val)
        else:
            temp = self.head
            for i in range(idx-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1
        return self.head

    def remove_last(self):
        if self.size == 0:
            return -1
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            for i in range(self.size -2):
                temp=temp.next
            self.tail = temp
            temp.next = None
            self.size -= 1

    def reverse_list(self):
        l = 0
        h = self.size-1
        while(l<h):
            left_node = self.get_node_at(l)
            right_node = self.get_node_at(h)

            left_node.val, right_node.val = right_node.val, left_node.val
            l += 1
            h -= 1
        return self.head

    def reverse_pointer(self):
        cur = self.head
        prev = None
        while(cur):
            next_p = cur.next
            cur.next = prev
            prev = cur
            cur = next_p
        self.head = prev
        return self.head

    def remove_at_index(self, idx):
        if idx < 0 or idx >= self.size:
            return "Invalid arguments"
        elif idx==0:
            self.remove_first()
        elif idx == self.size -1:
            self.remove_last()
        else:
            temp = self.head
            for i in range(0, idx-1):
                temp = temp.next
            temp.next = temp.next.next
            self.size -=1


l = LinkedList()
l.add_last(3)
l.add_last(4)
l.add_last(6)
l.add_last(8)

l.printList()

l.reverse_list()
print("after reverse")
l.printList()

print("After pointer")
l.reverse_pointer()
l.printList()

print("remove at index")
l.remove_at_index(2)
l.printList()
