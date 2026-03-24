import os

def main():
    #       ↓在此控制运行哪些章节的示例代码↓
    #        "ctrl + /" 快捷注释 / 取消注释
    #********************控制台********************
    # encapsulation_inheritance()    # 一、封装和继承
    # polymorphism()                 # 二、多态
    # file_operation()               # 三、文件操作
    # directory_operation()          # 四、目录常用操作
    regular_expression()           # 五、正则表达式
    #********************控制台********************

# --------------------------------------------------------------------------------
# 一、封装和继承
def encapsulation_inheritance():
    print("一、封装和继承========================================")
    # 1.基础操作一览
    #    操作                         说明                        示例
    #   定义类	                    创建一个类	                class Person:
    #                                                               pass
    #   定义构造方法	                初始化实例属性	            def __init__(self, name):
    #                                                               self.name = name
    #   析构函数(了解)	            在实例被销毁时执行           def __del__(self):
    #                                                               print(f"{self.name}对象使用完毕，已销毁")
    #   创建实例	                实例化对象	                p = Person("Alice")
    #   定义实例方法	                操作实例数据	                def greet(self):
    #                                                               return f"你好，{self.name}"
    #   调用实例方法	                执行实例方法	                p.greet()
    #   定义类方法	                操作类级别数据	            @classmethod
    #                                                           def from_string(cls, s):
    #                                                               return cls(s)
    #   调用类方法	                通过类或实例调用	            Person.from_string("Bob")
    #   定义静态方法	                与类相关但无需访问实例/类	@staticmethod
    #                                                           def is_valid_name(name):
    #                                                               return len(name) > 0
    #   调用静态方法	                通过类或实例调用	            Person.is_valid_name("Alice")
    #   定义属性	                在实例上添加属性	            p.age = 25
    #   访问属性	                获取属性值	                p.name
    #   修改属性	                更改属性值	                p.name = "Bob"
    #   删除属性	                删除实例属性	                del p.age
    #   定义私有属性(约定)	        表示内部使用，不应直接访问	self._internal = 10
    #   定义名称改写属性	            避免子类意外覆盖	            self.__secret = "hidden"
    #   访问名称改写属性(不建议)	    实际通过改写后的名称访问	    p._Person__secret
    #   定义属性装饰器(getter)	    实现属性访问控制	            @property
    #                                                           def name(self):
    #                                                               return self._name
    #   定义属性装饰器(setter)	    实现属性赋值控制	            @name.setter
    #                                                           def name(self, value):
    #                                                               self._name = value
    #   单继承	                    继承一个父类	                class Student(Person):
    #                                                               pass
    #   多继承	                    继承多个父类	                class Teacher(Person, Employee):
    #   (注：多继承到同名方法时，优先调用先继承的。                   pass
    #        建议避免使用多继承，用"单继承+组合"[在子类中创建其他类的实例，复用功能])
    #   重写父类方法	                覆盖父类方法	                def greet(self):
    #                                                               super().greet()         #这行代码可以保留父类方法
    #                                                               print("I'm a student")  #子类方法的功能
    #   调用父类方法	                使用父类的方法	            super().__init__(name)
    #   判断实例类型	                检查对象是否为指定类的实例   isinstance(p, Person)
    #   判断子类关系	                检查类是否为另一类的子类	    issubclass(Student, Person)
    #   获取类名	                获取实例所属类的名称	        p.__class__.__name__
    #   获取所有属性	                获取实例的所有属性和方法	    dir(p)
    #   查看实例字典	                获取实例的属性字典	        p.__dict__
    #   定义字符串表示(用户友好)	    供 print() 等调用	        def __str__(self):
    #                                                               return f"Person: {self.name}"
    #   定义字符串表示(开发者友好)	供调试使用	                def __repr__(self):
    #                                                               return f"Person('{self.name}')"
    #   定义运算符重载	            实现对象间的加法等操作	    def __add__(self, other):
    #                                                               return self.age + other.age
    #   限制实例属性	                固定允许的属性名，节省内存	__slots__ = ['name', 'age']
    #   定义可调用对象	            =使实例可以像函数一样调用	     def __call__(self, x):

    # 2.静态方法 vs 类方法 vs 实例方法
    #    对比维度      静态方法(@staticmethod)       类方法(@classmethod)      实例方法
    #   第一个参数    无(不用self/cls)              cls(代表类)               self(代表实例)
    #   装饰器        需要@staticmethod            需要@classmethod          不需要
    #   访问属性      只能访问类属性(不推荐)        只能访问类属性(通过cls)    能访问实例属性(通过self)
    #   调用方式      类名.方法名()(推荐)           类名.方法名()(推荐)       对象.方法名()(必须创建对象)
    #                 对象.方法名()                对象.方法名()
    #   核心用途      独立工具功能(如计算，验证)    操作类属性、工厂方法       操作实例属性、实例相关功能

    # 例：
    class Person:
        average = 75    # 平均寿命(类属性)

        def incorrect_get_average(self):
            return self.average
        def incorrect_set_average(self, value):
            self.average = value

        @classmethod
        def correct_get_average(cls):
            return cls.average
        @classmethod
        def correct_set_average(cls, value):
            cls.average = value

    person1 = Person()
    print(person1.incorrect_get_average())
    person1.incorrect_set_average(80)
    print(person1.incorrect_get_average())
    person2 = Person()
    print(person2.incorrect_get_average())
    print("--------------------")
    # 这里也可以通过对象调用类方法(但不推荐)
    print (Person.correct_get_average())
    Person.correct_set_average(90)
    print (Person.correct_get_average())
    print(person2.incorrect_get_average())
    print("--------------------")
    #----------------------------------------
    class Watch:
        def show_time(self):
            print(f"{self.__class__.__name__}查看时间")
    class HealthDevice:
        # 用owner来存储"单继承+组合"时的调用者
        def __init__(self, owner=None):
            self.owner = owner
        def check_health(self):
            # 当self.owner不为None时，说明是单继承+组合，用self.owner.__class__.__name__获取类名
            if self.owner:
                name = self.owner.__class__.__name__
            # 当self.owner为None时，说明是多继承，直接用self.__class__.__name__获取类名
            else:
                name = self.__class__.__name__
            print(f"{name}查看健康状态")
    # 用多继承创建一个智能手表类
    class SmartWatchA(Watch, HealthDevice):
        pass
    # 用"单继承+组合"创建一个智能手表类
    class SmartWatchB(Watch):
        def __init__(self):
            self.hd = HealthDevice(self)

    smart_watch_a = SmartWatchA()
    smart_watch_a.show_time()
    smart_watch_a.check_health()
    print("--------------------")
    smart_watch_b = SmartWatchB()
    smart_watch_b.show_time()
    smart_watch_b.hd.check_health()

    print()
