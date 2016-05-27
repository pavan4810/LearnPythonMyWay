"""
Notes: =========================================================================
Notes: Generator function (with yield) and generator expression
Notes: 
"""

def Reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

#===============================================================================
def Main(): 
    # Generator function.
    rev = Reverse("Pavan Kumar Avala")
    for char in rev:
        print char,
    print ""

    # Generator expression.
    data = "Pavan Kumar Avala"


    # Following creates list
    print [data[i] for i in range(len(data)-1, -1, -1)]
    print list(data[i] for i in range(len(data)-1, -1, -1))

    # Following creates set
    print {data[i] for i in range(len(data)-1, -1, -1)}

    # Following creates dictionary
    print {i:data[i] for i in range(len(data)-1, -1, -1)}

    data = ["Pavan", "Kumar", "Avala"]
    print [data[i][j] for i in range(len(data)-1, -1, -1)  for j in range(len(data[i])-1, -1, -1)]

    # zip takes one value from each argument 
    xvec = [10, 20, 30]
    yvec = [7, 5, 3]
    print [x*y for x,y in zip(xvec, yvec)]
    print sum(x*y for x,y in zip(xvec, yvec))         # dot product


#===============================================================================
if __name__ == "__main__":
    Main()
