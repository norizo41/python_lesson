"""
自作クラスの演算子の振る舞いを定義したい
参考：
https://www.lifewithpython.com/2014/06/python-redefine-operators.html
"""


class Array:
    def __init__(self, values):
        """
        valuesには数字を格納したリストを渡す
        """
        self.values = values

    def __add__(self, other):
        """
        +演算子を定義するメソッド
        values内の要素同士を足し合わせた新しいArrayインスタンスを返す
        """
        """
        mapはJavaでいうところのラムダ式。
        台2, 3引数を第一引数で受け取り、関数addを実行する
        """
        m = map(lambda x, y: x + y, self.values, other.values)
        """
        mapのままだと出力時iterator objectと呼ばれるものを返すため、
        listに変換する
        """
        l = list(m)
        return Array(l)

    def __mul__(self, other):
        """
        *演算子を定義するメソッド
        values内の要素同士をかけ合わせた
        新しいArrayインスタンスを返す
        """
        return Array(list(map(lambda x, y: x * y,
                            self.values,
                            other.values)))

m1 = Array([3, 5])
m2 = Array([10, 11])

m3 = m1 + m2
print(m3.values)

m4 = m1 * m2
print(m4.values)

"""
ほかにも、+=に対応した__iadd__、引き算に対応した__sub__、
/ に対応した__truediv__がある
"""
