def getCommonDivisor(x, y):

    biggerNum = 0
    smallerNum = 0

    if x > y :
        biggerNum = x
        smallerNum = y
    else :
        biggerNum = y
        smallerNum = x
    
    # 大きいほうから小さいほうを割った余りを求める
    surplus = biggerNum % smallerNum

    # 割り切れていればそれを返す
    if surplus == 0 :
        return smallerNum
    
    # 割り切れてなければ再帰的に自信を呼び出す
    surplus = getCommonDivisor(smallerNum, surplus)

    return surplus

print(getCommonDivisor(390, 273))
print(getCommonDivisor(71, 57))
print(getCommonDivisor(506, 437))
print(getCommonDivisor(56, 84))