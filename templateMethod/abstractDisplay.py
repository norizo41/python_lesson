"""
Pythonでは抽象クラスをABC(Abstract Base Class
-抽象基底クラス)モジュールを使用して実装することができる
"""
# ABCは標準モジュール
from abc import ABCMeta, abstractmethod

#抽象クラス
class AbstractDisplay(metaclass=ABCMeta):

    #抽象メソッド
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def print(self):
        pass
    @abstractmethod
    def close(self):
        pass
    
    #PythonにはJavaのfinal修飾子にあたるものがない！
    def display(self):
        self.open()
        for i in range(0, 5):
            self.print()
        self.close()
