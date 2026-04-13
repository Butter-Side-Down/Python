import math

def main():
    #       ↓在此控制运行哪些章节的示例代码↓
    #        "ctrl + /" 快捷注释 / 取消注释
    #********************控制台********************
    # test1()                        # 第1题：找水仙花数
    # test2()                        # 第2题：猴子吃桃
    # test3()                        # 第3题：统计字符类型个数
    # test4()                        # 第4题：简单列表排序
    # test5()                        # 第5题：复杂列表排序
    # test6()                        # 第6题：列表偶数求和
    # test7()                        # 第7题：找出年龄最大者
    # test8()                        # 第8题：动态排序
    # test9()                        # 第9题：寻找最小连续9整除数
    # test10()                       # 第10题：进制转换
    # test11()                       # 第11题：打印素数
    # test12()                       # 第12题：列表批量移除并求和
    # test13()                       # 第13题：列表去重
    # test14()                       # 第14题：元素互换
    # test15()                       # 第15题：计算倒数序列和
    # test16()                       # 第16题：日期计算
    # test17()                       # 第17题：斐波那契数列求项
    # test18()                       # 第18题：求质因数
    # test19()                       # 第19题：列表求积
    # test20()                       # 第20题：字符串截取和翻转
    # test21()                       # 第21题：字典键值互换
    # test22()                       # 第22题：字符串转换
    # test23()                       # 第23题：年龄验证(异常相关)
    # test24()                       # 第24题：Python绘图入门1
    # test25()                       # 第25题：Python绘图入门2
    # test26()                       # 第26题：Python绘图入门3
    # test27()                       # 第27题：导包生成随机数
    test28()                       # 第28题：随机生成验证码
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
# 第7题：找出年龄最大者
def test7():
    """
    需求：给定一个字典，其中每个人的姓名作为键，对应的年龄作为值。
          找出年龄最大者的姓名与年龄，并将其打印出来
    """
    print("第7题：找出年龄最大者========================================")
    peoples = {
        "张三": 18,
        "李四": 21,
        "王五": 19,
        "赵六": 21,
        "孙七": 17
    }

    max_age = float('-inf') # 将最大年龄初始化为负无穷大
    # 先找出最大年龄，然后找年龄匹配者)：
    for name, age in peoples.items():
        if age > max_age:
            max_age = age
    for name, age in peoples.items():
        if age == max_age:
            print(f"年龄最大者：{name}，年龄：{age}")

    print()
# --------------------------------------------------------------------------------
# 第8题：动态排序
def test8():
    """
    需求：给定一个已排序的整数列表，要求输入一个数后，
          根据列表原有的排序规律将其插入到正确的位置上
    """
    print("第8题：动态排序========================================")
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 3, 5, 7, 9]

    new_num = int(input("请输入要插入的数："))

    # 使用普通循环解决：
    for i in range(len(list1)):
        if new_num < list1[i]:
            list1.insert(i, new_num)
            break
    # 如果上面循环正常结束，则将新数插入到列表末尾
    else:
        list1.append(new_num)
    print(f"插入后列表为：{list1}")
    print("--------------------")
    # 使用列表函数解决：
    list2.append(new_num)
    list2.sort()
    print(f"插入后列表为：{list2}")

    print()
# --------------------------------------------------------------------------------
# 第9题：寻找最小连续9整除数
def test9():
    """
    需求：用户输入一个奇数，程序需要找到一个最小的由连续9组成的数(例如9, 99, 999等)
         这个数能被用户输入的奇数整除。输出这个最小的数以及它除以用户输入的奇数的结果。
    示例：如果用户输入3，程序应输出“最小的由1个9组成的数能被3整除”以及"9/3=3.0"；
          如果用户输入11，程序应输出"最小的由2个9组成的数能被11整除"以及"99/11=9.0"
    """
    print("第9题：寻找最小连续9整除数========================================")
    while True:
        num = int(input("请输入一个奇数："))
        if num % 2 == 1:
            divisor = num
            break

    devised = "9"
    count = 1
    while int(devised) % divisor != 0:
        devised += "9"
        count += 1
    print(f"最小的由{count}个9组成的数能被{divisor}整除")
    print(f"{devised}/{divisor}={int(devised) / divisor}")


    print()
# --------------------------------------------------------------------------------
# 第10题：进制转换
def test10():
    """
    需求：用户输入一个数字，实现十进制向二进制、八进制、十六进制的转换功能，并打印出转换结果
    """
    print("第10题：进制转换========================================")
    num = int(input("请输入一个数字："))
    print(f"十进制{num}转换成二进制为：{bin(num)}")
    print(f"十进制{num}转换成八进制为：{oct(num)}")
    print(f"十进制{num}转换成十六进制为：{hex(num)}")

    print()
# --------------------------------------------------------------------------------
# 第11题：打印素数
def test11():
    """
    需求：定义一个函数，该函数用于打印指定范围内的所有素数
    """
    print("第11题：打印素数========================================")
    def print_primes(start, end):
        results = []
        for i in range(start, end + 1):
            if i > 1:
                for j in range(2, int(math.sqrt(i)) + 1):
                    if i % j == 0:
                        break
                else:
                    results.append(i)
        return results

    print(f"结果：{print_primes(1, 100)}")

    print()
# --------------------------------------------------------------------------------
# 第12题：列表批量移除并求和
def test12():
    """
    需求：定义一个函数，该函数用于从第一个列表list1中移除所有存在于第二个列表list2中的元素，然后对剩余元素求和
    """
    print("第12题：列表批量移除并求和========================================")
    list1_1 = [1, 2, 3, 4, 5, 6, 7, 2, 8, 9, 10]
    list1_2 = [2, 6, 4, 11, 10]
    list2_1 = [1, 2, 3, 4, 5, 6, 7, 2, 8, 9, 10]
    list2_2 = [2, 6, 4, 11, 10]
    # 使用普通循环解决：
    def remove_and_sum1(list1, list2):
        new_list = []
        for i in list1:
            if i not in list2:
                new_list.append(i)
        print(new_list)
        return sum(new_list)
    # 使用列表推导式解决：
    def remove_and_sum2(list1, list2):
        new_list = [i for i in list1 if i not in list2]
        print(new_list)
        return sum(new_list)

    print(f"list1_1的结果为：{remove_and_sum1(list1_1, list1_2)}")
    print(f"list2_1的结果为：{remove_and_sum2(list2_1, list2_2)}")

    print()
# --------------------------------------------------------------------------------
# 第13题：列表去重
def test13():
    """
    需求：定义一个函数，该函数用于对列表进行去重处理，并返回一个不包含任何重复的元素的新列表
    """
    print("第13题：列表去重========================================")
    list1 = [9, 1, 3, 4, 7, 5, 6, 7, 2, 1, 9, 10]
    # 用循环解决：
    def remove_duplicates1(list1):
        new_list = []
        # 这里不能用列表推导式！因为其引用的是上面这个空的 new_list
        for i in list1:
            if i not in new_list:
                new_list.append(i)
        return new_list
    # 用集合解决：
    def remove_duplicates2(list1):
        new_list = list(set(list1))
        return new_list

    print(f"去重后的结果为：{remove_duplicates1(list1)}")
    print(f"去重后的结果为：{remove_duplicates2(list1)}")

    print()
# --------------------------------------------------------------------------------
# 第14题：元素互换
def test14():
    """
    需求：定义一个函数，该函数用于实现两个变量值的互换操作
    """
    print("第14题：元素互换========================================")
    var1 = 10
    var2 = 20
    # 通过解包解决：
    def swap(var1, var2):
        return var2, var1

    var1, var2 = swap(var1, var2)
    print(f"交换后的结果为：{var1}, {var2}")

    print()
# --------------------------------------------------------------------------------
# 第15题：计算倒数序列和
def test15():
    """
    需求：定义一个函数，该函数用于根据传入的整数n返回对应的倒数序列和：
          若n为偶数，则计算和1/2+1/4+...+1/n；
          若n为奇数，则计算和1/1+1/3+...+1/n
    """
    print("第15题：计算倒数序列和========================================")
    def calculate_sum(n):
        if n % 2 == 0:
            return sum(1 / i for i in range(2, n + 1, 2))
        else:
            return sum(1 / i for i in range(1, n + 1, 2))

    print(f"结果为：{calculate_sum(2)}")

    print()
# --------------------------------------------------------------------------------
# 第16题：日期计算
def test16():
    """
    需求：定义一个函数，该函数接收年份、月份和日期作为参数，计算这一天是该年的第几天
    """
    print("第16题：日期计算========================================")
    def is_leap_year(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False

    def calculate_day(year, month, day):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap_year(year):
            days[1] = 29
        total_days = sum(days[:month - 1]) + day
        print(f"{year}年{month}月{day}日是该年的第{total_days}天")

    calculate_day(2026, 4, 5)

    print()
# --------------------------------------------------------------------------------
# 第17题：斐波那契数列求项
def test17():
    """
    需求：定义一个函数，该函数用于计算斐波那契数列中的第n项
    斐波那契数列：数列的前两项均为1，从第三项开始，每一项都是其前两项的和。
                  如：1、1、2、3、5、...
    """
    print("第17题：斐波那契数列求项========================================")
    # 使用循环解决：
    def fibonacci1(n):
        if n <= 0:
            return "输入的数字必须大于0"
        elif n == 1 or n == 2:
            return 1
        else:
            fib_list = [1, 1]
            for i in range(2, n):
                fib_list.append(fib_list[i - 1] + fib_list[i - 2])
            return fib_list[n - 1]
    # 使用递归解决：
    def fibonacci2(n):
        if n <= 0:
            return "输入的数字必须大于0"
        elif n == 1 or n == 2:
            return 1
        else:
            return fibonacci2(n - 1) + fibonacci2(n - 2)

    print(f"斐波那契数列第5项为：{fibonacci1(5)}")
    print("--------------------")
    print(f"斐波那契数列第8项为：{fibonacci2(8)}")

    print()
# --------------------------------------------------------------------------------
# 第18题：求质因数
def test18():
    """
    需求：定义一个函数，该函数接收一个正整数n作为参数，并将其分解为质因数，打印出分解的结果
    示例：传入数据90，打印 90 = 2 * 3 * 3 * 5 作为质因数分解的结果
    """
    print("第18题：求质因数========================================")
    def factorize(n):
        num = n # 保存原始值
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        # 如果剩余 n > 1，说明它本身是个质数
        if n > 1:
            factors.append(n)
        # 将数值列表转换为字符串，并打印出分解的结果
        print(f"{num} = {' * '.join(map(str, factors))}")

    factorize(1234)

    print()
# --------------------------------------------------------------------------------
# 第19题：列表求积
def test19():
    """
    需求：定义一个函数，该函数接收一个整数作为参数，并返回列表中所有元素的乘积
    """
    print("第19题：列表求积========================================")
    def product(list1):
        if not list1:
            return "错误！列表不能为空！"
        elif not all(isinstance(i, int) for i in list1):
            return "错误！列表中只能包含整数！"
        else:
            result = 1
            for i in list1:
                result *= i
            return result

    print(f"列表中元素的乘积为：{product([])}")
    print(f"列表中元素的乘积为：{product([1, 2, '3', 4, 5])}")
    print(f"列表中元素的乘积为：{product([1, 2, 3, 4, 5])}")

    print()
# --------------------------------------------------------------------------------
# 第20题：字符串截取和翻转
def test20():
    """
    需求：定义一个函数，该函数接收一个字符串和一个整数作为参数。完成以下操作：
          1.从字符串头部截取指定数量的字符并翻转
          2.从字符串尾部截取相同数量的字符并翻转
          3.分别打印出 头部和尾部翻转后与剩余部分拼接后的新字符串
    """
    print("第20题：字符串截取和翻转========================================")
    def reverse_string(string, n):
        if not isinstance(string, str):
            return "错误！请输入字符串！"
        elif not isinstance(n, int):
            return "错误！请输入整数！"
        elif n > len(string):
            return "错误！截取的字符数量不能大于字符串的长度！"
        else:
            # 截取头部和尾部字符
            head = string[:n]
            head_remaining = string[n:]
            tail = string[-n:]
            tail_remaining = string[:-n]
            # 翻转字符
            new_head = head[::-1]
            new_tail = tail[::-1]
            new_string1 = new_head + head_remaining
            new_string2 = tail_remaining + new_tail
            return new_string1, new_string2

    print(f"字符串截取和翻转结果为：{reverse_string('hello world', 99)}")
    print(f"字符串截取和翻转结果为：{reverse_string('hello world', 3)}")
    print(f"字符串截取和翻转结果为：{reverse_string('hello world', 6)}")

    print()
# --------------------------------------------------------------------------------
# 第21题：字典键值互换
def test21():
    """
    需求：定义一个函数，用于交换指定字典的 key 和 value
    """
    print("第21题：字典键值互换========================================")
    def swap_keys_values(dictionary):
        if not isinstance(dictionary, dict):
            return "错误！请输入字典！"
        elif not dictionary:
            return "错误！字典不能为空！"
        elif len(dictionary.keys()) != len(set(dictionary.values())):
            return "错误！字典的 value 有重复，不能转换为 key ！"
        else:
            return {v: k for k, v in dictionary.items()}

    print(swap_keys_values({'a': 1, 'b': 2, 'c': 2}))
    print(swap_keys_values({'a': 1, 'b': 2, 'c': 3}))

    print()
# --------------------------------------------------------------------------------
# 第22题：字符串转换
def test22():
    """
    需求：定义一个函数，该函用于尝试将用户输入的字符串转换为整数：
          如果转换成功，则返回整数；否则返回错误信息
    """
    print("第22题：字符串转换========================================")
    def convert_string_to_int():
        try:
            return int(input("请输入一个整数："))
        except ValueError:
            return "错误！请输入有效的整数！"

    print(convert_string_to_int())

    print()
# --------------------------------------------------------------------------------
# 第23题：年龄验证(异常相关)
def test23():
    """
    需求：定义一个函数，该函数接收一个人的年龄作为参数
          如果年龄不在合法范围内(＜0或＞120)，则抛出异常，但不影响继续运行
    """
    print("第23题：年龄验证(异常相关)========================================")
    def verify_age(age):
        try:
            if age < 0 or age > 120:
                raise ValueError(f"❌ {age}不是有效值")
            else:
                print(f"年龄 {age} 验证成功！")
        except ValueError as e:
            print(e)

    verify_age(18)
    verify_age(-1)
    verify_age(122)
    verify_age(20)

    print()
# --------------------------------------------------------------------------------
# 第24题：Python绘图入门1
def test24():
    """
    需求：用Python的tkinter库来创建一个图形界面，并在其中绘制一个由圆圈组成的螺旋形图案
    """
    print("第24题：Python绘图入门1========================================")
    # 导入tkinter模块，用于创建图形用户界面
    from tkinter import Canvas, BOTH, mainloop
    def draw_spiral():
        # 创建一个Canvas组件，用于绘制图形，并设置宽度为500像素，高度为400像素
        canvas = Canvas(width=500, height=400)
        # 使用pack布局管理器将Canvas组件添加到窗口中，
        # 并设置其扩展和填充属性以便填满整个窗口
        canvas.pack(expand=True, fill=BOTH)
        # 初始化变量 k，用于控制圆圈的半径
        k = 1
        # 初始化变量 j，用于控制每次循环中 k 的增量，从而控制圆圈之间的大小差异
        j = 1
        # 绘制 26 个圆圈，形成类似螺旋线的同心圆
        for i in range(26):
            # 使用 create_oval 方法绘制圆圈
            canvas.create_oval(250-k, 200-k, 250+k, 200+k, width=1)
            k += j
            j += 0.4

        # 进入 tkinter 的主事件循环，这样窗口就会保持打开状态并响应用户的操作(如关闭窗口)
        mainloop()

    draw_spiral()

    print()
# --------------------------------------------------------------------------------
# 第25题：Python绘图入门2
def test25():
    """
    需求：使用Python的tkinter库来创建一个图形界面，并在其中绘制一个由红色线条组成的螺旋形图案
    """
    print("第25题：Python绘图入门2========================================")
    from tkinter import Canvas, BOTH, mainloop
    def draw_spiral():
        canvas = Canvas(width=300, height=300, bg="white")
        canvas.pack(expand=True, fill=BOTH)
        # 初始化第一组线条的起点坐标
        x0, y0 = 163, 163
        # 初始化第一组线条的终点 y 坐标偏移量
        y1 = 175
        # 绘制第一组线条
        for i in range(19):
            canvas.create_line(x0, y0, x0, y1, width=1, fill="red")
            # 更新起点坐标，每次向左上方移动5个像素
            x0, y0 = x0-5, y0-5
            # 更新终点 y 坐标偏移量，每次增加5个像素
            y1 += 5
        # 初始化第二组线条的起点坐标(与第一组相同)
        x0, y0 = 163, 163
        # 初始化第二组线条的终点 y 坐标偏移量
        y1 = 175
        # 绘制第二组线条
        for i in range(19):
            canvas.create_line(x0, y0, x0, y1, width=1, fill="red")
            # 更新起点坐标，每次向右下方移动5个像素
            x0, y0 = x0 + 5, y0 + 5
            # 更新终点 y 坐标偏移量，每次增加5个像素
            y1 += 5
        mainloop()

    draw_spiral()

    print()
# --------------------------------------------------------------------------------
# 第26题：Python绘图入门3
def test26():
    """
    需求：使用Python的tkinter库来创建一个图形界面，并在其中绘制一个由矩形组成的螺旋形图案。
    """
    print("第26题：Python绘图入门3========================================")
    from tkinter import Canvas, BOTH, mainloop
    def draw_spiral():
        canvas = Canvas(width=400, height=400, bg="white")
        canvas.pack(expand=True, fill=BOTH)
        # 初始化第一个矩形的左上角坐标
        x0, y0 = 163, 163
        # 初始化第一个矩形的右下角坐标
        x1, y1 = 175, 175
        for i in range(19):
            canvas.create_rectangle(x0, y0, x1, y1)
            # 更新第一个矩形的左上角坐标，每次向左上方移动5个像素
            x0, y0 = x0-5, y0-5
            # 更新第一个矩形的右下角坐标，每次向右下方移动5个像素
            x1, y1 = x1+5, y1+5
        mainloop()

    draw_spiral()

    print()
#--------------------------------------------------------------------------------
# 第27题：导包生成随机数
def test27():
    """
    需求：编写一个程序，使用random模块来生成各种随机数
    """
    print("第27题：导包生成随机数========================================")
    #    函数                   作用
    #   .random()            生成 [0.0, 1.0) 范围内的随机小数
    #   .randint(a, b)       生成 [a, b] 范围内的随机整数
    #   .choice(seq)         从指定序列中随机选择一个元素
    #   .shuffle(list1)      将指定列表的元素进行随机排序(会修改原列表！)
    #   .sample(list1, n)    从指定列表中随机选择 n 个元素
    print("× 本章无控制台输出案例")

    print()
#--------------------------------------------------------------------------------
# 第28题：随机生成验证码
def test28():
    """
    需求：编写一个程序，该程序能够根据用户指定的长度随机生成一个验证码
          其中可包含大小写英文字母和数字
    """
    print("第28题：随机生成验证码========================================")
    import string, random
    def random_code(length):
        # 创建一个包含大小写字母和数字的字符串
        code_str = string.ascii_letters + string.digits
        # 创建一个空列表，用于存储生成的随机字符
        code_list = []
        # 使用循环生成指定长度的验证码
        for i in range(length):
            # 使用 random.choice() 方法从 code_str 中随机选择一个字符
            code_list.append(random.choice(code_str))
        # 将生成的字符列表转换为字符串并返回
        return "".join(code_list)

    print(random_code(8))

    print()
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()