# --------------------------------------------------------------------------------
# 二、多态
def polymorphism():
    print("二、多态========================================")
    # 1.作用：不同类的对象，调用同名方法时，会执行各自类的实现，得到不同结果
    # 2.格式：
    #   2.1.鸭子类型(Python等动态语言典型用法，最常用)
    #   2.2.继承+方法重写(适合有层级关系的场景)

    # 2.1 例：
    class WechatPay:
        def pay(self,money):
            print(f"微信支付{money}元")
    class AlipayPay:
        def pay(self,money):
            print(f"支付宝支付{money}元")
    def pay_order(pay_method,money):
        pay_method.pay(money)

    pay_order(WechatPay(),10)
    pay_order(AlipayPay(),20)
    print("--------------------")

    # 2.2 例：
    class Animal:
        def make_sound(self):
            print("动物发出声音")
    class Dog(Animal):
        def make_sound(self):
            print("狗汪汪叫")
    class Cat(Animal):
        def make_sound(self):
            print("猫喵喵叫")
    def animal_make_sound(animal):
        animal.make_sound()

    animal_make_sound(Dog())
    animal_make_sound(Cat())

    print()
#--------------------------------------------------------------------------------
# 三、文件操作
def file_operation():
    print("三、文件操作========================================")
    # 1.文件打开/关闭：
    #   🞉 打开文件：
    #     · 格式1：文件对象 = open(文件路径, 访问模式, encoding="编码格式")
    #              读写操作...
    #        注意：其中编码格式仅用于文本文件
    #   ※· 格式2：with open(文件路径, 访问模式, encoding="编码格式") as 文件对象:
    #                 读写操作...
    #        注意：该方式会自动关闭文件(推荐)
    #   🞉 关闭文件：
    #     · 格式：文件对象.close

    # 2.文件读写：
    #   🞉 文件访问模式：
    #       模式    功能描述      是否创建新文件                   注意事项
    #       r     只读(默认)    否(文件不存在报错)               只能读，不能写
    #       w     只写          是(文件不存在创建，存在则覆盖)    只能写，不能读
    #       a     追加          是(文件不存在创建，存在则追加)    只能写，不能读
    #       r+    读写          否(文件不存在报错)               可同时读写，写在开头(会覆盖原有内容)
    #       w+    读写          是(文件不存在创建，存在则覆盖)    可同时读写
    #       a+    读写          是(文件不存在创建，存在则追加)    可同时读写，写在末尾
    #     注：二进制文件操作需用 b 模式(如 rb、wb 等)
    #   🞉 读取文件：
    #     · 格式1：文件对象.read(n)        # 读取指定字符(文本模式)/字节(二进制模式)，默认全部读取
    #     · 格式2：文件对象.readline()     # 逐行读取(文件指针自动换行)，适合大文件
    #     · 格式3：文件对象.readlines()    # 读取所有行(返回字符串列表)，适合小文件
    #     注：二进制文件用 read() 即可
    #   🞉 写入文件：
    #   ※· 格式1：文件对象.write(内容)
    #     注：对于文本文件，内容必须是字符串
    #         对于二进制文件，内容必须是 byte类型的字节串
    #     · 格式2：文件对象.writelines(字符串列表)
    #     注：写入字符串列表，但不会自动添加换行符
    #         实际使用较少，因为可以用 write() + "\n".join() 替代
    #         示例：f.write("\n".join(lines))    # 更简洁
    #   🞉 文件指针：读模式下，指针起始位置在开头；其他模式下，指针起始位置在末尾
    #     相关常用函数：
    #     · tell()                                            #返回当前指针位置(字节数)
    #     · seek(偏移量, 参考点[0:开头；1:当前位置；2:末尾])    # 移动指针

    # 3.文件路径
    #   🞉 绝对路径：略
    #   🞉 相对路径：
    #     · .：代表"当前目录"(脚本所在文件夹)，可省略
    #     · ..：代表"上一级目录"(脚本所在文件夹的父文件夹)
    #   🞉 获取脚本所在路径：
    #      import os
    #      print(os.getcwd())

    # 例：
    # Windows系统中，路径用反斜杠 \，但Python中 \ 是转义符
    # 所以要么加 r 前缀(推荐)，要么用双反斜杠 \\。
    print(os.getcwd())
    print("--------------------")
    with open (r".\文件操作.txt", "a+", encoding="utf-8") as f:
        # a+ 模式下文件指针在末尾
        f.seek(0)
        print(f.read())
        print("--------------------")
        f.write("\n追加内容")
        f.seek(0)
        print(f.read())

    print()
