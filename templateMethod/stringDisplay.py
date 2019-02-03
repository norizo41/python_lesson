import sys
from abstractDisplay import AbstractDisplay

#StringDisplayは、AbstractDisplayのサブクラス
class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self.string = string
        self.length = len(self.string.encode('sjis'))

    def open(self):
        self.printLine()
    
    def print(self):
        print('|' + self.string + '|')

    def close(self):
        self.printLine()

    def printLine(self):
        sys.stdout.write('+')
        for i in range(self.length):
            sys.stdout.write('-')
        print('+')