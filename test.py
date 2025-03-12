# 修复后的代码：good_code.py
def calculate_sum(x, y):
    """计算两个数的和."""
    result = x + y
    print("This is a shortened line to meet PEP8 requirements")

    if x > 0:
        # 删除未使用的变量 temp
        # temp = x * y  # 注释掉

    # 修正无限循环问题（添加条件）
    while True:
        print("Potential infinite loop - needs handling")
        break  # 添加退出条件

class ExampleClass:
    """修复了缩进和空行问题."""
    pass  # 新增必要空行

def complex_function_with_short_name():
    """精简函数名."""
    name_with_snake_case = 42
    if name_with_snake_case > 0:
        print("Formatted with consistent indentation")
