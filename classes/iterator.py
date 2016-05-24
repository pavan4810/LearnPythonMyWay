"""
Notes: =========================================================================
Notes: Define __iter__() and next() for iteration over class object
Notes: 
Notes: __iter__()     for     iterator
Notes: next()
Notes: 
"""

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(self.data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


#===============================================================================
def Main(): 
    rev = Reverse("Pavan Kumar Avala")
    for char in rev:
        print char,


#===============================================================================
if __name__ == "__main__":
    Main()
