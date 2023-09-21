import math
"""暴力算法"""
def isPrime(prime_n):
    if prime_n < 2:
        return False  # 小于2的数不是素数（负数、0、1）
    for prime_i in range(2, int(math.sqrt(prime_n) + 1)):
        if prime_n % prime_i == 0:
            return False
    return True

n = 10000  # 输入值
count = 0  # 个数
for i in range(2, n):
    count += isPrime(i)  # 暴力算法
print("小于"+str(n)+"的素数个数有：", count)
