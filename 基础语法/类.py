class A:
  def list (self):
    return [1,2,3]

class B():
  def __init__ (self):
    self.extend(A)

  def update (self):
    self.data = 2

b = B()
print(dir(b))
print(b.list())
print(isinstance(b, A))