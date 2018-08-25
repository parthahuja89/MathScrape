dictionary = []
# recognized vars
dictionary.append('x')
dictionary.append('y')
dictionary.append('z')
dictionary.append('a')
dictionary.append('b')
dictionary.append('c')

# recognized expressions

dictionary.append('(')
dictionary.append(')')
dictionary.append('=')
dictionary.append('<')
dictionary.append('>')
dictionary.append('+')
dictionary.append('^')
dictionary.append('{')
dictionary.append('}')
dictionary.append('/')
dictionary.append('-')
dictionary.append('sqrt')

#
def cleaner(expression):

    ex = list(expression)
    cleaned = []

    for e in ex:
        if(isSqrt(e,ex)):
            cleaned.append('sqrt')
        if(isOver(e,ex)):
           currentidx = ex.index(e)
           cleaned.__add__(')', currentidx-1)
           cleaned.__add__("(", 0)
        if (e in dictionary or e.isdigit()):
            cleaned.append(e)

    return cleaned

def isSqrt( current,arr):
    if (current == 's'):
        currentidx = arr.index(current)
        nextidx = currentidx + 1
        if (arr.__getitem__(nextidx) == 'q'):
            return True


def isOver(current, arr):
    if(current =='o'):
        currentidx = arr.index(current)
        nextidx = currentidx + 1
        if (arr.__getitem__(nextidx) == 'v'):
            return True

if __name__ == "__main__":
    e = '{-b\pm\sqrt{b^2-4ac} \over 2a}. '
    print('original string:' + e)
    cleaner(e)
    cleaned_string = ''.join(map(str, cleaner(e)))
    print(cleaned_string)
