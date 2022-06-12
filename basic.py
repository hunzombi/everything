class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def add_vector(self, vec):
    return Vector(self.x + vec.x, self.y + vec.y)
