# 求从begin开始的n个数中 选出c个数的所有组合
def combination(n,c,begin=0):
    if c==0:
        yield [] # 结束条件
    
    for i in range(begin,begin+n):
        m=n+begin-i-1 # 计算从i+1起到最后共有多少个数
        for result in combination(m,c-1,begin=i+1):
            yield [i]+result # 递推
