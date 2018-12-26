from GameObject import GameObject
from abc import ABCMeta, abstractmethod


class Bullet(GameObject,metaclass=ABCMeta):

    objType = "bullet"
    
    def __init__(self,damage,speed,explosion,orbit):
         self.damage = int(damage)
         self.speed = int(speed)
         self.explosion = explosion
         self.orbit = orbit

    @classmethod
    def getType(cls):
        return cls.objType

    def move(self):
        pass

    def getDamage(self):
        return self.damage
    
    def setDamage(self,damage):
        self.damage = damage
    
    
    