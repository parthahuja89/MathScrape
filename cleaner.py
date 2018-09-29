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
    cleaned = list()

    for e in ex:

        if(isSqrt(e,ex)):
            cleaned.append('sqrt')
        if(isOver(e,ex)):
          #replace at first and move further
         cleaned.insert(0, '(')
         cleaned.append(')/')

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
    e = '{-b\pm\sqrt{b^2-4ac}\over2a}. '
    e2 = 'xhelloooooo^43+yhfe'
    print('original string:' + e2)
    cleaner(e2)
    cleaned_string = ''.join(map(str, cleaner(e2)))
    print(cleaned_string)
