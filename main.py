"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    ### TODO
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return binary2int(x.binary_vec + y.binary_vec)

    x_padded, y_padded = pad(x.binary_vec, y.binary_vec)

    x_left, x_right = split_number(x_padded.binary_vec)
    y_left, y_right = split_number(y_padded.binary_vec)

    z2 = _quadratic_multiply(x_left, y_left)  
    z1 = _quadratic_multiply(x_left, y_right) 
    z0 = _quadratic_multiply(x_right, y_left) 
    z0_and_z1 = _quadratic_multiply(x_right, y_right)

    z2 = bit_shift(z2, len(x_left) * 2)
    z1 = bit_shift(z1, len(x_left))
    z0 = bit_shift(z0, len(x_right))

    result = z2.decimal_val + z1.decimal_val + z0.decimal_val
    return binary2int(list(bin(result)[2:]))
    ###


    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000


    
    

