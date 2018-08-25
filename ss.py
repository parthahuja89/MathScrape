from sympy import *
from sympy.abc import _clash1
equation = 'x/2-4'

#classification

trig = []
trig.append('sin')
trig.append('cos')
trig.append('tan')
trig.append('cot')
trig.append('cosec')
trig.append('sec')


def classification(equation):

  isTrig(equation)
  isLog(equation)




def isTrig(equation):
    for t in trig:
        if (t in equation):
            print('trigonometric function')
            return true

    else:
        return false

def isLog(equation):
    if ('log' in equation):
        print('logarthimic function')
        return true
    else:
        return false


#math functions
def simplify(eq):
    if(isLog(eq)):
        result = sympy.expand_log(equation)
        print(result)
    if(isTrig(eq)):
        result = sympy.trigsimp(equation)
        print(result)
        return result
    else:
        #possible polynominal *factor?
        sympy.simplify(equation)


def expand(e):
    if(isTrig(e)):
        result = sympy.expand_trig(e)
        print(result)
    if(isLog(e)):
        result = sympy.expand_log(e)
        print(result)
        return result
    else:
        result = sympy.expand(e)
        print(result)
        return result
#calculus

def differentiate(equation):
    return sympy.diff(equation)

def partial_Derivate(expression):
    #order: partial derivative order -> dxdydz -> x,y,z
   # print(sympify(expression))
    x = symbols('x')

    print(diff(equation), x)
    print(sympify(expression))
if __name__ == '__main__':
    classification(equation)
    partial_Derivate(equation)