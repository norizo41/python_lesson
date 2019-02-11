from abc import ABCMeta, abstractmethod
from product import Product

class Factory(metaclass=ABCMeta):
    
    def create(self, owner):
        p = self.createProduct(owner)
        self.registerProduct(p)
        return p

    @abstractmethod
    def createProduct(self, owner):
        pass

    @abstractmethod
    def registerProduct(self, product):
        pass


