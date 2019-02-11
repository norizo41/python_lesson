import sys
sys.path.append('../framework')
from product import Product

class IDCard(Product):
    def __init__(self, owner):
        self.__owner = owner

    def use(self):
        print('I use ' + self.__owner + '\'s card.')

    def getOwner(self):
        return self.__owner
