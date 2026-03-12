import numpy as np
import matplotlib.pyplot as plt
import math


def add(x,y):
  return x + y
def subtract(x,y):
  return x - y
def multiply(x,y):
  return x * y
def divide(x,y):
  return x / y
def sq(x,y):
  return(math.sqrt(x))

while True:
    operation = int(input("Enter the operation you wish to perform: 1 = ADDITION, 2 = SUBTRACTION, 3 = MULTIPLICATION, 4 = DIVISION, 5 = SQUARE ROOT, 6 = PLOT A FUNCTION, 7 = EXPONENTIAL, 8 = LOGARITHM"))
    if operation in [1, 2, 3, 4, 5, 6]:
      break
    print("Invalid input. Please enter a number between 1 and 8.")

if operation == 1:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  print(num1, "+", num2, "=", add(num1,num2))
elif operation == 2:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  print(num1, "-", num2, "=", subtract(num1,num2))
elif operation == 3:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  print(num1, "*", num2, "=", multiply(num1,num2))
elif operation == 4:  
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  print(num1, "/", num2, "=", divide(num1,num2))
elif operation == 5:
  num1 = float(input("Enter number: "))
  print("Square root of", num1, "=", sq(num1))
elif operation == 6:
  func = input("Enter the function you wish to plot (e.g. 'x**2' for x squared): ")
  x = np.linspace(-10, 10, 100)
  y = eval(func)
  plt.plot(x, y)
  plt.title("Plot of " + func)
  plt.xlabel("x")
  plt.ylabel("y")
  plt.grid()
  plt.show()
elif operation == 7:
  base = float(input("Enter the base: "))
  exponent = float(input("Enter the exponent: "))
  print(base, "raised to the power of", exponent, "=", base ** exponent)
elif operation == 8:
  num = float(input("Enter the number: "))
  print("Logarithm of", num, "=", math.log(num))