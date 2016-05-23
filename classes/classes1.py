"""
Notes: =========================================================================
Notes: class ClassName[(baseclass)]:
Notes:      class Dog:
Notes:      class Dog(Animal):
Notes:
Notes: Mutable (lists and dictionaries) objects will be shared across.
"""

class Dog:
  """Dog class """

  kind = "canine"
  tricks = []

  def __init__(self,name):
    self.name = name
    # Create new mutable oject during initialization.
    self.tricks2 = []

  def add_trick(self, trick):
    self.tricks.append(trick)

  def add_trick2(self, trick):
    self.tricks2.append(trick)


#===============================================================================
# A and B don't share "kind" attribute, but share "tricks" attribute (because
# it is mutable object)
#
a = Dog('puppy')
b = Dog('scooby')

print "a.kind = ", a.kind
print "b.kind = ", b.kind

a.kind = "Testing"

print "a.kind = ", a.kind
print "b.kind = ", b.kind


#===============================================================================
# A and B don't share "kind" attribute, but share "tricks" attribute (because
# it is mutable object)
#
a.add_trick('roll over')
b.add_trick('play dead')

print a.tricks


#===============================================================================
# Create new mutable oject during initialization.
#
a.add_trick2('roll over')
b.add_trick2('play dead')

print a.tricks2
