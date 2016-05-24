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

     
#===============================================================================
if __name__ == "__main__":
    Main()
