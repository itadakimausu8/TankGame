import pyxel
from Script.Tile import Tile
from Script.Tanks.testTank import testTank
from Script.Bullets.testBullet import testBullet
from Script.GameManager import GameManager
class ClientGUI:

    mapSize = 10
    def __init__(self):
        pyxel.init(255, 255, caption="Hello Pyxel")
        self.GM = GameManager()
        #pyxel.load("assets/tile.pyxel")
        self.tileList = [ [Tile(25,w*25,h*25) for h in range(ClientGUI.mapSize)] for w in range(ClientGUI.mapSize)]

        
        #create testTank
        #self.test = testTank()
        pyxel.image(0).load(0, 0, self.GM.getTankImage()[0])
        #self.test.setPosition([2,2])
        
        #create testBullet
        pyxel.image(1).load(0, 0, self.GM.getBulletImage()[0])

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        #operate tank

        # if pyxel.btnp(pyxel.KEY_LEFT):
        #   self.test.moveLeft()
        # elif pyxel.btnp(pyxel.KEY_RIGHT):
        #   self.test.moveRight()
        # elif pyxel.btnp(pyxel.KEY_UP):
        #   self.test.moveUp()
        # elif pyxel.btnp(pyxel.KEY_DOWN):
        #   self.test.moveDown()
        # elif pyxel.btnp(pyxel.KEY_SPACE):
        #    self.test.launchBullet()
        

    def draw(self):
        pyxel.cls(0)

        for row in self.tileList:
            for col in row:
               pyxel.rectb(col.getPosX(), col.getPosY(), col.getPosX() + col.getSize(), col.getPosY()+col.getSize(), 3)

        #pyxel.blt(-5, -1, 0, 0, 0, self.test.getPosition()[0], self.test.getPosition()[1],0)
        self.x = 0
        self.y = 1
        self.posTile = self.tileList[self.GM.getTankPosition()[0][
            self.x]][self.GM.getTankPosition()[0][self.y]]

        self.posTile2 = self.tileList[self.GM.getBulletPosition()[0][
            self.x]][self.GM.getBulletPosition()[0][self.y]]
        pyxel.blt(self.posTile.getCenterPosX(), self.posTile.getCenterPosY(),
                  0, 0, 0, 32, 38, 0)
        pyxel.blt(self.posTile2.getCenterPosX(), self.posTile2.getCenterPosY(),
                  1, 0, 0, 32, 38, 0)
        # self.test_text(6, 124)


    # def test_text(self, x, y):
    #     pyxel.text(x, y, "text(x,y,s,col)", 7)

    #     x += 4
    #     y += 8
    #     s = "Elapsed frame count is {}\n" "Current mouse position is ({},{})".format(
    #         pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y
    #     )

    #     pyxel.text(x + 1, y, s, 1)
    #     pyxel.text(x, y, s, 9)

