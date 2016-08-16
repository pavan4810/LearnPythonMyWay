class Queue():
  """List as Queue"""
  mylist = []

  def push(self, x):
    self.mylist.append(x)

  def pop(self):
    return self.mylist.pop(0)

  def printStack(self):
    print self.mylist


queue = Queue()
print queue.__doc__

queue.push(10)
queue.printStack()

queue.push(20)
queue.printStack()

queue.push(30)
queue.printStack()

print queue.pop()
queue.printStack()

print queue.pop()
queue.printStack()
