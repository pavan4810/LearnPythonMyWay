class Dog():
  """Dog class """

  kind = "canine"
  tricks = []

  def __init__(self,name):
    self.name = name

  def add_trick(self, trick):
    self.tricks.append(trick)

a = Dog('puppy')
b = Dog('scooby')

print "a.kind = ", a.kind
print "b.kind = ", b.kind

a.kind = "Testing"

print "a.kind = ", a.kind
print "b.kind = ", b.kind

a.add_trick('roll over')
b.add_trick('play dead')

print a.tricks
