module_name = "custom_module"

__all__ = ["add"]

def add(a,b):
    print(f"{a}+{b}的结果为：{a+b}")
def sub(a,b):
    print(f"{a}-{b}的结果为：{a-b}")

if __name__ == "__main__":
    print(f"{module_name}模块被直接运行")
else:
    print(f"{module_name}模块被其他模块导入")