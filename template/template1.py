"""
Notes: =========================================================================
Notes: Template class from string module can be used for creating templates.
Notes:      from string import Template
Notes:
Notes: Default delimiter is "$". It can be changed.
Notes: {} braces for placeholder
Notes:
"""

from string import Template

class MyTemplate(Template):
    delimiter = "#"

def Main():
    cart = []
    cart.append(dict(Item="Burger", Price=4, Qty=2))
    cart.append(dict(Item="Wings", Price=5, Qty=8))
    cart.append(dict(Item="Iced Tea", Price=3, Qty=1))
    cart.append(dict(Item="Coke Float", Price=2, Qty=1))

    t = Template("$Qty * $Item  = $Price")
    for data in cart:
        print t.substitute(data)
    print ""
        

    # Using Safe substitute and not defining $Sr
    t = Template("$Sr $Qty * $Item  = $Price")
    for data in cart:
        print t.safe_substitute(data)
    print ""
        

    # Changed Delimiter
    t = MyTemplate("#Qty * #Item  = #Price")
    for data in cart:
        print t.substitute(data)
    print ""
        

    cart = []
    cart.append(dict(Item="Ham", Price=4, Qty=2))
    cart.append(dict(Item="Fish", Price=5, Qty=8))
    cart.append(dict(Item="Chicken", Price=3, Qty=8))
    # Using {} braces for placeholder
    t = Template("$Qty * ${Item}burger  = $Price")
    for data in cart:
        print t.safe_substitute(data)
        

#===============================================================================
if __name__ == "__main__":
    Main()
