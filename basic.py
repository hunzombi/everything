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
