class Stack():
  """List as Stack"""
  mylist = []

  def push(self, x):
    self.mylist.append(x)

  def pop(self):
    return self.mylist.pop()

  def printStack(self):
    print self.mylist


stack = Stack()
print stack.__doc__

stack.push(10)
stack.printStack()

stack.push(20)
stack.printStack()

stack.push(30)
stack.printStack()

print stack.pop()
stack.printStack()

print stack.pop()
stack.printStack()
