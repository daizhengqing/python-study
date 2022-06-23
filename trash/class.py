# @classmethod和@staticmethod
# 实例方法、类方法和静态方法的区别
print('---实例方法、类方法和静态方法的区别---')
class A(object):
  data = 10

  def __init__(self):
    self.a = 0

  # 实例方法
  def method(self):
    print(self.staticMethod)
    self.a += 1

  # 类方法
  @classmethod
  def classMethod(cls):
    print(cls.staticMethod)
    print(cls)
    return 2

  #静态方法
  @staticmethod
  def staticMethod():
    return 3

# print(A.method())
# print(A.classMethod())
# print(A.staticMethod())

a = A()
b = A()
a.method()
A.classMethod()

# A.data += 1
# a.data += 1
# print(id(A.data), id(a.data))
# A.data += 1
# a.data += 10
# print(A.data, a.data)
# print(dir(a))
# print(a.__class__.data)

# A.data += 1
# a.data += 1

# print(A.data)
# print(a.data)

# a.data += 1

# print(a.method())
# print(a.classMethod())
# print(a.staticMethod())

print('---实例变量和类变量---')
# 实例变量和类变量
class B:
  a = 0

  def __init__(self):
    B.a += 1
    self.b = 1

print(B.a)
ba = B()
print(ba.a, ba.b)
bb = B()
print(bb.a, bb.b)