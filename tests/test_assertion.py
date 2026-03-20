# tests/test_assertion.py
import pytest
from apps.mycalc import divide

def test_various_assertions():
    # true/false assertions
    assert True
    assert [1, 2, 3]
    assert not []
    assert "hello"
    assert " "
    assert False == 0
    assert True == 1
    
# comparison assertions
    assert 4 > 2
    assert 5 >= 5
    assert 3 < 10
    assert 2 <= 2
    assert 5 == 5
    assert 5 != 3
    
# membership assertions
    assert "pytest" in "I love pytest"
    assert "test" not in "I love popcorn"
    assert 3 in [1, 2, 3, 4, 5]
    assert 10 not in [1, 2, 3, 4, 5]
    assert "a" in {"a": 1, "b": 2}
    assert "c" not in {"a": 1, "bc": 2}
    
#sameness assertions
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    assert a == b
    '''assert a is b # False, because a and b are different objects in memory  '''
    assert a is c # True, because c references the same object as a
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert (1/3) == pytest.approx(0.3333333, abs=0.0000001)
    
def test_float_approx():
    result = divide(1,3)
    
    assert result == pytest.approx(0.33333, abs=3.4e-3)
    # |실제값 - 예상한값| / 예상한값 -> 1.1e-5
    assert result == pytest.approx(0.33333, rel=1.1e-5) #rel은 상대오차, abs는 절대오차
    
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
        
def test_divide_wrong_type_raises_exception():
    with pytest.raises(ValueError):
        divide(10, "2")
        
# warnings assertions
import warnings

def function_that_warns():
    warnings.warn("This is a warning message.", DeprecationWarning)
    print("Function executed with a warning.")
    return True

def test_deprecation_warning():
    with pytest.warns(DeprecationWarning):
        function_that_warns()
        
