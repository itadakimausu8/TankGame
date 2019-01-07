import pyxel
from Script.Tile import Tile
from Script.Tanks.testTank import testTank
from Script.Bullets.testBullet import testBullet
from Script.GameManager import GameManager


class ClientGUI:

    mapSize = 10

    def __init__(self):
        self.isLoad = False
        self.turnText = ""
        pyxel.init(255, 255, caption="Tank Game")
        self.GM = GameManager()
        #pyxel.load("assets/tile.pyxel")
        self.tileList = [[Tile(25, w*25, h*25) for h in range(ClientGUI.mapSize)]
                         for w in range(ClientGUI.mapSize)]

        self.confirmDraw = False
        self.isBulletMove = False

        #add
        self.gameText = ""
        self.winText = [0, 5]
        self.loseText = [0, 50]
        self.drawText = [0, 105]

        self.oldMyTankX = 0
        self.oldMyTankY = 0
        self.oldEnemyTankX = 0
        self.oldEnemyTankY = 0

        self.myTankAngle = [0, 0]
        #self.enemyTankAngle=[0,0]
        self.rightTank = [0, 0]
        self.upperTank = [25, 0]
        self.leftTank = [50, 0]
        self.lowerTank = [75, 0]

        self.bulletSuggest = False
        self.targetX = 0
        self.targetY = 0
        self.currentMyTankX = 0
        self.currentMyTankY = 0

        self.bullets = []
        self.bulletsPlace = [0, 0]
        #爆発描写用
        self.ex = 0
        self.ey = 0
        self.currentFrames = 0

        #名前用
        self.enemyTankAngleUpper = 0
        self.enemyTankAngleRight = 1
        self.enemyTankAngleLower = 2
        self.enemyTankAngleLeft = 3
        self.enemyTankAngle = 0
        self.bulletAngle = [0, 0]
        self.bulletAngleUpper = [0, 125]
        self.bulletAngleUpperRight = [25, 125]
        self.bulletAngleRight = [50, 125]
        self.bulletAngleLowerRight = [75, 125]
        self.bulletAngleLower = [0, 100]
        self.bulletAngleLowerLeft = [25, 100]
        self.bulletAngleLeft = [50, 100]
        self.bulletAngleUpperLeft = [75, 100]

        #create testTank
        #self.test = testTank()
        pyxel.image(0).load(0, 0, self.GM.getTankImage()[0])
        #self.test.setPosition([2,2])

        #create testBullet


        pyxel.image(0).load(0, 0, "assets/gameText.png")
        pyxel.image(1).load(0, 0, "assets/bullet_16x16.png")
        pyxel.image(2).load(0, 0, "assets/tileset25.png")

        self.GM.load()
        pyxel.run(self.update, self.draw)

    def update(self):

        self.currentMyTankX = self.GM.getTankPosition()[0][0]
        self.currentMyTankY = self.GM.getTankPosition()[0][1]

        if self.isLoad:
            #self.GM.bulletsPop()
            self.GM.load()
            self.GM.calcDamage()
            self.bullets = self.GM.bulletExplosion()
            self.isLoad = False

        #operate tank
        if self.confirmDraw:
               self.turnText = "EnemyTurn"
               self.oldEnemyTankX = self.GM.getTankPosition()[1][0]
               self.oldEnemyTankY = self.GM.getTankPosition()[1][1]
               if self.isBulletMove:
                  self.GM.bulletMove()
                  #add test
                  self.GM.calcDamage()
                  self.bullets = self.GM.bulletExplosion()

                  self.isBulletMove = False
        else:
            if self.GM.getTurn() == 0:
                    self.turnText = "MyTurn"
                    #print("myTurn")
                    #print("btn possible")
                    if pyxel.btnp(pyxel.KEY_Q):
                        self.bulletSuggest = False

                    if pyxel.btnp(pyxel.KEY_LEFT) and self.GM.buttonFrame(pyxel.frame_count):
                        if self.bulletSuggest == True:
                            if self.targetX > 0 and not (self.currentMyTankX == self.targetX-1 and self.currentMyTankY == self.targetY):
                                self.targetX -= 1
                        else:
                            self.GM.pressLeft()
                            self.myTankAngle = self.leftTank
                            self.isBulletMove = True
                            self.confirmDraw = True
                            # self.GM.load()
                    elif pyxel.btnp(pyxel.KEY_RIGHT) and self.GM.buttonFrame(pyxel.frame_count):
                        if self.bulletSuggest == True:
                            if self.targetX < self.mapSize-1 and not (self.currentMyTankX == self.targetX+1 and self.currentMyTankY == self.targetY):
                                self.targetX += 1
                        else:
                            self.GM.pressRight()
                            self.myTankAngle = self.rightTank
                            self.isBulletMove = True
                            self.confirmDraw = True
                            # self.GM.load()
                    elif pyxel.btnp(pyxel.KEY_UP) and self.GM.buttonFrame(pyxel.frame_count):
                        if self.bulletSuggest == True:
                            if self.targetY > 0 and not (self.currentMyTankY == self.targetY-1 and self.currentMyTankX == self.targetX):
                                self.targetY -= 1
                        else:
                            self.GM.pressUp()
                            self.myTankAngle = self.upperTank
                            self.isBulletMove = True
                            self.confirmDraw = True
                            # self.GM.load()
                    elif pyxel.btnp(pyxel.KEY_DOWN) and self.GM.buttonFrame(pyxel.frame_count):
                        if self.bulletSuggest == True:
                            if self.targetY < self.mapSize-1 and not (self.currentMyTankY == self.targetY+1 and self.currentMyTankX == self.targetX):
                                self.targetY = self.targetY+1
                        else:
                            self.GM.pressDown()
                            self.myTankAngle = self.lowerTank
                            self.isBulletMove = True
                            self.confirmDraw = True
                            # self.GM.load()
                    elif pyxel.btnp(pyxel.KEY_SPACE):
                        if self.bulletSuggest == True:
                            self.GM.pressSpace([self.targetX, self.targetY])
                            self.isBulletMove = True
                            self.bulletSuggest = False
                            self.confirmDraw = True
                            # self.GM.load()
                        else:
                            if self.currentMyTankX == 4 and self.currentMyTankY == 4:
                                self.targetX = 4
                                self.targetY = 5
                            else:
                                self.targetX = 4
                                self.targetY = 4
                            self.bulletSuggest = True
            elif self.GM.getTurn() == 1:
                self.GM.load()
                self.bullets = self.GM.bulletExplosion()
                self.GM.bulletsPop()
                if self.oldEnemyTankX > self.GM.getTankPosition()[1][0]:
                    self.enemyTankAngle = self.enemyTankAngleRight
                elif self.oldEnemyTankX < self.GM.getTankPosition()[1][0]:
                    self.enemyTankAngle = self.enemyTankAngleLeft
                elif self.oldEnemyTankY > self.GM.getTankPosition()[1][1]:
                    self.enemyTankAngle = self.enemyTankAngleUpper
                elif self.oldEnemyTankY < self.GM.getTankPosition()[1][1]:
                    self.enemyTankAngle = self.enemyTankAngleLower
            else:
                self.turnText = "Connecting"

    def draw(self):
        pyxel.cls(0)

        for row in self.tileList:
            for col in row:
               pyxel.rectb(col.getPosX(), col.getPosY(), col.getPosX(
               ) + col.getSize(), col.getPosY()+col.getSize(), 3)
        pyxel.text(55, 41, self.turnText, pyxel.frame_count % 16)

        #pyxel.blt(-5, -1, 0, 0, 0, self.test.getPosition()[0], self.test.getPosition()[1],0)
        self.x = 0
        self.y = 1

        #Tank GUI
        self.MyTankPositionTile = self.tileList[self.GM.getTankPosition()[0][
            self.x]][self.GM.getTankPosition()[0][self.y]]

        self.EnemyTankPositionTile = self.tileList[self.GM.getTankPosition()[1][
            self.x]][self.GM.getTankPosition()[1][self.y]]

        pyxel.blt(self.MyTankPositionTile.getCenterPosX()-6, self.MyTankPositionTile.getCenterPosY() -
                  6, 2, self.myTankAngle[0], self.myTankAngle[1], 25, 25, 0)
        #pyxel.blt(self.EnemyTankPositionTile.getCenterPosX(), self.EnemyTankPositionTile.getCenterPosY(),0, 0, 0, 32, 38, 0)
        if self.enemyTankAngle == self.enemyTankAngleRight:
            pyxel.blt(self.EnemyTankPositionTile.getCenterPosX(
            )-6, self.EnemyTankPositionTile.getCenterPosY()-6, 2, self.leftTank[0], self.leftTank[1], 25, 25, 0)
        elif self.enemyTankAngle == self.enemyTankAngleLeft:
            pyxel.blt(self.EnemyTankPositionTile.getCenterPosX(
            )-6, self.EnemyTankPositionTile.getCenterPosY()-6, 2, self.rightTank[0], self.rightTank[1], 25, 25, 0)
        elif self.enemyTankAngle == self.enemyTankAngleUpper:
            pyxel.blt(self.EnemyTankPositionTile.getCenterPosX(
            )-6, self.EnemyTankPositionTile.getCenterPosY()-6, 2, self.upperTank[0], self.upperTank[1], 25, 25, 0)
        #elif self.enemyTankAngle==self.enemyTankAngleLower:
        else:
            pyxel.blt(self.EnemyTankPositionTile.getCenterPosX(
            )-6, self.EnemyTankPositionTile.getCenterPosY()-6, 2, self.lowerTank[0], self.lowerTank[1], 25, 25, 0)

        #TankHP GUI
        pyxel.text(self.MyTankPositionTile.getCenterPosX(), self.MyTankPositionTile.getCenterPosY(
        ), str(self.GM.getTankHP()[0]) + "/" + str(self.GM.getTankMaxHP()[0]), 7)
        pyxel.text(self.EnemyTankPositionTile.getCenterPosX(
        ), self.EnemyTankPositionTile.getCenterPosY(), str(self.GM.getTankHP()[1]) + "/" + str(self.GM.getTankMaxHP()[1]), 7)

        #bullet GUI
        for BulletPosition, BulletPoint, BulletOrbit in zip(self.GM.getBulletPosition(), self.GM.getBulletPoint(), self.GM.getBulletOrbit()):
            self.currentTilePosition = self.tileList[BulletPosition[
                self.x]][BulletPosition[self.y]]

            self.BulletPosintPosition = self.tileList[BulletPoint[
                self.x]][BulletPoint[self.y]]

            orbitX = BulletOrbit[self.x]
            orbitY = BulletOrbit[self.y]
            self.BulletInitialPosition = self.tileList[orbitX][orbitY]

            centerX = self.BulletInitialPosition.getCenterPosX(
            ) - self.BulletPosintPosition.getCenterPosX()
            centerY = self.BulletInitialPosition.getCenterPosY(
            ) - self.BulletPosintPosition.getCenterPosY()

            if BulletOrbit[self.x]-BulletPoint[self.x] > 0:
                if BulletOrbit[self.y]-BulletPoint[self.y] > 0:
                    self.bulletAngle = self.bulletAngleLowerLeft
                elif BulletOrbit[self.y]-BulletPoint[self.y] == 0:
                    self.bulletAngle = self.bulletAngleLeft
                elif BulletOrbit[self.y]-BulletPoint[self.y] < 0:
                    self.bulletAngle = self.bulletAngleUpperLeft
            elif BulletOrbit[self.x]-BulletPoint[self.x] < 0:
                if BulletOrbit[self.y]-BulletPoint[self.y] > 0:
                    self.bulletAngle = self.bulletAngleLowerRight
                elif BulletOrbit[self.y]-BulletPoint[self.y] == 0:
                    self.bulletAngle = self.bulletAngleRight
                elif BulletOrbit[self.y]-BulletPoint[self.y] < 0:
                    self.bulletAngle = self.bulletAngleUpperRight
            else:
                if BulletOrbit[self.y]-BulletPoint[self.y] > 0:
                    self.bulletAngle = self.bulletAngleLower
                elif BulletOrbit[self.y]-BulletPoint[self.y] < 0:
                    self.bulletAngle = self.bulletAngleUpper

            if abs(centerX) >= abs(centerY):
                # print("getCenterPosX:" + str(self.currentTilePosition.getCenterPosX()) +
                #       "getCenterPosY:" + str(self.currentTilePosition.getCenterPosY()) +
                #       "orbit" + str(orbitY/abs(orbitX))
                #       )
                print("bulletPosition:" + str(self.currentTilePosition.getCenterPosX()
                                              ) + ":" + str(self.currentTilePosition.getCenterPosY()))
                ans = self.BulletInitialPosition.getCenterPosY() + ((self.BulletPosintPosition.getCenterPosY() - self.BulletInitialPosition.getCenterPosY())/abs(self.BulletPosintPosition.getCenterPosX() -
                                                                                                                                                                 self.BulletInitialPosition.getCenterPosX()) * abs(self.currentTilePosition.getCenterPosX() - self.BulletInitialPosition.getCenterPosX()))
                #pyxel.blt(self.currentTilePosition.getCenterPosX(),int(ans), 1, 0, 0, 32, 38, 0)
                pyxel.blt(self.currentTilePosition.getCenterPosX(), int(
                    ans), 2, self.bulletAngle[0], self.bulletAngle[1], 25, 25, 0)
                # import pdb
                # pdb.set_trace()

            elif abs(centerX) < abs(centerY):
                # import pdb
                # pdb.set_trace()
                print("bulletPosition:" + str(self.currentTilePosition.getCenterPosX()
                                              ) + ":" + str(self.currentTilePosition.getCenterPosY()))
                ans = self.BulletInitialPosition.getCenterPosX() + ((self.BulletPosintPosition.getCenterPosX() - self.BulletInitialPosition.getCenterPosX())/abs(self.BulletPosintPosition.getCenterPosY() -
                                                                                                                                                                 self.BulletInitialPosition.getCenterPosY()) * abs(self.currentTilePosition.getCenterPosY() - self.BulletInitialPosition.getCenterPosY()))
                pyxel.blt(int(ans),
                          self.currentTilePosition.getCenterPosY(), 2, self.bulletAngle[0], self.bulletAngle[1], 25, 25, 0)

            #print("bullet2:" + str(self.GM.getBulletPosition()[1]))

        if self.bulletSuggest == True:
            self.realX = self.targetX*25
            self.realY = self.targetY*25
            pyxel.rect(self.realX, self.realY, self.realX+25, self.realY+25, 4)

            #text
        if self.gameText != "":
             pyxel.text(128, 128, self.gameText, 7)

        

        #explosion GUI
        for bullets in self.bullets:
            self.bulletsPlace = bullets.getPoint()
            pyxel.blt(
                25*self.bulletsPlace[0]-25, 25*self.bulletsPlace[1]-25, 2, 0, 150, 75, 75, 0)
        
        
        pyxel.blt(50, 80, 0, self.drawText[0], self.drawText[1], 255, 50, 0)

        if self.confirmDraw:
            if self.turnText == "EnemyTurn":

                # if pyxel.btnp(pyxel.KEY_LEFT):
                #     pass
                # elif pyxel.btnp(pyxel.KEY_RIGHT):
                #     pass
                # elif pyxel.btnp(pyxel.KEY_UP):
                #     pass
                # elif pyxel.btnp(pyxel.KEY_DOWN):
                #     pass
                self.confirmDraw = False
                self.isLoad = True
