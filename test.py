# 文件名: bad_code.py

def calculateSum(x, y):
    result= x + y
    print("This is a very long line that should exceed PEP8 line length limit. It is an example of violation") # 没有空格

    if x > 0:
        temp = x * y  # 未使用的变量 'temp'

    while True:
        print("Infinite loop! 引入非ASCII字符")  # 无限循环
    return result  # 缩进错误（应该在函数内对齐）

class ExampleClass():
    pass        # 行尾有多余空格

def ComplexFunctionWith way_too_LongName():
    """函数名和文档字符串不符合规范"""
    NameWithCamelCase = 42    # 变量命名不符合 snake_case
    #
    # 错误的缩进层级（空行但缩进混乱）
    if NameWithCamelCase > 0:
        #
        # 过多的空行和缩进不一致
        print("This is an example with multiple style issues") 
    #
# 文件结束
