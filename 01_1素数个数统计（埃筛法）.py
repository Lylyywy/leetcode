"""埃筛法"""
n = input("请输入一个整数\n")
count = 0

x = [False for i in range(int(n))]
for i in range(2, int(n)):
    if not x[i-1]:
        count += 1
        j = i * i  # 最简遍历方法
        while j < int(n):  # 将x数组下标为i的整数倍的都不执行count++，i从2到n
            x[j-1] = True
            j += i
print("小于"+str(n)+"的素数个数有：", count)
