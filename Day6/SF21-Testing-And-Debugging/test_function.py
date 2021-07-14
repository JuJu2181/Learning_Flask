import pytest
import sys
from function import *

# @pytest.mark.number
#@pytest.mark.skip(reason="It is obvious. No need to check it")
def test_add():
    assert add(2,3) == 5
    assert add(1, -1) == 0
    assert add(-1, -1) == -2
    assert add(1.5, -1) == 0.5

# @pytest.mark.number
#@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python 3.8 or higher")
def test_product():
    assert product(2,3) == 6
    assert product(2,-3) == -6
    assert product(-2,-3) == 6
    assert product(0.5,0.5) == 0.25

# @pytest.mark.number
def test_division():
    assert division(8,2) == 4
    assert division(18,-3) == -6
    assert division(-64,-4) == 16
    assert division(5,2) == 2.5
    assert division(10,2.5) == 4

# @pytest.mark.number
def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        division(9, 0)

# @pytest.mark.string
def test_add_string():
    f_value =  add('Software', ' Fellowship')
    assert f_value == 'Software Fellowship'
    assert type(f_value) is str
    assert 'Software' in f_value

# @pytest.mark.string
def test_product_string():
    f_value =  product('Locus', 3)
    assert f_value == 'LocusLocusLocus'
    assert type(f_value) is str
    assert 'Locus' in f_value


# @pytest.mark.parametrize('num1, num2, result',
#                         [
#                             (2 ,3, 5),
#                             (1, -1, 0),
#                             (-1, -1, -2),
#                             (1.5, -1, 0.5)
#                         ]
#                         )
# def test_add(num1, num2, result):
#     assert add(num1, num2) == result
