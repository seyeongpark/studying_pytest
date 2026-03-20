#tests/test_mycalc.py

from apps.mycalc import add
from apps.mycalc import substract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 3.5) == 6.0
    
def test_add_positive_numbers():
    a = 12
    b = 3
    expect = 15
    
    actual = add(a,b)
    assert expect == actual
    
def test_add_negative_numbers():
    a = -5
    b = -10
    expect = -15
    
    actual = add(a,b)
    assert expect == actual

def test_subsctract():
    assert substract(5, 2) == 3
    assert substract(0, 5) == -5
    assert substract(4, -3) == 7  
    
'''def test_fail_example():
    assert add(1, '2') == 3'''
    