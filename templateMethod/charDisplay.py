import sys
from abstractDisplay import AbstractDisplay

#CharDisplayは、AbstractDisplayのサブクラス
class CharDisplay(AbstractDisplay):

    def __init__(self, char):
        self.__char = char

    def open(self):
        sys.stdout.write('<<')
    
    def print(self):
        sys.stdout.write(self.__char)

    def close(self):
        print('>>')
