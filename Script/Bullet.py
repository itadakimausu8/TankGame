from Script.GameObject import GameObject
from abc import ABCMeta, abstractmethod


class Bullet(GameObject,metaclass=ABCMeta):

    
    def __init__(self,damage,speed,explosion,orbit,point):
         self.objType = "bullet"
         self.damage = int(damage)
         self.speed = int(speed)
         self.explosion = explosion
         self.orbit = orbit
         self.position = [0, 0]
         self.point = point

    def getType(self):
        return self.objType

    def move(self):
        pass

    def getDamage(self):
        return self.damage
    
    def setDamage(self,damage):
        self.damage = damage
    
    def getPosition(self):
        return self.position

    def setPosition(self, pos):
        if type(pos) == type(list()):
           self.position = pos
        else:
           print("Argument please in the list")

    def getPoint(self):
        return self.point
    
