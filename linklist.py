# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class linklist:
#     def __init__(self):
#         self.head = None
    
#     def Insert_begin(self, data):
#         newnode = node(data)
#         if self.head is None:
#             self.head = newnode
#             return
#         newnode.next = self.head
#         self.head = newnode

    
#     def traverse(self):
#         if self.head is None:
#             print("linklist is empty")
#             return
#         cur = self.head
#         while cur:
#             print(cur.data, end="->")
#             cur = cur.next
#         print("None")

# # Testing
# ll = linklist()
# ll.Insert_begin(200)
# ll.Insert_begin(400)
# ll.Insert_begin(4)
# ll.traverse()



class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linklist:
    def __init__(self):
        self.head = None
    
    def Insert_end(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return
        cur = self.head
        while cur.next != None:  # last node tak jao
            cur = cur.next
        cur.next = newnode  # last node ke next me newnode jod do
    
    def traverse(self):
        if self.head is None:
            print("linklist is empty")
            return
        cur = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print("None")

# Testing
ll = linklist()
ll.Insert_end(20)
ll.Insert_end(30)
ll.Insert_end(40)
ll.traverse()
