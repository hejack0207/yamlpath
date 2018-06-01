#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from yamlpath.skeleton import fib
from yamlpath.keypath import *

__author__ = "hejack0207"
__copyright__ = "hejack0207"
__license__ = "mit"


def test_fib():
    assert 1 == 1
    with pytest.raises(AssertionError):
        1 != 1

def test_yaml():
    paths = keypaths('''version: '2'

services:
generator:
    x''', 5,9)
    print "keypath:"+"/".join(paths)

def test_yaml3():
    paths = keypaths('''version: '2'

services:
generator:
    x:
        - x1
        - x2
        - x3: 
            y: "abc"''', 4,9)
    print "keypath:"+"/".join(paths)

def test_yaml2():
    paths = keypaths('''version '2'
x''', 2,1)
    print "keypath:"+"/".join(paths)
