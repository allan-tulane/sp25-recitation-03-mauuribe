from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert quadratic_multiply(BinaryNumber(6), BinaryNumber(5)) == 6*5
    assert quadratic_multiply(BinaryNumber(14), BinaryNumber(10)) == 14*10
    assert quadratic_multiply(BinaryNumber(27), BinaryNumber(5)) == 27*5
    assert quadratic_multiply(BinaryNumber(11), BinaryNumber(3)) == 11*3
