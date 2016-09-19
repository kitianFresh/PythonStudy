#关于数据类型：
  亮点是动态类型的语言和shell脚本类似，也就是在运行过程中可以改变数据类型;

  这是C/C++ Java这种静态类型（编译时就确定了类型，且类型不可修改，如 int a = 5; a = "asd";是不允许的）的语言没有的

#关于字符编码：
  Python3在内存中的字符表示都采用了unicode编码；

  读取某种编码格式（ASCII UTF-8 GB2312）的源文件-->以unicode方式存入内存-->以某种编码方式写入磁盘或者网络;

  一个字符串技巧： 'c'\*n 表示'c'重复n次 当n = 3，则表示'ccc';

#Python2 和 Python3的字符串编码问题

##Python2
```python
>>> import sys
>>> sys.getdefaultencoding()
'ascii'
>>> str_byte = '田'
>>> type(str_byte)
<type 'str'>
>>> len(str_byte)
3
>>> str_byte
'\xe7\x94\xb0'
>>> repr(str_byte)
"'\\xe7\\x94\\xb0'"
>>> print(str_byte)
田
>>> str(str_byte)
'\xe7\x94\xb0'
>>> str_byte.__str__()
'\xe7\x94\xb0'
>>> 
>>> 
>>> str_byte.encode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
>>> 
>>> 
>>> str_b = b'田'
>>> type(str_b)
<type 'str'>
>>> len(str_b)
3
>>> str_b
'\xe7\x94\xb0'
>>> repr(str_b)
"'\\xe7\\x94\\xb0'"
>>> print(str_b)
田
>>> str(str_b)
'\xe7\x94\xb0'
>>> str_b.__str__()
'\xe7\x94\xb0'

```
在python2中，直接定义一个字符串字面量，他的类型是str，但这并不是逻辑意义上的字符串，因为很显然，按照程序逻辑上的意义，'田'的长度时1而不是3;
这说明python2中的str类型实际上是byte-string，也就是单纯的字节对象，并且按照字节数组处理而不是逻辑意义上的字符串处理;
为什么这里python内部存储的str\_byte的值是\xe7\x94\xb0,因为在你打出'田'字的时候，首先被输入法处理，此时输入法按照系统编码utf8来存储'田'即\xe7\x94\xb0,然后送给python2解释器，Python2解释器就会拿到字节数组[s, t, r, \_, b, y, t, e, ' ', =, ' ', \xe7, \x94, \xb0],然后进行语法解析，知道这是字符串赋值语句，并把str\_byte当成str对象来处理，内部存储为\xe7\x94\xb0;

另外，str\_byte本身其实会被解释为str(str\_byte),而str(object)这个built in function又调用object.\_\str\_\_()(当没有encoding和error参数的时候);

再来看print(str\_byte),print函数接受字节数组，然后按照系统默认编码打印出这个字符串，因为都是utf8，所以可以打印;

最后的str\_b的加b前缀的写法和不加前缀等价的;

```python
>>> str_unicode = u'田'
>>> type(str_unicode)
<type 'unicode'>
>>> len(str_unicode)
1
>>> str_unicode
u'\u7530'
>>> repr(str_unicode)
"u'\\u7530'"
>>> str(str_unicode)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\u7530' in position 0: ordinal not in range(128)
>>> print(str_unicode)
田
>>> str_unicode.__str__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\u7530' in position 0: ordinal not in range(128)

>>> reload(sys)
<module 'sys' (built-in)>
>>> sys.setdefaultencoding('utf-8')
>>> str(str_unicode)
'\xe7\x94\xb0'
```
我们发现在字符串字面量前面加上u前缀后，str\_unicode就是unicode类型，并且使用len()求长度也得到了正确的逻辑长度1;
可是在使用str(object)作用到str\_unicode时，结果尽然发生了ascii encode错误，这充分说明python2内部在做强制转换，将unicode类型转换成byte-string类型，并且采用了系统默认编码sys.getdefaultencoding()='ascii';党我们通过sys.setdefaultencoding设置成符合的utf8编码后，错误消失了，这说明我们推测正确;

这里显然是Python2解释器接读取到[s, t, r, \_, u, n, i, c, o, d, e, ' ', =, ' ', u, \xe7, \x94, \xb0],然后解析到u表明是要作为unicode存储，因此str\_unicode就存储成了Python2内部的Unicode码，也就是utf16，\u7530;

也就是说python2 内部的Unicode字符串才是符合程序逻辑意义的字符串;

