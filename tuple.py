#有序列表tuple，一旦被初始化，就不能被修改
classmates=('A','B','C','G')
print(classmates)
#注意，定义tulpe中单个元素必须加，
t=(2,)
print(t)
#理解tuple的不可变
s=('a','c',['A','C'])
print(s)
s[2][0]='X'
print(s)