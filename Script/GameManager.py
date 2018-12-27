from Script.Tile import Tile
from Script.Tanks.testTank import testTank
from Script.Bullets.testBullet import testBullet
class GameManager:
    #This class is Singleton

    # _unique_instance = None


    # def __new__(cls):
    #     raise NotImplementedError('Cannot initialize via Constructor')

    # @classmethod
    # def __internal_new__(cls):
    #     return super().__new__(cls)

    # @classmethod
    # def getInstance(cls):
    #     if not cls._unique_instance:
    #         cls._unique_instance = cls.__internal_new__() 

    #     return cls._unique_instance

    def __init__(self):
        self.myTank = testTank()
        self.myTank.setPosition([0,0])

        self.myBullet = testBullet()
        self.myBullet.setPosition([0,1])
        
        self.enemyTank = testTank()
        self.enemyTank.setPosition([9,9])

        self.enemyBullet = testBullet()
        self.enemyBullet.setPosition([9, 8])
        
    
    def getTankImage(self):
        return [self.myTank.getImage(), self.enemyTank.getImage()]

    def getTankPosition(self):
        return [self.myTank.getPosition(),self.enemyTank.getPosition()]

    def getTankHP(self):
        return [self.myTank.getHP(), self.enemyTank.getHP()]

    def getBulletImage(self):
        return [self.myBullet.getImage(), self.enemyBullet.getImage()]
    
    def getBulletPosition(self):
        return [self.myBullet.getPosition(), self.enemyBullet.getPosition()]

    # def getBulletPoint(self):
    #     return [self.myBullet.getPoint(), self.enemyBullet.getPoint()]



    

