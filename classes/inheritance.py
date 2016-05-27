"""
Notes: =========================================================================
Notes: class ClassName[(baseclass)]:
Notes:  Ex:     class Dog(Animal):
Notes: 
Notes: When executed as standalone script, __name__ == "__main__".
Notes: When imported from different file,  __name__ == "<filename without .py>"
Notes: 
"""

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "\"Pet class object with name " + self.name +\
               " and age " + str(self.age) + "\""

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Pet):
    def __init__(self, name, age):
        Pet.__init__(self, name, age)

    def __str__(self):
        return "\"Dog class object with name " + self.name +\
               " and age " + str(self.age) + "\""

#    def talk(self):
#        return "wooof wooof"

class Cat(Pet):
    def __init__(self, name, age):
        Pet.__init__(self, name, age)

    def __str__(self):
        return "\"Cat class object with name " + self.name +\
               " and age " + str(self.age) + "\""

    def talk(self):
        return "meow meow"


class MultiClass(Cat, Dog):
    # uses depth-first algorim for searching attributes/methods.
    pass

#===============================================================================
def Main():
    myPet = Pet("Pet", 5)
    myCat = Cat("Pussy", 3)
    myDog = Dog("Puppy", 1)
    
    # String representation for a class.
    print "myPet is", str(myPet)
    print "myDog is", str(myDog)
    print ""
 
    # Check Inheritance.
    print "Is myPet a Pet? ", isinstance(myPet, Pet)
    print "Is myPet a Dog? ", isinstance(myPet, Dog)
    print "Is myDog a Pet? ", isinstance(myDog, Pet)
    print "Is myDog a Dog? ", isinstance(myDog, Dog)
    print ""

    # Check Subclass.
    print "Is Dog a subclass of Pet? ", issubclass(Dog, Pet)
    print "Is Pet a subclass of Dog? ", issubclass(Pet, Dog)
    print "Is Cat a subclass of Pet? ", issubclass(Cat, Pet)
    print "Is Pet a subclass of Dog? ", issubclass(Pet, Dog)
    print ""

    print "myCat talk as", myCat.talk()

    try:
        print "myDog talk as", myDog.talk()
    except NotImplementedError as e:
        print "NotImplementedError : ", e.args


#===============================================================================
# When executed as standalone script, __name__ == "__main__".
# When imported from different file, __name__ == "<filename>"
#
if __name__ == "__main__":
    Main()
