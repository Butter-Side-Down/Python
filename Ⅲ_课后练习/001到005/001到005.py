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
    test18()                       # 第18题：求质因数
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
          请找出年龄最大者的姓名与年龄，并将其打印出来
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
            return sum(1 / i for i in range(1, n + 1, 2))
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


    print()
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()