```python
>>> print(str_unicode)
田
>>> print(str_unicode.encode('utf8'))
田
>>> print(str_unicode.encode('gbk'))
��
>>> type(str_unicode.encode('utf8'))
<type 'str'>
>>> type(str_unicode.encode('gbk'))
<type 'str'>
```
str\_unicode经过encode后，类型又是str了，并且当byte-string和实际默认编码不符合时，例如gbk和默认的utf8不符合，就会出现乱码了;

##Python3
```python
>>> str_byte = '田'
>>> type(str_byte)
<class 'str'>
>>> len(str_byte)
1
>>> str_byte
'田'
>>> repr(str_byte)
"'田'"
>>> print(str_byte)
田
>>> str(str_byte)
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 TypeError: 'bytes' object is not callable
>>> str_byte.__str__()
'田'
>>> import sys
>>> sys.getdefaultencoding()
'utf8'
>>> str_unicode = u'田'
>>> len(str_unicode)
1
>>> str_unicode
'田'
>>> repr(str_unicode)
"'田'"
>>> print(str_unicode)
田
>>> str(str_unicode)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> str_unicode.__str__()
'田'
>>> str_u = u'\u7530'
>>> str_u
'田'
>>> repr(str_u)
"'田'"
```
我们发现在Python3中，代码中书写的字符串字面常量都变成了class str类型，这个class str其实对应Python2中的type unicode类型，并且没有了str()函数可以调用;


```python
>>> str_b = b'田'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
>>> str_b = b'tian'
>>> type(str_b)
<class 'bytes'>
>>> str_b = b'\xe7\x94\xb0'
>>>len(str_b)
3
>>> str_b.decode('utf-8')
'田'
>>> type(str_b.decode('utf-8'))
<class 'str'>
>>> frame = bytearray()
>>> type(frame)
<class 'bytearray'>
>>> frame.append(0xe7)
>>> frame.append(0x94)
>>> frame.append(0xb0)
>>> frame.decode('utf-8')
'田'

```
那么Python2中的byte-string类型即type str在Python3中对应的是class bytes;不过，在Python3中，加b前缀的书写方式已经默认不能包含非ascii字符了;但是Python2和Python3都有bytearray类型;

最后，我们理清一下Python的字符串演进过程

演进过程：

×××××××××× | Python2 | Python3
:--------:|:--------: | :---------:
byte-string | type str  | class bytes
unicode-string | type unicode | class str
bytearray | type bytearray | class bytearray

书写方式：

××××××××| byte-string | unicode-string | bytearray
:-------:|:-----------:|:--------------:|:---------:
Python2 | 无前缀u | 加前缀u | bytearray()
Python3 | 加前缀b(只支持ascii) | 加或者不加u | bytearray()

实际上bytearray和byte-string等价;



#关于list []和tuple ()：
  list可以存储不同数据类型的元素（原因是Python是动态类型的语言啊），C++ Java中的List就不行;

  tuple是一旦初始化就不可改变的list，是一种安全的list；***注意的是，tuple的元素不变指的是元素的“指向”不变***；

#关于dict和set:
  其实就是hash，key为不可变对象；set是元素不重复的list,s = set([1,1,2,3,2]);

#关于函数：
  Python的函数可以返回任意多个返回值（实际上是返回一个tuple);

  参数传递灵活，有必选参数、默认参数、**可选参数(\*args) tuple**、关键字参数（\*\*kw）dict、命名关键字参数(\*做分隔符)可混用

#高级特性：
  切片：就是把集合进行划分的语法；L = list(range(10)) L[start:end] 特别要注意start和end可以为负数，有很多巧妙的切片操作
          eg：翻转一个字符串 s[::-1] 

  迭代：for ele in Iterable:

  列表生成器：[x\*x for x in range() if x]

  **生成器generator**：为了**动态生成列表从而节省内存**,一边循环一边计算,也即是说generator保存的是列表元素的生成算法;
  把[]改为()；g = (x\*x for x in range()) next(g)；复杂的算法可以用一个generator函数来完成，每一次next(g)执行就会到yeild

  可以直接作用于for循环的数据类型有以下几种：
  
  1. 一类是集合数据类型，如list、tuple、dict、set、str等；
  2. 一类是generator，包括生成器和带yield的generator function。
  3. 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
  
  迭代器：Iterable != Iterator,generator都是Iterator；Iterator是一个无限大的数据流，通过不断的next来去下一个元素；但是像

  list这样的就不行存储无限大的数据流:
  1. 类比java中的Iterable接口和Iterator类，容器都只有通过调用iterator()方法才能生成可以next的数据;
  2. 凡是可作用于for循环的对象都是Iterable类型；
  3. 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
  4. 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象

