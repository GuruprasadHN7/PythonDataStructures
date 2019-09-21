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
      if(prev_node is  None):
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

    def popByVal(self,val):
      temp = self.head
      if(temp is not None):
        if(temp.data == val):
          self.head = temp.next
          temp = None
          return 

      while(temp is not None):
        if(temp.data == val):
          break
        prev = temp
        temp = temp.next
      
      if(temp == None):
        return 
      
      prev.next =  temp.next
      temp = None


    def popByPos(self,position):
      if(self.head is None):
        return
      temp = self.head
      if position == 0:
        self.head = temp.next
        temp = None
        return
      for i in range(position-1):
        temp = temp.next
        if(temp is None):
          break
        
      if(temp is None):
        return
      if(temp.next is None):
        return
      next = temp.next.next
      temp.next = None
      temp.next = next

    def getCountIter(self):
      temp = self.head
      count = 0
      while(temp):
        count += 1
        temp = temp.next
      return count 

    def getCountRec(self,node):
      if(not node):
        return 0
      return 1 + self.getCountRec(node.next)
    
    def getCount(self):
      return self.getCountRec(self.head)
      
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
    llist.insertAfter(llist.head,8)
    llist.PrintList()
    llist.popByVal(7)
    llist.PrintList()
    llist.popByPos(0)
    llist.PrintList()
    llist.append(2)
    print('the length of the list',llist.getCountIter())
    print(llist.getCount())