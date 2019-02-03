# 図書委員の中村くん
from bookList import BookList
from lendingList import LendingList

class Librarian:
    def searchBook(self, bookName):
        # 本を探す
        bookList = BookList()
        location = bookList.searchBook(bookName)
        # 本の場所がNoneではない（所蔵している）とき
        if not location:
            # 貸出中かチェックする
            lendingList = LendingList()
            if lendingList.check(bookName) :
                #貸出中のとき
                return '貸出中です'
            else:
                #貸出中でないとき
                return location
        # 貯蔵していないとき
        else:
            return 'その本は所蔵していません'