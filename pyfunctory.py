"""
ATOMS

"""



"""
NUGGETS

"""



"""
UTILITIES

"""



"""
FACTORIES

Higher-order functions for the creation of other functions, 
generators and larger program flow sequences.

"""

def compose(*funcs):
    def inner(data, funcs=funcs):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner
