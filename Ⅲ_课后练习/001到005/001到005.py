def main():
    #       ↓在此控制运行哪些章节的示例代码↓
    #        "ctrl + /" 快捷注释 / 取消注释
    #********************控制台********************
    # test1()                        # 第1题：找水仙花数
    # test2()                        # 第2题：猴子吃桃
    # test3()                        # 第3题：统计字符类型个数
    # test4()                        # 第4题：简单列表排序
    # test5()                        # 第5题：复杂列表排序
    test6()                        # 第6题：列表偶数求和
    # test7()                        #
    # test8()                        #
    # test9()                        #
    # test10()                       #
    #********************控制台********************

#--------------------------------------------------------------------------------
# 第1题：找水仙花数
def test1():
    """
    需求：找水仙花数
    🞉 水仙花数：各位数字立方和等于该数本身的三位数
    """
    print("第1题：找水仙花数========================================")
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a ** 3 + b ** 3 + c ** 3 == i:
            print(i)

    print()
#--------------------------------------------------------------------------------
# 第2题：猴子吃桃
def test2():
    """
    需求：介绍略，第10天吃前只剩一个桃子，求第一天摘了多少个(第一天也吃了)
    """
    print("第2题：猴子吃桃========================================")
    # 递归解决
    def eat1(day):
        if day == 1:
            return 1
        else:
            return (eat1(day - 1) + 1) * 2
    print(f"第一天摘了{eat1(10)}个桃子")
    print("--------------------")
    # for循环解决
    def eat2(day):
        peaches = 1 # 第day天剩下1个桃子
        for day in range(day - 1, 0, -1):
            peaches = (peaches + 1) * 2
        return peaches
    print(f"第一天摘了{eat2(10)}个桃子")

    print()
# --------------------------------------------------------------------------------
# 第3题：统计字符类型个数
def test3():
    """
    需求：输入一行字符，分别统计出其中英文字符、空格、数字和其它字符的个数
    """
    print("第3题：统计字符类型个数========================================")
    str = input("输入任意字符串：")

    count_letter = 0
    count_space = 0
    count_digit = 0
    count_other = 0

    for ch in str:
        if ch.isalpha():
            count_letter += 1
        elif ch.isspace():
            count_space += 1
        elif ch.isdigit():
            count_digit += 1
        else:
            count_other += 1

    print(f"中英文字符：{count_letter}")
    print(f"空格：{count_space}")
    print(f"数字：{count_digit}")
    print(f"其它字符：{count_other}")

    print()
#--------------------------------------------------------------------------------
# 第4题：简单列表排序
def test4():
    """
    需求：给定一个简单列表，对其元素进行排序
    🞉 简单列表：元素类型不是复合类型(列表/元组/字典)
    """
    print("第4题：简单列表排序========================================")
    # 1.会改变原内容的排序函数：.sort(key=None, reverse=False)
    #   🞉 参数详解：
    #     · key(可选)：接收一个函数作为参数。该函数会在每个元素上调用，其返回值将作为排序的依据。
    #            如果未提供，则直接比较
    #     · reverse(可选)：指定排序规则，默认为False(升序)，如果为True则为降序
    # 2.不改变原内容的排序函数：sorted(iterable, key=None, reverse=False)
    #   🞉 参数详解：
    #     · iterable：可迭代对象(排序目标)
    #     · key(可选)：接收一个函数作为参数。该函数会在每个元素上调用，其返回值将作为排序的依据。
    #            如果未提供，则直接比较
    #     · reverse(可选)：指定排序规则，默认为False(升序)，如果为True则为降序

    list = [5, 3, 1, 2, 4]
    print(f"排序前原列表：{list}")
    print(f"方法2排序后：{sorted(list)}")
    print(f"方法2排序后原列表：{list}")
    list.sort() # .sort返回值是None！不能直接打印！
    print(f"方法1排序后：{list}")
    print(f"方法1排序后原列表：{list}")

    print()
#--------------------------------------------------------------------------------
# 第5题：复杂列表排序
def test5():
    """
    需求：给定一个学生信息列表，根据学生的成绩进行排序
    🞉 学生成绩数据格式：复杂列表，元素是字典或者元组
    """
    print("第5题：复杂列表排序========================================")
    # 结合匿名函数简化代码：lambda 形参: 返回值
    # ※注意：匿名函数只能实现简单的逻辑(一个函数只有一个返回值且只有一句代码)
    #         一般而言，匿名函数调用次数很少，基本上就只调用一次
    students = [
        {"sno":101, "sname": "张三", "sgrade": 90},
        {"sno":104, "sname": "李四", "sgrade": 100},
        {"sno":102, "sname": "王五", "sgrade": 70},
        {"sno":105, "sname": "赵六", "sgrade": 80},
        {"sno":103, "sname": "孙七", "sgrade": 60}
    ]
    # 定义一个打印方法，方便查看列表
    def print_students(students):
        for s in students:
            print(f"学号：{s['sno']}，姓名：{s['sname']}，成绩：{s['sgrade']}")
    print(f"排序前原列表：")
    print_students(students)
    print("--------------------")
    print(f"按学号排序后：")
    print_students(sorted(students, key=lambda s: s['sno']))
    print("--------------------")
    print(f"按姓名排序后：")
    print_students(sorted(students, key=lambda s: s['sname'], reverse=True))
    print("--------------------")
    print(f"按成绩排序后：")
    print_students(sorted(students, key=lambda s: s['sgrade'], reverse=True))

    print()
# --------------------------------------------------------------------------------
# 第6题：列表偶数求和
def test6():
    """
    需求：给定一个整数列表，计算并打印该列表中所有偶数的和
    """
    print("第6题：列表偶数求和========================================")
    list = [1, 3, 2, 4, 5, 6, 10, 8, 9, 7]
    sum1 = 0
    sum2 = 0
    # 使用普通循环解决：
    for i in list:
        if i % 2 == 0:
            sum1 += i
    print(f"列表中所有偶数和为：{sum1}")
    print("--------------------")
    # 使用列表推导式解决：[表达式 for 变量 in 可迭代对象 if 条件]
    for i in [i for i in range(len(list)) if list[i] % 2 == 0]:
        sum2 += list[i]
    print(f"列表中所有偶数和为：{sum2}")

    print()
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()