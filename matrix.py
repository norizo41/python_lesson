# 行列、ベクトルの計算をハンズオン
# 参考サイト
# https://note.nkmk.me/python-numpy-matrix/
# ライブラリは「pip install [パッケージ名]」を実行することで取り込める
# 今回であれば「pip install numpy」を実効

import numpy as np

# 1.リストの要素としてリストを指定すれば
# 二次元の配列となる。
l_2d = [[0, 1, 2], [3, 4, 5]]
print(l_2d)
print(type(l_2d))
# [[0, 1, 2], [3, 4, 5]]
# <class 'list'>

# 2. numpy.ndarrayはnumpy.array()で生成できる。
# 第一引数にPythonのリストなどを渡す。
arr = np.array([[0, 1, 2], [3, 4, 5]])
print(arr)
print(type(arr))
# [[0 1 2]
#  [3 4 5]]
# <class 'numpy.ndarray'>

# 3. numpy.array()のほかには等差数列を生成する関数
# np.arange()などでもndarrayを生成できる。
# さらに、reshape()メソッドで形状を変更したりすることも可能。
arr = np.arange(6)
print(arr)
# [0 1 2 3 4 5]
arr = np.arange(6).reshape((2, 3))
print(arr)
# [[0 1 2]
#  [3 4 5]]

# 4. Numpy行列numpy.matrixはコンストラクタnumpy.matrix()で生成できる。
mat = np.matrix([[0, 1, 2], [3, 4, 5]])
print(mat)
print(type(mat))
# [[0 1 2]
#  [3 4 5]]
# <class 'numpy.matrixlib.defmatrix.matrix'>
mat = np.matrix(arr)
print(mat)
print(type(mat))
# [[0 1 2]
#  [3 4 5]]
# <class 'numpy.matrixlib.defmatrix.matrix'>

# 5. コンストラクタの引数に一次元配列を渡すと二次元配列に
# 拡張され、三次元以上の配列を渡すとエラーになる。
mat_1d = np.matrix([0, 1, 2])
print(mat_1d)
print(type(mat_1d))
print(mat_1d.shape)
# [[0 1 2]]
# <class 'numpy.matrixlib.defmatrix.matrix'>
# (1, 3)
# mat_3d = np.matrix([[[0, 1, 2]]])
# ValueError: matrix must be 2-dimensional

# 6. Pythonリスト型の二次元配列の要素の値は
# list[行番号][列番号]でアクセスできる。
# 行番号・列番号は0始まり。値を取得することも、変更（代入）することもできる。
print(l_2d[0][1])
# 1
l_2d[0][1] = 100
print(l_2d)
# [[0, 100, 2], [3, 4, 5]]

# 7. numpy.ndarray, numpy.matrixは、arr[行番号][列番号]
# またはarr[行番号, 列番号]でアクセスできる。
# 行番号・列番号は0始まり。値を取得することも、変更（代入）することもできる。
# 以下の例はndarrayだが、matrixでも同様。
print(arr[0][1])
# 1
print(arr[0, 1])
# 1
arr[0, 1] = 100
print(arr)
# [[  0 100   2]
# [  3   4   5]]

# 8. Pythonリスト型の二次元配列の転置行列は以下のように取得できる。
l_2d = [[0, 1, 2], [3, 4, 5]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5]]
l_2d_t = [list(x) for x in list(zip(*l_2d))]
print(l_2d_t)
# [[0, 3], [1, 4], [2, 5]]

# 9. numpy.ndarrayとnumpy.matrixは.Tで転置行列を取得できる。
# 以下の例はndarrayだが、matrixでも同様。
arr = np.arange(6).reshape((2, 3))
print(arr)
# [[0 1 2]
# [3 4 5]]
arr_t = arr.T
print(arr_t)
#[[0 3]
# [1 4]
# [2 5]]

# 10. Pythonリスト型では、+演算子はリストの結合となり、
# -演算子に対する処理は定義されていないためエラーになる
l_2d_1 = [[0, 1, 2], [3, 4, 5]]
l_2d_2 = [[0, 2, 4], [6, 8, 10]]
l_2d_sum = l_2d_1 + l_2d_2
print(l_2d_sum)
# [[0, 1, 2], [3, 4, 5], [0, 2, 4], [6, 8, 10]]
# l_2d_sub = l_2d_1 - l_2d_2
# TypeError: unsupported operand type(s) for -: 'list' and 'list'

# 11. numpy.ndarrayとnumpy.matrixでは、
# +演算子と-演算子で各要素がそれぞれ加算・減算される。
arr1 = np.arange(6).reshape((2, 3))
print(arr1)
# [[0 1 2]
#  [3 4 5]]
arr2 = np.arange(0, 12, 2).reshape((2, 3))
print(arr2)
# [[ 0  2  4]
#  [ 6  8 10]]
arr_sum = arr1 + arr2
print(arr_sum)
# [[ 0  3  6]
#  [ 9 12 15]]
arr_sub = arr1 - arr2
print(arr_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]
mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)
mat_sum = mat1 + mat2
print(mat_sum)
# [[ 0  3  6]
#  [ 9 12 15]]
mat_sub = mat1 - mat2
print(mat_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

# 12. Pythonリスト型では、数値ごとの*演算ははいれつを
# 繰り返しとなり、リスト同士の*演算は定義されていない
l_2d_mul = l_2d_1 * 2
print(l_2d_mul)
# [[0, 1, 2], [3, 4, 5], [0, 1, 2], [3, 4, 5]]
# l_2d_mul = l_2d_1 * l_2d_2
# TypeError: can't multiply sequence by non-int of type 'list'

# 13. numpy.ndarrayとnumpy.matrixでは、
# 数値との*演算はスカラー倍となる
arr_mul = arr1 * 2
print(arr_mul)
# [[ 0  2  4]
#  [ 6  8 10]]
mat_mul = mat1 * 2
print(mat_mul)
# [[ 0  2  4]
#  [ 6  8 10]]

# 14. 行列同士の要素ごとの積（アダマール積）を取得するには
# numpy.multiply() を使う
arr_mul = arr1 * arr2
print(arr_mul)
# [[ 0  2  8]
#  [18 32 50]]

# 15. 行列の積を算出するには、numpy.dot(), numpy.matmul(),
# @演算子を使う。
# @演算子はPython3.5, Numpy1.10.0以降で利用可能で、numpy.matmul()と等価
# dot()は関数だけでなくメソッドとしても用意されている
arr1 = np.arange(4).reshape((2, 2))
print(arr1)
# [[0 1]
#  [2 3]]
arr2 = np.arange(6).reshape((2, 3))
print(arr2)
# [[0 1 2]
#  [3 4 5]]
arr_mul_matrix = np.dot(arr1, arr2)
print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]
arr_mul_matrix = arr1.dot(arr2)
print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]
arr_mul_matrix = np.matmul(arr1, arr2)
print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]
arr_mul_matrix = arr1 @ arr2
print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)
mat_mul_matrix = np.dot(mat1, mat2)
print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]
# mat_mul_matrix = mat1.dot(mat2)
print(mat_mul_matrix)
# [[ 3  4  5]
# [ 9 14 19]]
mat_mul_matrix = np.matmul(mat1, mat2)
# [[ 3  4  5]
# [ 9 14 19]]
mat_mul_matrix = mat1 @ mat2
print(mat_mul_matrix)
# [[ 3  4  5]
# [ 9 14 19]]
# num.matrixでは、*演算子でも行列の積が算出される
mat_mul_matrix = mat1 * mat2
print(mat_mul_matrix)
# [[ 3  4  5]
# [ 9 14 19]]


