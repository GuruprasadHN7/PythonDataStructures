class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self,new_data):
      new_node = Node(new_data)
      new_node.next = self.head
      self.head = new_node

    def insertAfter(self,prev_node,new_data):
      if(prev_node is not None):
        print("prev node must be in linkedlist")
        return
      new_node = Node(new_data)
      new_node.next = prev_node.next
      prev_node.next = new_node

    def append(self,new_data):
      new_node = Node(new_data)
      if(self.head is None):
        self.head = new_node
        return
      last = self.head
      while(last.next):
        last = last.next
      
      last.next = new_node
    
    def PrintList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = Linkedlist()
    llist.append(4)
    llist.push(5)
    llist.append(7)
    llist.insertAfter(llist.head.next,8)
    llist.PrintList()