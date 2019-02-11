from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):

    # 何はともあれuseできるもの
    @abstractmethod
    def use(self):
        pass
