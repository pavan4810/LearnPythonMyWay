"""
Notes:
Notes: string.split(separator character within single or double quotes)
Notes:   Ex:  sentense.split(' '), sentense.split(" "), sentense.split('/')
"""

def split_sentense(sentense, separator):
    """ This function breaks senses into words. """
    return sentense.split(separator)

string = "Pavan Kumar Avala"
print split_sentense(string, ' ')

string = "Pavan Kumar Avala"
print split_sentense(string, " ")

string = "Pavan Kumar,Avala"
print split_sentense(string, ',')

string = "Pavan Kumar/Avala"
print split_sentense(string, '/')

string = "Pavan Kumar\Avala"
print split_sentense(string, '\\')

string = "Pavan Kumar'Avala"
print split_sentense(string, '\'')

string = 'Pavan Kumar"Avala'
print split_sentense(string, "\"")
