# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


'''
# print('hello world')
# print('the quick brown fox','jumps over','the lazy dog')
# print(300)
# print(100+200)
# print('100 + 200 =',100 + 200)
#

# # input
# name = input()
#
# print(name)

name = input('please enter your name: ')
print('hello',name)
'''


# # 转义字符
# print('i\'m ok.')
# 
# print('i \'m learning \n python.')
# 
# print('\\\n\\')
# 
# # r'' 表示''内部字符不转译
# 
# print('\\\t\\')
# 
# print(r'\\\t\\')
#
# # '''...''' 可以表示多行内容
# 
# print('''line1
# ... line2
# ... line3
#
#
# )
#
# print('''
#      line1
#      line2
#      line3''')


# list
#
# classmates = ['Michael','bob','tracy']      #一个list
# print(classmates)
#
# print(len(classmates))                            #len 用来查看list 元素个数
#
# print(classmates[0])                              #计数从0开始，-1可以表示最后一个数
# print(classmates[-1])
# print(classmates[-2])
#
# #在list 中追加元素到末尾
# classmates.append('Adam')
# print(classmates)
#
# #把元素插入指定位置
# classmates.insert(1,'jack')
# print(classmates)
#
# #删除list末尾元素，用pop（）方法；
# classmates.pop()
#
# #删除list指定位置元素，用pop（i）方法；
# classmates.pop(1)
#
#
# #替换元素
# classmates[1] = 'sarah'
#
# #list 中元素类型可以不同
# L = ['apple',123,True]
#
# #list可以是另一个list
# s = ['python','java',['asp','php'],'scheme']
# len(s)                  #个数为4
#
# # S 可拆分为两个list
# p = ['asp','php']
# s = ['python','java', p,'scheme']       #要拿到'php'可以写成p[1]或者s[2][1]  s可以看成是一个二维数组，类似的还有三维、四维……数组

#tuple

classmates = ('Michael','Bob','tracy')              # 一个tuple   a = ()   #空元组   b = (1)   #数字   c = [2]   #列表   d = (3,)   #元组  e = (4,5,6)#元组



# 条件判断
# if 语句
# age = 20
# if age >= 18:
#     print('your age is',age)
#     print('adult')
# else:
#     print('your age is',age)
#     print('teenager')

# elif
# age = 3
# if age >= 18:
#     print('adult')
# elif age >=6 :
#     print('teenager')
# else:
#     print('kid')


# input
#
# birth = input('birth:')
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
# # 由于input 输入为str 类型 所以要转换成整数类型来比较，
# s = input('birth:')
# birth = int(s)
# if birth <2000:
#     print('00前')
# else:
#     print('00后')
#



# 循环
#for 循环
# names = ['Michael','bob','tracy']
# for name in names:
#     print(name)

# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)

list (range(5))

sum = 0
for x in range (101):
    sum = sum +x
print(sum)

#while 循环

sum = 0
n = 99
while n >0 :
    sum= sum +n
    n = n-2
print(sum)


