import math


def add(a, b):
    """+加法函数"""
    return a + b

def subtract(a, b):
    """-减法函数"""
    return a - b

def multiply(a, b):
    """乘法函数"""
    return a * b

def divide(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b

def square_root(a):
    """开平方函数"""
    if a < 0:
        raise  ValueError("不能对负数开平方")
    return math.sqrt(a)


if __name__ == "__main__":
    print("简单计算器")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 × 5 = {multiply(10, 5)}")
    print(f"10 ÷ 5 = {divide(10, 5)}")
    print(f"100 的开平方 = {square_root(100)}")