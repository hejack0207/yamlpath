import unittest
from .keypath import *

class TestKeypath(unittest.TestCase):
    def setup(self):
        pass

    def test_yaml(self):
        paths = keypaths('''version: '2'

services:
    generator:
        x''', 5,9)
        print "keypath:"+"/".join(paths)

    def test_yaml3(self):
        paths = keypaths('''version: '2'

services:
    generator:
        x:
            - x1
            - x2
            - x3: 
                y: "abc"''', 4,9)
        print "keypath:"+"/".join(paths)

    def test_yaml2(self):
        paths = keypaths('''version '2'
x''', 2,1)
        print "keypath:"+"/".join(paths)

if __name__ == "__main__":
    unittest.main()
