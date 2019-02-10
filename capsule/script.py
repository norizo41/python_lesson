class Obj:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.__num2 = num2

    def getNum2(self):
        return self.__num2

    def setNum2(self, num2):
        self.__num2 = num2

obj = Obj(3, 4)
print(obj.num1)
# print(obj.__num2) # 実行時エラー
print(obj.getNum2())
obj.setNum2(5)
print(obj.getNum2())
