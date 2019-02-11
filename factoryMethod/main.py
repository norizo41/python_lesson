import sys
sys.path.append('./framework')
sys.path.append('./idCard')

from idCard import IDCard
from idCardFactory import IDCardFactory

factory = IDCardFactory()
card1 = factory.create('Yuki')
card2 = factory.create('Tomura')
card3 = factory.create('Satoh')

card1.use()
card2.use()
card3.use()

