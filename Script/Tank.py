from abc import ABCMeta, abstractmethod
from Script.GameObject import GameObject


class Tank(GameObject,metaclass=ABCMeta):


    def __init__(self,hp,bullet,speed):
         self.hp = int(hp)
         self.bullet = bullet
         self.speed = int(speed)
         self.objType = "Tank"
         self.position = [0,0]

    def getImage(self):
        return "No Image"

    def getType(self):
        return self.objType
    
    def getHP(self):
        return self.hp

    def getSpeed(self):
        return self.speed

    def getPosition(self):
        return self.position

    def setPosition(self, pos):
        if type(pos) == type(list()):
           self.position = pos
        else:
           print("Argument please in the list")
    
    def launchBullet(self):
        pass
    
    # move functions 
    def moveUp(self):
        if self.position[1] >0:
          self.position[1] -= self.speed

    def moveDown(self):
        if self.position[1] < 9:
          self.position[1] += self.speed

    def moveLeft(self):
        if self.position[0] > 0:
          self.position[0] -= self.speed

    def moveRight(self):
        if self.position[0] < 9:
          self.position[0] += self.speed

    def calcDamage(self,damage):
        self.hp = self.hp - int(damage)
    
    def Destroy(self):
        pass
    

    
    
