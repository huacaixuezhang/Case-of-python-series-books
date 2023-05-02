from random import randint
class Die:
    """表示一个股子的类"""
    def __init__(self,num_sides=6):
        self.num_sides=num_sides

    def roll(self):
        """返回一个位于 1和股子面数之间的随机数"""
        return randint(1,self.num_sides)
