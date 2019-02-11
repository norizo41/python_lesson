import sys
from abstractDisplay import AbstractDisplay

#StringDisplayは、AbstractDisplayのサブクラス
class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self.__string = string
        self.__length = len(self.__string.encode('sjis'))

    def open(self):
        self.printLine()
    
    def print(self):
        print('|' + self.__string + '|')

    def close(self):
        self.printLine()

    def printLine(self):
        sys.stdout.write('+')
        for i in range(self.__length):
            sys.stdout.write('-')
        print('+')
