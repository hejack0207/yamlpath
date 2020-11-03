import unittest
#  import os,sys
#  sys.path += [os.path.abspath("../src")]
from yamlpath.keypath import *

class TestKeypath(unittest.TestCase):

    def test_yaml(self):
#2345678901234567890
        data = '''
version: '2'

services:
    generator:
        image: nginx
        ports:
            - 80
            - 8080

     consumer:
      build: .
      file: Dockerfile

networks:
    - frontend
    - backend
'''
#2345678901234567890
        assert keypaths(data, 2, 1) == ['version']
        assert keypaths(data, 2, 8) == ['version']
        assert keypaths(data, 2, 9) == ['version']
        assert keypaths(data, 2, 13) == ['version']
        assert keypaths(data, 2, 14) == ['version']
        assert keypaths(data, 3, 1) == ['version']
        assert keypaths(data, 4, 8) == ['version']

        assert keypaths(data, 4, 9) == ['services']
        assert keypaths(data, 6, 14) == ['services','generator', 'image']
        assert keypaths(data, 7, 9) == ['services','generator', 'image']
        assert keypaths(data, 7, 14) == ['services','generator', 'ports']
        assert keypaths(data, 8, 14) == ['services','generator', 'ports']

        assert keypaths(data, 11, 13) == ['services','consumer']
        assert keypaths(data, 12, 9) == ['services','consumer', 'build']
        assert keypaths(data, 13, 13) == ['services','consumer', 'file']

if __name__ == "__main__":
    unittest.main()
