print('---什么自省---')
# 什么自省
# 就是python在运行时能自动推断出变量的类型并获取
a: list = [1,2,3]
b = [1,2,3]
print(type(a))
print(type(b))

print('---_a、__a和__a__有什么区别---')
# _a、__a和__a__有什么区别
# _a
_a = 1
# run test.py
# import other的时候_a会包含在other中
# from other import *的时候，_a不会被import

#__a
class A:
  _a = 666
  __a  = 233
print(dir(A))
print(A._a)
print(A._A__a)
# 在class中 __开头的对象会被改编，名字前缀会加上_类名,其目的是防止命名冲突

# __a__
# 双下划线开头结尾的是python的内置对象
# python推荐不要用使用这样的命名方式应用在自定义的变量函数等


print('---python格式化字符有哪些方式---')
# python格式化字符有哪些方式
# 有三种方式%操作符, format, f-string
# %操作符
a = 'Hello, %s' % 'PP'
b = 'Hello, %s & %d' % ('PP', 222)
c = 'Hello, %(a)s & %(b)s' % { 'a': 'KD', 'b': 'BM' }
print(a)
print(b)
print(c)

# format函数
# 性能不如%操作符和f-string
a = 'Hello, {0}'.format('IO')
b = 'Hello, {name}'.format(name="LK")

# 比%操作符更灵活
c = 'Hell0, {0}, {1}, {2}, {0}'.format(*[11,22,33])
print(a)
print(b)
print(c)

# format是一个函数，可以直接作为参数传给其他函数
li = [12,45,78,784,2,69,1254,4785,984]
print('\n'.join(map('the number is {}'.format, li)))

#f-string
# 书写简单，可读性强
name = 233
a = f'Hello, {name}'


print('is 和 == 有什么区别')
# is 和 == 有什么区别