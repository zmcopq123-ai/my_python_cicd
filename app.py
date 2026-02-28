import math


def add(a, b):
    return a + b


def subtract(a, b):    # 函数之间要空2行
    return a - b


def multiply(a, b):    # 函数之间要空2行
    return a * b


def divide(a, b):      # 函数之间要空2行
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


def square_root(a):
    """开平方函数"""
    if a < 0:
        raise ValueError("不能对负数开平方")
    return math.sqrt(a)


if __name__ == "__main__":    # 函数和主程序之间也要空2行
    print("简单计算器")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 × 5 = {multiply(10, 5)}")
    print(f"10 ÷ 5 = {divide(10, 5)}")
    print(f"100 的开平方 = {square_root(100)}")

# 文件末尾要有一个空行（非常重要！）
