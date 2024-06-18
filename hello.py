import gl

# 这是一个中文注释
if __name__ == '__main__':
    print("hello world")

# 1 python中的变量不需要声明，变量的赋值操作即是变量声明和定义的过程。
# 2 python中一次新的赋值，将创建一个新的变量。即是变量的名称相同，变量的标识并不相同。用id()函数可以获取变量标识：
x = 1
print(id(x))
x = 2
print(id(x))


# 6 也可以把全局变量放到一个专门的文件中，然后通过import来引用：
def fun():
    print(gl._a)
    print(gl._b)


fun()

# 1 条件语句：
x = 2
if x == 1:
    print("a")
else:
    print("b")

# 2 条件语句：
x = 4
if x == 1:
    print("a")
elif x == 2:
    print("b")
elif x == 3:
    print("c")
else:
    print("d")

# 3 条件嵌套：
x = 8
if x <= 10:
    if x == 11:
        print("aa")
    else:
        print("ab")
elif x <= 20:
    print("b")
elif x <= 30:
    print("c")
else:
    print("d")

# 5 循环语句：
x = 0
while x < 5:
    x += 1
    print(x)
else:
    print("while loop over")

# 6 循环语句：
arr = ["apple", "banana", "grape", "orange"]
for cur in arr:
    print(cur)
else:
    print("for loop over")

# 7 python不支持类似c的for(i=0;i<5;i++)这样的循环语句，但可以借助range模拟
for x in range(0, 5, 2):
    print(x)

# 1 元组(tuple)：python中一种内置的数据结构。元组由不同的元素组成，每个元素可以存储不同类型的数据，如字符串、数字甚至元素。
# 元组是写保护的，即元组创建之后不能再修改。元组往往代表一行数据，而元组中的元素代表不同的数据项。可以把元组看做不可修改的数组。
tuple_name = ("apple", "banana", "grape", "orange")

# 2 列表(list)：列表和元组相似，也由一组元素组成，列表可以实现添加、删除和查找操作，元素的值可以被修改。列表是传统意义上的数组。
list = ["apple", "banana", "grape", "orange"]
# 可以使用append方法来在尾部追加元素，使用remove来删除元素。
list.append("cherry")
list.remove("apple")

# 3 字典(dictionary)：由键-值对组成的集合，字典中的值通过键来引用。键和值之间用冒号隔开，键-值对之间用逗号隔开，并且被包含在一对花括号中。
dict2 = {"a": "apple", "b": "banana", "g": "grape", "o": "orange"}


# 6 函数定义
def arithmetic(x, y, operator):
    result = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y
    }
    return result[operator]


print(arithmetic(4, 5, "*"))

# 1 格式化输出：
format2 = "%s%d" % ("abc", 1.23)
print(format2)

# 2 用+进行字符串的合并：
str1 = "hello"
str2 = "world"
result = str1 + " " + str2
print(result)

# 4 通过切片截取字符串：
word = "world"
print(word[0:3])

# 1 简单处理文件：
context = "hello,world"
f = open("hello.txt", 'w')
f.write(context)
f.close()


# 类的定义
class Fruit:
    @staticmethod
    def grow():
        print("Fruit grow")


fruit = Fruit()
fruit.grow()


# 类的继承
class Apple(Fruit):
    @staticmethod
    def flower():
        print("Apple flower")


apple = Apple()
apple.grow()
apple.flower()
