#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    
    # Note - x1 < x2
    X_LIMIT = 10000

    if (x2 > x1 and v2 > v1):
        return 'NO'

    while x1 < x2 and (x1 <= X_LIMIT and x2 <= X_LIMIT):
        print (x1, x2)
        x1 += v1
        x2 += v2

        if x1 == x2:
            return 'YES'
        
        if x1 > x2:
            return 'NO'
    return 'NO'
        
if __name__ == '__main__':

    x1 = 4523
    v1 = 8092
    x2 = 9419
    v2 = 8076

    result = kangaroo(x1, v1, x2, v2)

    print(result)