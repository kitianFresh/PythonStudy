#�����������ͣ�
    �����Ƕ�̬���͵����Ժ�shell�ű����ƣ�Ҳ���������й����п��Ըı��������ͣ�
    ����C/C++ Java���־�̬���ͣ�����ʱ��ȷ�������ͣ������Ͳ����޸ģ��� int a = 5; a = "asd";�ǲ�����ģ�������û�е�
#�����ַ����룺
    Python3���ڴ��е��ַ���ʾ��������unicode���룻
    ��ȡĳ�ֱ����ʽ��ASCII UTF-8 GB2312����Դ�ļ�-->��unicode��ʽ�����ڴ�-->��ĳ�ֱ��뷽ʽд����̻�������
	һ���ַ������ɣ� 'c'*n ��ʾ'c'�ظ�n�� ��n = 3�����ʾ'ccc'
#����list []��tuple ()��
    list���Դ洢��ͬ�������͵�Ԫ�أ�ԭ����Python�Ƕ�̬���͵����԰�����C++ Java�е�List�Ͳ���
    tuple��һ����ʼ���Ͳ��ɸı��list����һ�ְ�ȫ��list��**ע����ǣ�tuple��Ԫ�ز���ָ����Ԫ�صġ�ָ�򡱲���**��
#����dict��set:
    ��ʵ����hash��keyΪ���ɱ����set��Ԫ�ز��ظ���list,s = set([1,1,2,3,2])

#���ں�����
    Python�ĺ������Է�������������ֵ��ʵ�����Ƿ���һ��tuple����
    �����������б�ѡ������Ĭ�ϲ�����*��ѡ������*args��tuple*���ؼ��ֲ�����**kw��dict�������ؼ��ֲ���(*���ָ���)�ɻ���
#�߼����ԣ�
    ��Ƭ�����ǰѼ��Ͻ��л��ֵ��﷨��L = list(range(10)) L[start:end] �ر�Ҫע��start��end����Ϊ�������кܶ��������Ƭ����
          eg����תһ���ַ��� s[::-1] 
    ������for ele in Iterable:
    �б���������[x*x for x in range() if x]
    *������generator*��Ϊ��*��̬�����б�Ӷ���ʡ�ڴ�*,һ��ѭ��һ�߼���,Ҳ����˵generator��������б�Ԫ�ص������㷨;
     ��[]��Ϊ()��g = (x*x for x in range()) next(g)�����ӵ��㷨������һ��generator��������ɣ�ÿһ��next(g)ִ�оͻᵽyeild
        ����ֱ��������forѭ�����������������¼��֣�
        һ���Ǽ����������ͣ���list��tuple��dict��set��str�ȣ�
        һ����generator�������������ʹ�yield��generator function��
        ��Щ����ֱ��������forѭ���Ķ���ͳ��Ϊ�ɵ�������Iterable
    ��������Iterable != Iterator,generator����Iterator��Iterator��һ�����޴����������ͨ�����ϵ�next��ȥ��һ��Ԫ�أ�������

    list�����ľͲ��д洢���޴��������
    ���java�е�Iterable�ӿں�Iterator�࣬������ֻ��ͨ������iterator()�����������ɿ���next��������
    ���ǿ�������forѭ���Ķ�����Iterable���ͣ�
    ���ǿ�������next()�����Ķ�����Iterator���ͣ����Ǳ�ʾһ�����Լ�������У�
    ��������������list��dict��str����Iterable������Iterator����������ͨ��iter()�������һ��Iterator����
#�߽׺�����
    map/reduce/filter/sorted���Ƕ�һ����������Ԫ���������ͳһ���󣬲������Ǵ������func��һ��������Iterable
    ���غ���
    �������� lambda
    **װ����**(Python �ṩ�����Լ����װ����ģ�ͣ���Java��ͨ���̳�ʵ��)
    ƫ����
	
#�������
    ��̬���Ե�Ѽ�������ص�����˼̳в���̬���������Ǳ���ģ���̬�д��ݵĲ�����һ���Ǹ����Ͷ���ֻҪ��ʵ��ͬ�ַ���
	����ʵ������̬��ʵ�����Ժͷ�����
	__slot__:�޶��ܰ󶨵�����
	@property:����ʵ�����Ե�ֱ�ӷ��ʣ���ͬʱ���Խ������Լ�飬�൱��װ����
	�̳й����еĸ�����ÿ�����ʾSuperClass.__init__Ҳ������super()
	The __init__ method of our Employee class explicitly invokes the __init__method of the 
	Person class. We could have used super instead. super().__init__(first, last) is 
	automatically replaced by a call to the superclasses method, in this case __init__:
    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum
	Please note that we used super() without arguments. This is only possible in Python3. 
	We could have written "super(Employee, self).__init__(first, last, age)" which still 
	works in Python3 and is compatible with Python2.
	type��class:class�Ĵ�������������type��ɵģ�type(classname, superclasses, attributedict)
	�ܹ���̬�����ࣻtype����Ĵ����ߣ����object��type��ʵ����ͬʱtype�̳���object������
	isinstance(type, object)��isinstance(object, type)��Ϊ�档��type�����ã�type.__call__()���
	type.__new__(typeclass, classname, superclass,attributedict)
	type.__init__(cls, classname, superclasses, attributedict)
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
    Robot��Robot2��һ����
    