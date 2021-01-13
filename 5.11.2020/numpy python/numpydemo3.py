# Python program to demonstrate
# basic operations on single array
import numpy as np
 
# Defining Array 1
a = np.array(
    [
              [1, 2],
              [3, 4]
    ]
)
 
# Defining Array 2
b = np.array(
    [
              [4, 3],
              [2, 1]
    ]
)
               
# Adding 1 to every element
a=a + 1
print ("Adding 1 to every element:\n", a)
 
# Subtracting 2 from each element
b=b-2
print ("\nSubtracting 2 from each element:\n", b)
 
# sum of array elements
# Performing Unary operations
print ("\nSum of all array "
       "elements: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray sum:\n", a + b)
print ("\nArray subtract:\n", a - b)
print ("\nMultiplication:\n", np.multiply(a,b))
print ("\nMultiplication:\n", a*b)
print ("\nMatrix Multiplication:\n", np.matmul(a,b))
print ("\nInverse of matrix a:\n", np.linalg.inv(a))
print ("\nTranspose :\n", a.transpose())


