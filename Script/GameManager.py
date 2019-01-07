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
         
        # self.tileList = [[Tile(25, w*25, h*25) for h in range(mapSize)]
        #                         for w in range(mapSize)]

        self.myTank = testTank()
        self.myTank.setPosition([0,0])

        
        self.enemyTank = testTank()
        self.enemyTank.setPosition([9,9])


        self.bullet_list = list()
        # self.myBullet = testBullet([0, 4], [9,8])
        # self.myBullet.setPosition([9, 8])

        # self.bullet_list.append(self.myBullet)

        # self.enemyBullet = testBullet([9,6],[0,9])
        # self.enemyBullet.setPosition([0, 9])

        #self.bullet_list.append(self.enemyBullet)

        # self.enemyBullet2 = testBullet([9,8],[9,9])
        # self.enemyBullet2.setPosition([9, 9])

       #self.bullet_list.append(self.enemyBullet2)

       #turn
        self.turn = 99

        self.connect = TCPClient()

       #count
        self.button_count = 0 
    
    def load(self):
        data = self.createData()
        self.sendData(data)

    def read(self):
        data = self.createData()
        self.readData(data)


    def buttonFrame(self,pyxel_count):
        if pyxel_count > self.button_count:
           self.button_count = pyxel_count + 5
           return True
        return False


    def getTankImage(self):
        return [self.myTank.getImage(), self.enemyTank.getImage()]

    def getTankPosition(self):
        return [self.myTank.getPosition(),self.enemyTank.getPosition()]

    def getTankHP(self):
        return [self.myTank.getHP(), self.enemyTank.getHP()]

    def getTankMaxHP(self):
        return [self.myTank.getMaxHP(), self.enemyTank.getMaxHP()]

    def getBulletImage(self):
        #return [self.myBullet.getImage(), self.enemyBullet.getImage()]
        return [bullet.getImage() for bullet in self.bullet_list]

    def getBulletPosition(self):
        #return [self.myBullet.getPosition(), self.enemyBullet.getPosition()]
        return [bullet.getPosition() for bullet in self.bullet_list]
    
    def getBulletPoint(self):
        #return [self.myBullet.getPosition(), self.enemyBullet.getPosition()]
        return [bullet.getPoint() for bullet in self.bullet_list]
    
    def getBulletOrbit(self):
        #return [self.myBullet.getPosition(), self.enemyBullet.getPosition()]
        return [bullet.getOrbit() for bullet in self.bullet_list]

    def isBullet(self):
        return bool(self.bullet_list)
    
    def getTurn(self):
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
    
    def pressSpace(self, bulletPoint):
        bulletType = self.myTank.launchBullet()
        pos = [self.myTank.getPosition()[0], self.myTank.getPosition()[1]]
        bullet = testBullet(bulletPoint, pos)
        bullet.setPosition(pos)
        bullet.setOrbit(pos)
        self.bullet_list.append(bullet)

    def setPoint(self,bulletPoint):
        #bulletPointには[0,4]みたいにタイルの位置を引数にとってください
        bulletType = self.myTank.launchBullet()
        pos = [self.myTank.getPosition()[0], self.myTank.getPosition()[1]]
        bullet = testBullet(bulletPoint, pos)
        bullet.setPosition(pos)
        bullet.setOrbit(pos)
        self.bullet_list.append(bullet)

        

    def bulletMove(self):
        for bullet in self.bullet_list:
            bullet.move()
            print("bulletMovePos" + str(bullet.getPosition()))
        # import pdb
        # pdb.set_trace()

    def confirmHP(self):
        if self.myTank.getHP() <= 0 and self.enemyTank.getHP() <= 0:
           return "draw"
        elif self.enemyTank.getHP() <= 0:
           return "you win"
        elif self.myTank.getHP() <= 0:
           return "you lose"
            



    #battle calc 
    # must process after bulletMove()
    def calcDamage(self):
        arrival_bullets = []
        for i ,bullet in enumerate(self.bullet_list):
            if bullet.getArrival():
                arrival_bullet = self.bullet_list[i]
                
                #explosion
                myTankPos = self.myTank.getPosition()
                enemyTankPos = self.enemyTank.getPosition()

                #MyTank calc
                if (arrival_bullet.getPoint() == myTankPos) or \
                    ([arrival_bullet.getPoint()[0] + 1, arrival_bullet.getPoint()[1]] == myTankPos) or \
                    ([arrival_bullet.getPoint()[0] + 1, arrival_bullet.getPoint()[1] - 1] == myTankPos) or  \
                ([arrival_bullet.getPoint()[0], arrival_bullet.getPoint()[1] - 1] == myTankPos) or \
                ([arrival_bullet.getPoint()[0] -1, arrival_bullet.getPoint()[1] -1 ] == myTankPos) or \
                ([arrival_bullet.getPoint()[0] -1, arrival_bullet.getPoint()[1]] == myTankPos) or \
                ([arrival_bullet.getPoint()[0] -1, arrival_bullet.getPoint()[1] + 1] == myTankPos) or \
                    ([arrival_bullet.getPoint()[0], arrival_bullet.getPoint()[1] + 1] == myTankPos) or \
                ([arrival_bullet.getPoint()[0] + 1, arrival_bullet.getPoint()[1] + 1] == myTankPos) :
                    self.myTank.calcDamage(arrival_bullet.getDamage())

                if (arrival_bullet.getPoint() == enemyTankPos) or \
                ([arrival_bullet.getPoint()[0] + 1, arrival_bullet.getPoint()[1]] == enemyTankPos) or \
                    ([arrival_bullet.getPoint()[0] + 1, arrival_bullet.getPoint()[1] - 1] == enemyTankPos) or \
                    ([arrival_bullet.getPoint()[0], arrival_bullet.getPoint()[1] - 1] == enemyTankPos) or \
                    ([arrival_bullet.getPoint()[0] - 1, arrival_bullet.getPoint()[1] - 1] == enemyTankPos) or \
                ([arrival_bullet.getPoint()[0] - 1, arrival_bullet.getPoint()[1]] == enemyTankPos) or \
                ([arrival_bullet.getPoint()[0] - 1, arrival_bullet.getPoint()[1] + 1] == enemyTankPos) or \
                    ([arrival_bullet.getPoint()[0], arrival_bullet.getPoint()[1] + 1] == enemyTankPos) or \
                ([arrival_bullet.getPoint()[0] + 1, arrival_bullet.getPoint()[1] + 1] == enemyTankPos):
                    self.enemyTank.calcDamage(arrival_bullet.getDamage())

                arrival_bullets.append(arrival_bullet)
        
        return arrival_bullets

    def bulletsPop(self):
        for i ,bullet in enumerate(self.bullet_list):
         if bullet.arrivalCheck():
                self.bullet_list.pop(i)
    
    def bulletExplosion(self):
        bullets = list()
        for bullet in self.bullet_list:
           if bullet.arrivalCheck():
               bullets.append(bullet)
        return bullets
        
               

    #data
    def createData(self):
        data = TCPData()
        # print("dataset2:"+str(self.getBulletPosition()) +
        #       ":" + str(self.getBulletPoint()))
        # import pdb
        # pdb.set_trace()
        data.setData(1, self.getTankPosition()[0], self.getTankHP()[0], [1], self.getBulletPosition(), self.getBulletPoint(
        ), 1, self.getTankPosition()[1], self.getTankHP()[1], self.getBulletOrbit(), self.getBulletPosition(), self.getBulletPoint(
        ), self.turn)
        return data

    def setData(self,data):
        self.turn = int(data.getMyTurn())
        self.myTank.setPosition(data.getEnemyTankPosition())
        self.enemyTank.setPosition(data.getMyTankPosition())
        self.myTank.setHP(data.getEnemyTankHP())
        self.enemyTank.setHP(data.getMyTankHP())
        
        # print("dataset:"+str(data.getMyBulletPosition()) +
        #       ":" + str(data.getMyBulletPoint()))

        self.bullet_list = list()
        for  bulletPos,bulletPoint,bulletOrbit in zip(data.getMyBulletPosition(),data.getMyBulletPoint(),data.getEnemyBulletType()):
            bullet = testBullet(bulletPoint,bulletOrbit)
            bullet.setPosition(bulletPos)
            bullet.setOrbit(bulletOrbit)
            #bullet.setPoint(bulletPoint)
            self.bullet_list.append(bullet)
        
            

    def sendData(self,data):
        rtData = self.connect.connecting(data)
        self.setData(rtData)

    def readData(self,data):
        self.changeTurn()
        self.connect.connecting(data)
        #self.setData(rtData)
    
    # def calcTilePosition(self,pos):
    #     tile = self.tileList[pos[0]][pos[1]]
    #     return [tile.getCenterPosX(), tile.getCenterPosY()]


    # def getBulletPoint(self):
    #     return [self.myBullet.getPoint(), self.enemyBullet.getPoint()]



    