#--------------------------------------------------------------------------------
# 四、目录常用操作
def directory_operation():
    print("四、目录常用操作========================================")
    # 1.前提：导入 os 模块 和 shutil 模块
    #   格式：import os
    #         import shutil

    # 2.文件/目录操作：
    #   2.1.文件操作：
    #      🞉 文件移动/改名：os.rename()
    #       功能：给文件/目录改名、移动文件到同一磁盘的其他目录 (本质是 改路径 + 改名字)
    #       格式：os.rename(源路径, 目标路径)
    #        · 源路径：文件/目录的原始路径(相对路径或绝对路径)
    #        · 目标路径：修改后的新路径(如果只改名字，路径不变即可；如果要移动，改路径即可)
    #       注意：源路径必须切实存在，否则报错
    #             跨盘移动会报错，如果需要跨盘移动，应使用 shutil.move()
    #             目标路径如果已存在同名文件/目录，会直接报错【谨慎操作！】
    #      🞉 删除文件：os.remove()
    #       功能：删除指定路径的文件(只能删文件，不能删目录)
    #       格式：os.remove(文件路径)
    #       注意：文件路径必须切实存在，否则报错
    #             删除目录会报错，如果需要删除目录，应使用 os.rmdir()
    #             删除后无法恢复(除非有备份)【谨慎操作！】
    #----------------------------------------
    #   2.2.目录操作：
    #      🞉 创建单级目录：os.mkdir()
    #       功能：创建一个新的单级空目录(文件夹)
    #       格式：os.mkdir(目录路径)
    #       注意：目录路径不能已存在，否则报错
    #             父目录必须切实存在，否则报错
    #      🞉 创建多级目录：os.makedirs()
    #       功能：创建一个新的多级空目录(文件夹)
    #       格式：os.makedirs(目录路径)
    #      🞉 删除空目录：os.rmdir()
    #       功能：删除指定的空目录(文件夹)
    #       格式：os.rmdir(目录路径)
    #       注意：目录路径必须切实存在，否则报错
    #             目录必须为空(不含文件、子目录)，否则报错
    #             删除后无法恢复【谨慎操作！】
    #      🞉 删除目录：shutil.rmtree()
    #       功能：完全删除指定的目录(文件夹)，无论其是否为空【谨慎操作！】
    #       格式：shutil.rmtree(目录路径)
    #      🞉 查看当前工作目录：os.getcwd()
    #       功能：获取Python脚本当前运行的目录(返回绝对路径)
    #       格式：os.getcwd()
    #      🞉 查看目录内容：os.listdir()
    #       功能：获取指定目录下的所有文件和子目录，返回一个列表(元素是文件名/目录名)
    #       格式：os.listdir(目录路径)
    #----------------------------------------
    #   2.3.路径检验：
    #      🞉 判断文件/目录是否存在：os.path.exists()
    #       功能：判断指定路径(文件或目录)是否存在，返回布尔值
    #       格式：os.path.exists(目标路径)
    #      🞉 检验是否为文件：os.path.isfile()
    #       功能：判断指定路径是否存在且是一个文件，返回布尔值
    #       格式：os.path.isfile(目标路径)
    #      🞉 检验是否为目录：os.path.isdir()
    #       功能：判断指定路径是否存在且是一个目录，返回布尔值
    #       格式：os.path.isdir(目标路径)
    #
    #  实际使用建议：对文件/路径进行操作前应当先判断其是否存在
    print("× 本章无控制台输出案例")

    print()
#--------------------------------------------------------------------------------
# 五、正则表达式
def regular_expression():
    print("五、正则表达式========================================")


    print()
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

