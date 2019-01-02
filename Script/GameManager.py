#network
from Script.networking.TCPClient import TCPClient
from Script.networking.TCPData import TCPData

#tile
from Script.Tile import Tile

#tank
from Script.Tanks.testTank import testTank

#bullet
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

        self.myBullet = testBullet([0,3])
        self.myBullet.setPosition([0,1])
        
        self.enemyTank = testTank()
        self.enemyTank.setPosition([9,9])

        self.enemyBullet = testBullet([0,3])
        self.enemyBullet.setPosition([9, 8])

       #turn
        self.turn = 99

        self.connect = TCPClient()
    
    def load(self):
        data = self.createData()
        self.sendData(data)


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

    def getTurn(self):
        print(self.turn)
        return self.turn
    
    def changeTurn(self):
        if self.turn == 1:
            self.turn = 0
        elif self.turn == 0:
            self.turn = 1

        return self.turn

    def pressLeft(self):
        self.myTank.moveLeft()
    
    def pressRight(self):
        self.myTank.moveRight()
    
    def pressUp(self):
        self.myTank.moveUp()

    def pressDown(self):
        self.myTank.moveDown()
    
    # def pressSpace(self):
    #     self.myTank.launchBullet()

    def createData(self):
        data = TCPData()
        data.setData(1, self.getTankPosition()[0], self.getTankHP()[0], [1], self.getBulletPosition()[0], [0], 1, self.getTankPosition()[1], self.getTankHP()[1], [1], self.getBulletPosition()[1], [0],self.turn)
        return data

    def setData(self,data):
        print("setData:" + str(data.getMyTankPosition()))
        self.turn = int(data.getMyTurn())
        self.myTank.setPosition(data.getEnemyTankPosition())
        self.enemyTank.setPosition(data.getMyTankPosition())

    def sendData(self,data):
        print("data" + data.pushData())
        rtData = self.connect.connecting(data)
        print("rtData" + rtData.pushData())
        self.setData(rtData)
    

    # def getBulletPoint(self):
    #     return [self.myBullet.getPoint(), self.enemyBullet.getPoint()]



    

