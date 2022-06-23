def a ():
  return 233

print(a)

def b (cb):
  print(cb)
  print(id(cb), id(a))

b(a)