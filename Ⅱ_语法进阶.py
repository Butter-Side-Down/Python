def main():
    #       ↓在此控制运行哪些章节的示例代码↓
    #        "ctrl + /" 快捷注释 / 取消注释
    #********************控制台********************
    classes_and_objects()          # 一、类和对象
    #********************控制台********************

# --------------------------------------------------------------------------------
# 一、类和对象
def classes_and_objects():
    print("一、类和对象========================================")
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
    #   访问名称改写属性	            实际通过改写后的名称访问	    p._Person__secret
    #   定义属性装饰器(getter)	    实现属性访问控制	            @property
    #                                                           def name(self):
    #                                                               return self._name
    #   定义属性装饰器(setter)	    实现属性赋值控制	            @name.setter
    #                                                           def name(self, value):
    #                                                               self._name = value
    #   单继承	                    继承一个父类	                class Student(Person):
    #                                                               pass
    #   多继承	                    继承多个父类	                class Teacher(Person, Employee):
    #                                                               pass
    #   重写父类方法	                覆盖父类方法	                def greet(self):
    #                                                               return super().greet() + " I'm a student"
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

    # 例：
    print()
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

