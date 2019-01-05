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
        pyxel.init(255, 255, caption="Hello Pyxel")
        self.GM = GameManager()
        #pyxel.load("assets/tile.pyxel")
        self.tileList = [ [Tile(25,w*25,h*25) for h in range(ClientGUI.mapSize)] for w in range(ClientGUI.mapSize)]

        self.confirmDraw = False
        self.isBulletMove = False
        #create testTank
        #self.test = testTank()
        pyxel.image(0).load(0, 0, self.GM.getTankImage()[0])
        #self.test.setPosition([2,2])
        
        #create testBullet
        
        pyxel.image(1).load(0, 0, "assets/bullet_16x16.png")

        self.GM.load()
        pyxel.run(self.update, self.draw)


    def update(self):

        if self.isLoad:
            self.GM.load()
            self.GM.calcDamage()
            self.isLoad = False

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        #operate tank
        if self.confirmDraw:
               self.turnText = "EnemyTurn"
               if self.isBulletMove:
                  self.GM.bulletMove()
                  #add test
                  self.GM.calcDamage()
                  self.isBulletMove = False
        else:
            if self.GM.getTurn() == 0:
                    self.turnText = "MyTurn"
                    #print("myTurn")
                    #print("btn possible")
                    if pyxel.btnp(pyxel.KEY_LEFT):
                        self.GM.pressLeft()
                        self.isBulletMove = True
                        self.confirmDraw = True
                        #self.GM.load()
                    elif pyxel.btnp(pyxel.KEY_RIGHT):
                        self.GM.pressRight()
                        self.isBulletMove = True
                        self.confirmDraw = True
                        #self.GM.load()
                    elif pyxel.btnp(pyxel.KEY_UP):
                        self.GM.pressUp()
                        self.isBulletMove = True
                        self.confirmDraw = True
                        #self.GM.load()
                    elif pyxel.btnp(pyxel.KEY_DOWN):
                        self.GM.pressDown()
                        self.isBulletMove = True
                        self.confirmDraw = True
                        #self.GM.load()
                    elif pyxel.btnp(pyxel.KEY_SPACE):
                        self.GM.pressSpace()
                        self.isBulletMove = True
                        self.confirmDraw = True
                    #    self.GM.load()
            elif self.GM.getTurn() == 1:
                self.GM.load()
            else:
                self.turnText = "Connecting"
            


    def draw(self):
        pyxel.cls(0)

        pyxel.text(55, 41, self.turnText, pyxel.frame_count % 16)
        for row in self.tileList:
            for col in row:
               pyxel.rectb(col.getPosX(), col.getPosY(), col.getPosX() + col.getSize(), col.getPosY()+col.getSize(), 3)

        #pyxel.blt(-5, -1, 0, 0, 0, self.test.getPosition()[0], self.test.getPosition()[1],0)
        self.x = 0
        self.y = 1
        
    
        #Tank GUI
        self.MyTankPositionTile = self.tileList[self.GM.getTankPosition()[0][
            self.x]][self.GM.getTankPosition()[0][self.y]]

        self.EnemyTankPositionTile = self.tileList[self.GM.getTankPosition()[1][
            self.x]][self.GM.getTankPosition()[1][self.y]]

        pyxel.blt(self.MyTankPositionTile.getCenterPosX(), self.MyTankPositionTile.getCenterPosY(),
                  0, 0, 0, 32, 38, 0)
        pyxel.blt(self.EnemyTankPositionTile.getCenterPosX(), self.EnemyTankPositionTile.getCenterPosY(),
                  0, 0, 0, 32, 38, 0)
        
        #TankHP GUI
        pyxel.text(self.MyTankPositionTile.getCenterPosX(), self.MyTankPositionTile.getCenterPosY(
        ), str(self.GM.getTankHP()[0]) + "/" + str(self.GM.getTankMaxHP()[0]), 7)
        pyxel.text(self.EnemyTankPositionTile.getCenterPosX(
        ), self.EnemyTankPositionTile.getCenterPosY(), str(self.GM.getTankHP()[1]) + "/" + str(self.GM.getTankMaxHP()[1]), 7)


        #bullet GUI
        for BulletPosition, BulletPoint, BulletOrbit in zip(self.GM.getBulletPosition(), self.GM.getBulletPoint(),self.GM.getBulletOrbit()):
            self.currentTilePosition = self.tileList[BulletPosition[
                self.x]][BulletPosition[self.y]]

            self.BulletPosintPosition = self.tileList[BulletPoint[
                self.x]][BulletPoint[self.y]]
            
            orbitX = BulletOrbit[self.x]
            orbitY = BulletOrbit[self.y]
            self.BulletInitialPosition = self.tileList[orbitX][orbitY]


            centerX = self.BulletInitialPosition.getCenterPosX() - self.BulletPosintPosition.getCenterPosX()
            centerY = self.BulletInitialPosition.getCenterPosY() - self.BulletPosintPosition.getCenterPosY()




            if abs(centerX) >= abs(centerY):
                # print("getCenterPosX:" + str(self.currentTilePosition.getCenterPosX()) +
                #       "getCenterPosY:" + str(self.currentTilePosition.getCenterPosY()) +
                #       "orbit" + str(orbitY/abs(orbitX))
                #       )
                print("bulletPosition:" + str(self.currentTilePosition.getCenterPosX()) + ":" + str(self.currentTilePosition.getCenterPosY()))
                ans = self.BulletInitialPosition.getCenterPosY() + ((self.BulletPosintPosition.getCenterPosY() - self.BulletInitialPosition.getCenterPosY())/abs(self.BulletPosintPosition.getCenterPosX()-self.BulletInitialPosition.getCenterPosX()) * abs(self.currentTilePosition.getCenterPosX() - self.BulletInitialPosition.getCenterPosX()))
                pyxel.blt(self.currentTilePosition.getCenterPosX(), int(ans), 1, 0, 0, 32, 38, 0)
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
                          self.currentTilePosition.getCenterPosY(), 1, 0, 0, 32, 38, 0)

            #print("bullet2:" + str(self.GM.getBulletPosition()[1]))
    

        if self.confirmDraw:
            if self.turnText == "EnemyTurn":
                # import pdb
                # pdb.set_trace()
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

