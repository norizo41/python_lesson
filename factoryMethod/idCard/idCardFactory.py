import sys
sys.path.append('../framework')
from factory import Factory
from product import Product
from idCard import IDCard

class IDCardFactory(Factory):
    def __init__(self):
        self.__owners = []

    def createProduct(self, owner):
        return IDCard(owner)

    def registerProduct(self, product):
        self.__owners.append(product.getOwner())

    def getOwners(self):
        return self.__owners