#高阶函数：
  map/reduce/filter/sorted都是对一组数据流中元素做运算的统一抽象，参数都是处理规则func和一个数据流Iterable;

  返回函数;

  匿名函数 lambda;

  **装饰器**(Python 提供了语言级别的装饰器模型，在Java中通过继承实现);
  
  偏函数
	
#面向对象：
  动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的，多态中传递的参数不一定是父类型对象，只要他实现同种方法
  
  对象实例允许动态绑定实例属性和方法；

  \_\_slot\_\_:限定能绑定的属性;

  @property:可以实现属性的直接访问，但同时可以进行属性检查，相当于装饰器；

  继承过程中的父类调用可以显示SuperClass.__init__也可以用super()

  The \_\_init\_\_ method of our Employee class explicitly invokes the \_\_init\_\_method of the Person class. We could have used super instead. super().\_\_init\_\_(first, last) is automatically replaced by a call to the superclasses method, in this case \_\_init\_\_:
    
```Python
def __init__(self, first, last, staffnum):
	super().__init__(first, last)
	self.staffnumber = staffnum
```
  Please note that we used super() without arguments. This is only possible in Python3. We could have written "super(Employee, self).\_\_init\_\_(first, last, age)" which still works in Python3 and is compatible with Python2.
	
  type和class:class的创建本质上是由type完成的，type(classname, superclasses, attributedict) 能够动态创建类；

  type是类的创建者，因此object是type的实例，同时type继承自object，所以 isinstance(type, object)和isinstance(object, type)都为真。当type被调用，type.\_\_call\_\_()会调 type.\_\_new\_\_(typeclass, classname, superclass,attributedict) type.\_\_init\_\_(cls, classname, superclasses, attributedict)
	
```Python
class Robot:
    counter = 0
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return "Hi, I am " + self.name
    def Rob_init(self, name):
        self.name = name
    Robot2 = type("Robot2", 
              (), 
              {"counter":0, 
               "__init__": Rob_init,
               "sayHello": lambda self: "Hi, I am " + self.name})
```
  Robot和Robot2是一样的

#装饰器：
  这里的装饰器和设计模式里的装饰模式并不是同一个概念；

  他本质上是一种语法糖，可以实现对一段函数代码的替换，主要是对这段函数代码的前后增加一些通用的额外的代码。比如，枷锁，解锁；进入，退出；前后包裹闭合的html节点；使用方法是在要装饰的函数前加@decorator;

  decorator可以是函数也可以是类；decorator必须时可以调用的，也就是实现了\_\_call\_\_函数，并且还需要返回一个函数作为结果来替换被装饰的函数。由于函数本身就是可以调用的，因此不必额外添加\_\_call\_\_(),但是类就必须加；

  decorator也分带参数和不带参数的;

  比如：
```Python
def log(func):
    def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	retrn wrapper

def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print(text)
			print('call %s():' % func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

class decorator(object):
	def __init__(self, func):
		self.f = func
	def __call__(self, *args):
		self.f(*args)

class decorator(object):
	def __init__(self, arg1, arg2, arg3):
		self.arg1 = arg1
		self.arg2 = arg2
		self.arg3 = arg3
	def __call__(self, func):
		def wrapper(*args):
			func(*args)
		return wrapper
```

#元类和元方法：
  我们知道，一般情况下，我们会知道类有哪些属性和方法，然后我们据此定义类，但是当我们事先不知道，只有在运行的时候才知道时，如何动态的生成一个类，并用该类来创建实例呢？也就是元类，生成类的类。

  python类的创建都是type创建的；因此如何动态的生成一个类，就需要用到type这个元类。

#元类中使用\_\_new\_\_(mcl,name,bases,namespc)和\_\_init\_\_(cls,name,bases,namespc)
  使用元类创建一个新的类时，首先调用\_\_new\_\_，在类被创建之后，才调用\_\_init\_\_来做一些初始化工作；
  
  \_\_new\_\_和\_\_init\_\_有一个关键的区别就是，\_\_new\_\_可以在调用父类构造器之前改变类的定义和行为，比如改变name，bases，namespace这些参数。这里我们就可以通过构造元类，来改变子类定义的方法，动态的生成一个类了；不过这里有特定的语法来动态生成一个类；以下是代码示例：

```Python

```
  正常情况下，普通的类不需要用到\_\_new\_\_,只需要\_\_init\_\_初始化就行了；
