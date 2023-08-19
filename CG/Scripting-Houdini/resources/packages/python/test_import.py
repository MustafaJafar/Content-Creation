""" Test Import Module. 

This module was made to test importing custom scripts.
you can test in houdini as follows: 
1. create "python" Node and add this code:

from test_import import test
test()

"""


def test () : 
    print("This is printed from python external library\n")