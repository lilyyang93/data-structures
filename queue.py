class Queue:
  def __init__(self):
    self.total = 0
    self.queue = []
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue.append(data)
    self.total += 1
    return self.queue

  def dequeue(self):
    # write your code to remove the data to the Queue following FIFO and return the Queue
    self.queue.remove(self.queue[0])
    self.total -= 1
    return self.queue

  def size(self):
    # write your code that returns the size of the Queue
    return self.total

q1 = Queue() #initialize q1 variable
q1.enqueue(2) #add 2 to the queue
q1.enqueue(4) #add 4 to the queue 
q1.enqueue(6) #add 6 to the queue 
print(q1.queue) #-> [2, 4, 6]
q1.dequeue() #remove the element that was first inputted 
print(q1.queue) #-> [4, 6]
print(q1.size()) #-> 2 (length of queue after adding 3 elements then removing 1 element is now 2)

