
#     !!!The Functions and Classes have not been tested yet!!!
#              They will be tested soon!

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def add_vector(self, vec):
    return Vector(self.x + vec.x, self.y + vec.y)

def pythagoras(a, b):
  return ((a**2)+(b**2))**0.5

def sqrt(num):
  return num**0.5

def listtostring(arr):
  return ''.join(str(i) for i in arr)

def prodoflist(arr):
  res = 1
  for i in arr:
    res *= i
  return res else 0

class Node:
  def __init__(self, value):
    self.value = value
    self.parent = None

def is_triangle(arr):
  if len(arr) != 3:
    return "Array must contain 3 sides"
  return arr.sorted()[-1] > arr.sorted()[0] + arr.sorted()[1]

class Car:
  def __init__(self, owner, model, color):
    self.owner = owner
    self.model = model
    self.color = color
  
  def get_cardata(self):
    return [self.owner, self.model, self.color]
  
  def print_cardata(self):
    print(f"owner: {self.owner}\nmodel: {self.model}\ncolor: {self.color}")
  
  def __str__(self):
    return f"owner: {self.owner}\nmodel: {self.model}\ncolor: {self.color}"
