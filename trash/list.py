class List(list):
  def __init__(self, data) -> None:
    self.extend(data)

  # 第一个item
  @property
  def head (self):
    return self[0]

  #最后一个item
  @property
  def last (self):
    return self[len(self) - 1]
  
  # 查询第一个满足条件的item
  def find (self, callback):
    for index in range(len(self)):
      item = self[index]
      if callback(item, index):
        return item
  
  # 查询所有满足条件的item
  def findAll (self, callback):
    res = []
    for index in range(len(self)):
      item = self[index]
      if callback(item, index):
        res.append(item)
    return res

  # 查询满足条件的第一个item的index
  def findIndex (self, callback):
    for index in range(len(self)):
      item = self[index]
      if callback(item, index):
        return index
  
  # 是否包括某个item
  def includes (self, target):
    return self.find(lambda x, *args: x == target) != None

  # 是否有一个满足条件
  def some (self, callback):
    for index in range(len(self)):
      item = self[index]
      if callback(item, index) == True:
        return True
    return False

  # 是否全部满足条件
  def every (self, callback):
    for index in range(len(self)):
      item = self[index]
      if callback(item, index) == False:
        return False
    return True

s = List([1,2,3])
print(s.head)
print(s.last)
print(s.find(lambda x, *args: x == 2))
print(s.findAll(lambda x, *args: x > 1))
print(s.includes(2))
print(s.includes(90))
print(s.some(lambda x, *args: x > 3))
print(s.some(lambda x, *args: x < 2))
print(s.every(lambda x, *args: x < 2))
print(s.every(lambda x, *args: x > 0))

