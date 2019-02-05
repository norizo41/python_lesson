# 因数分解、方程式、微分積分の計算をハンズオン
# 参考サイト
# https://note.nkmk.me/python-sympy-factorization-solve-equation/
# ライブラリは「pip install [パッケージ名]」を実行することで取り込める
# 今回であれば「pip install sympy」を実効

import sympy
# ライブラリ名とファイル名は重複しないように！！！
# （ex 「sympy.py」という名前を付けたら参照されなくなる）

# 1. 変数は以下のようにsympy.Symbol()で定義する
x = sympy.Symbol('x')
y = sympy.Symbol('y')
print(type(x))

# 2. その変数を使って自由に数式を定義できる。
# 四則演算（+, -, *, /）、べき乗（**）などの演算子は
# Python標準のものを使う。
expr = x**2 + y +1
print(expr)
# x**2 + y + 1
# 変数の名称とsympy.symbol()の引数に渡す文字列は違っていてもいいが、
# 分かりにくくなるだけなので、同じものにしておいたほうが無難。
z = sympy.Symbol('zzzz')
expr_z = z**2 + 3 + 3 * z
print(expr_z)
# zzzz**2 + 3*zzzz + 3

# 3.定義した式の変数に値を代入したい場合はsubs()メソッドを使う。
# 第一引数に対象の変数、第二引数に代入する値を指定する。
# 数値を代入したり、ほかの変数を代入したりできる。
print(expr)
# x**2 + y + 1
print(expr.subs(x, 1))
# y + 2
print(expr.subs(x, y))
# y**2 + y + 1
# 複数の変数に式を代入する場合は、（変数、代入する値）の
# タプルのリストを引数に指定する。
print(expr.subs([(x, 1), (y, 2)]))
# 4

# 4. 式を定義しただけだと自動的に展開されたりはしない。
# 式を展開したい場合はsympy.expand()を使う。
expr = (x + 1)**2
print(expr)
# (x + 1)**2
expr_ex = sympy.expand(expr)
print(expr_ex)
# x**2 + 2*x + 1

# 5. 因数分解したい場合はsyspy.factor()を使う。
# いくつか例を示す。変数が複数あってもよい。
print(expr_ex)
# x**2 + 2*x + 1
expr_factor = sympy.factor(expr_ex)
print(expr_factor)
# (x + 1)**2
print(sympy.factor(x**3 - x**2 - 3 * x + 3))
# (x - 1)*(x**2 - 3)
print(sympy.factor(x * y + x + y + 1))
# (x + 1)*(y + 1)

# 6. 方程式を解く（方程式の解を取得する）場合は
# sympy.solve()を使う。
# sympy.solve(式)で式 = 0とした場合の解が取得できる。
# 平方根（ルート）はsqrt、虚数単位はIで表される。
# （sqrtはsquare rootの略）
print(sympy.solve(x**2 - 3 * x + 2))
# [1, 2]
print(sympy.solve(x**2 + x + 1))
# [-1/2 - sqrt(3)*I/2, -1/2 + sqrt(3)*I/2]

# 7. 連立方程式を解く場合もsympy.solve()を使う。
# 複数の式を含むリスト（またはタプル）をsympy.solve()
# の引数に指定すればOK。
expr1 = 3 * x + 5 * y -29
expr2 = x + y - 7
print(sympy.solve([expr1, expr2]))
# {x: 3, y: 4}

# 8. 複数の変数を含む式において、任意の変数に対して解を
# 取得することができる。第二引数に対象の変数を指定する。
expr = x + y**2 - 4
print(sympy.solve(expr, x))
# [-y**2 + 4]
print(sympy.solve(expr, y))
# [-sqrt(-x + 4), sqrt(-x + 4)]

# 9. 式の微分をするにはsympy.diff()を使う。
print(sympy.diff(x**3 + 2 * x**2 + x))
# 3*x**2 + 4*x + 1

# 10. 複数の変数を含む式において、任意の変数に対して
# 微分することもできる。第二引数に対象の変数を指定する。
expr = x**3 + y**2 -y
print(sympy.diff(expr, x))
# 3*x**2
print(sympy.diff(expr, y))
# 2*y - 1

# 10. 式の積分をするにはsympy.integrate()を使う。
print(sympy.integrate(3*x**2 + 4*x + 1))
# x**3 + 2*x**2 + x

# 11. 三角関数、指数関数、対数関数などはsympy.sin(), sympy.exp()
# sympy.log()のように定義されている。
# 微分や積分も可能。
print(sympy.diff(sympy.cos(x)))
# -sin(x)
print(sympy.diff(sympy.sin(x)))
# cos(x)
print(sympy.diff(sympy.exp(x)))
# exp(x)
print(sympy.diff(sympy.log(x)))
# 1/x
print(sympy.integrate(sympy.cos(x)))
# sin(x)
print(sympy.integrate(sympy.sin(x)))
# -cos(x)
print(sympy.integrate(sympy.exp(x)))
# exp(x)
print(sympy.integrate(sympy.log(x)))
# x*log(x) - x
