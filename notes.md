#关于数据类型：
    亮点是*动态类型*的语言和shell脚本类似），也就是在运行过程中可以改变数据类型；
    这是C/C++ Java这种静态类型（编译时就确定了类型，切类型不可修改，如 int a = 5; a = "asd";是不允许的）的语言没有的
#关于字符编码：
    Python3在内存中的字符表示都采用了unicode编码；
    读取某种编码格式（ASCII UTF-8 GB2312）的源文件-->以unicode方式存入内存-->以某种编码方式写入磁盘或者网络
#关于list []和tuple ()：
    list可以存储不同数据类型的元素（原因是Python是动态类型的语言啊），C++ Java中的List就不行
    tuple是一旦初始化就不可改变的list，是一种安全的list；**注意的是，tuple的元素不变指的是元素的“指向”不变**；
#关于dict和set:
    其实就是hash，key为不可变对象；set是元素不重复的list,s = set([1,1,2,3,2])

#关于函数：
    Python的函数可以返回任意多个返回值（实际上是返回一个tuple）；
    参数传递灵活，有必选参数、默认参数、*可选参数（*args）tuple*、关键字参数（**kw）dict、命名关键字参数(*做分隔符)可混用
#高级特性：
    切片：就是把集合进行划分的语法；L = list(range(10)) L[start:end] 特别要注意start和end可以为负数，有很多巧妙的切片操作
          eg：翻转一个字符串 s[::-1] 
    迭代：for ele in Iterable:
    列表生成器：[x*x for x in range() if x]
    *生成器generator*：为了*动态生成列表从而节省内存*,一边循环一边计算,也即是说generator保存的是列表元素的生成算法;
     把[]改为()；g = (x*x for x in range()) next(g)；复杂的算法可以用一个generator函数来完成，每一次next(g)执行就会到yeild
        可以直接作用于for循环的数据类型有以下几种：
        一类是集合数据类型，如list、tuple、dict、set、str等；
        一类是generator，包括生成器和带yield的generator function。
        这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
    迭代器：Iterable != Iterator,generator都是Iterator；Iterator是一个无限大的数据流，通过不断的next来去下一个元素；但是像

    list这样的就不行存储无限大的数据流
    类比java中的Iterable接口和Iterator类，容器都只有通过调用iterator()方法才能生成可以next的数据流
    凡是可作用于for循环的对象都是Iterable类型；
    凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
    集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
#高阶函数：
    map/reduce/filter/sorted都是对一组数据流中元素做运算的统一抽象，参数都是处理规则func和一个数据流Iterable
    返回函数
    匿名函数 lambda
    **装饰器**(Python 提供了语言级别的装饰器模型，在Java中通过继承实现)
    偏函数
    