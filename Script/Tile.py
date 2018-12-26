import pyxel
class Tile:
    
    def __init__(self,size,posX,posY):
        self.__obj = None
        self.size = size
        self.posX = posX
        self.posY = posY
        self.posCX = posX + int(size/4)
        self.posCY = posY + int(size/4)
        #pyxel.run(self.update, self.draw)

    def getSize(self):
        return self.size

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY
    
    def getCenterPosX(self):
        return self.posCX
    
    def getCenterPosY(self):
        return self.posCY

    def setObject(self,obj):
        self.obj = obj

    def state(self):
        return self.__obj is not None

    def drawLine(self, size, posX,posY, col):
        pyxel.rectb(posX, posY, posX+size, posY+size, col)


    
