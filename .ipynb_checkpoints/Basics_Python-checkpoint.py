import numpy as np

#Q4
x = input("Enter a float string: ")
x_float = float(x)
print("Converted to float: ",x_float,type(x_float))

#Q5
print("The powers of 2 from 2^1 to 2^8")
for i in range(1,9):
    print(2**i)

#Q6
exponent = int(input("Enter the exponent integer: "))
print("2 raised to the power of ",exponent," is ",2**exponent)

#Q7
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
smallest_index = numbers.index(min(numbers))
print(f"The index of the smallest number is: {smallest_index}")

#Q8


#Q9
num1 = float(input("Enter first float num: "))
num2 = float(input("Enter second float num: "))
ans = int(num1/num2)
print("The ans in integer form is ",ans)

#Q10
arr = np.random.rand()
print(arr)

#Q11
arr = np.linspace(0,1,20)
print(arr)

#Q12
arr = np.arange(1,26).reshape(5,5)
print(arr)
print("The sum of columns: ")
print(arr.sum(axis=0))
print("The sum of rows: ")
print(arr.sum(axis=1))