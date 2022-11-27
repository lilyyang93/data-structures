class Node:
  # store your DATA and NEXT values here
  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node

  def __str__(self): #to print out our node values
    return f"Node: {self.data}, which points to: {self.next_node}"

class LinkList:
  # write your __init__ method here that should store a 'head' value which is the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head_node=None):
    self.head_node = head_node 
    self.length = 0


  def add(self, data):
    # write your code to ADD an element to the Linked List
    new_node = Node(data) #create a new node using the Node class 
    if self.head_node == None: #if there is currently no head node,  
      self.head_node = new_node #assign the new node that we just created as the head node.
    else:
      current_node = self.head_node #if there is already a head node, first reference current_node as the head node since that is the starting point
      if current_node.next_node == None: #if the current node doesn't have a node to point to (again, remember initially we will look at head node)
        current_node.next_node = new_node #then the current node will point to the new node we just created 
      else: #if the current node does already have a node to point to, keep traversing the linked list until we find one where its next node is None 
        while current_node.next_node: #so while a current node has an existing next node, 
          current_node = current_node.next_node #we can traverse the linked list by updating what the current node is by using its next node as reference 
          #once we find a node where it doesn't point to another node, we can break out of the loop
        current_node.next_node = new_node #and have the pointer-less node now point to the new node we just created 
    self.length += 1 #increase length of linked list by 1

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List

    #assign n_to_remove to the data argument
    #in our linked list, starting from the head node (current node), check to see if the current node's next node is n_to_remove
    #if it's not, continue.
    #once n_to_remove is found, reassign current_node's next node to n_to_remove's next node
    #then, remove n_to_remove 
      current_node = self.head_node #again we are starting by looking at the head node 
      prev_node = None 
      n_to_remove = data
      if current_node.data == n_to_remove: #if the head node is value we are trying to remove, 
        self.head_node = current_node.next_node #reassign the head node to what was supposed to be its next node 
      else: #if not...
        while current_node.data != n_to_remove: #while the current node we are looking at is not the value we want to remove (remember we start at head node)
          prev_node = current_node #previous node gets assigned to current node before we change the node we are currently looking at
          current_node = current_node.next_node #after we save the previous node, we can change the current node to its next node 
        prev_node.next_node = current_node.next_node #once the match is found, we can break out of the loop and reassign the previous node's next node to the match's next node 
      self.length -= 1

  def get(self, element_to_get):
    # write your code to GET and return an element from the Linked List
    current_node = self.head_node #again we are starting at the head node
    while element_to_get != current_node.data: #if the current node is not element to get, keep traversing the list until you find a match
      current_node = current_node.next_node
    return f"Node {element_to_get}"

linked_list1 = LinkList() #create a new linked list 
linked_list1.add(1) #add a data value (1) to the linked list 
#print(linked_list1.head_node.data) #-> 1
linked_list1.add(2) #add a data value (2) to the linked list 
#print(linked_list1.head_node.next_node.data) #-> 2
linked_list1.add(3) #add data values (3, 4, then 5) to the linked list 
linked_list1.add(4)
linked_list1.add(5)
#print(linked_list1.head_node) #-> Node: 1, Next node: Node: 2, Next node: Node: 3, Next node: Node: 4, Next node: Node: 5, Next node: None
#print(linked_list1.length) #-> 5
linked_list1.remove(1)
#print(linked_list1.head_node) #-> Node: 2, which points to: Node: 3, which points to: Node: 4, which points to: Node: 5, which points to: None
linked_list1.remove(3)
print(linked_list1.head_node) #-> Node: 2, which points to: Node: 4, which points to: Node: 5, which points to: None
print(linked_list1.length) #-> 3
print(linked_list1.get(2)) #-> Node 2
print(linked_list1.get(4)) #-> Node 4
