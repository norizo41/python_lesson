"""
複数の選択肢から確率で選ぶ
参考：
https://www.haya-programming.com/entry/2018/03/31/174915
"""
import numpy as np

"""
a, b, c, dを[0.15, 0.35, 0.2, 0.3]の確率で選ぶ
"""
x = np.random.choice(['a', 'b', 'c', 'd'], p=[0.15, 0.35, 0.2, 0.3])
print(x)

"""
インデックスを返す確率を指定することもできる
"""
x = np.random.choice(4, p=[0.15, 0.35, 0.2, 0.3])
print(x)

"""
複数の結果も吐かせることも可能
"""
x = np.random.choice(4, size=10, p=[0.15, 0.35, 0.2, 0.3])
print(x)

"""
replaceというオプションがある。これは重複するかどうかを指定する
（福引ででた玉を一々中に戻すかどうかに相当）defaultはTrueで、
玉を中に戻すことに相当する。Falseにすると、1個ずつ玉を
取り出す操作に相当する。
"""
x = np.random.choice(5, 5)
print(x)

x = np.random.choice(5, 5, replace=False)
print(x)

"""
一定の確率で違う選択をする
参考：
https://www.haya-programming.com/entry/2018/02/06/152348
"""

"""
epsilonの確率で処理Aを行い、1-epsilonの確率で処理Bを行うメソッドを実装する
"""
from random import random
def p_select(epsilon):
    if epsilon > random():
        return True
    else:
        return False
# 確認のために10000回回し、TrueとFalseの数をカウントする。
lst = [p_select(0.2) for x in range(10000)]
print(lst.count(True))
print(lst.count(False))

