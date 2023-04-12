import numpy as np

# Method 1
data = [[1,2,3], [4,5,6]]
numpy_data = np.array(data)
print("Numpy Array Using Array Function is :\n" , numpy_data)

#Method 2
numpy_zero = np.zeros((1,3))
print("Numpy Array of Zeros is :" , numpy_zero)

#Method 3
numpy_ones = np.ones((1,3))
print("Numpy Array of Ones is :" , numpy_ones)

#Method 4
numpy_arr = np.arange(5)
print("Numpy Array using Arange :" , numpy_arr)


# Changing the DataType of NumPy Arrays
string_arr = np.array(['1.24','1.0','3.56'],dtype=np.string_)
print("\nThe array :", string_arr, " has datatype ", string_arr.dtype)
float_arr = string_arr.astype(float)
print("Now, The array :", float_arr, " has datatype ", float_arr.dtype)

#Performing Arithmetic with NumPy Array
num_arr = np.arange(5)
print("The original array is ", num_arr)
print("Multiplying Array with 2 " , num_arr*2)
print("Addding 5 to original Array Elements" , num_arr + 5)
