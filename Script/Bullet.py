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
        x = 0
        y = 1
        xd = self.point[x]-self.orbit[x]
        yd = self.point[y]-self.orbit[y]


        if xd == 0 or yd == 0:
            if (int(self.point[x]-self.position[x]) == 0) and (int(self.point[y]-self.position[y]) == 0):
                print("Destroy")
                self.Destroy()
                return
            if xd > 0:
                self.position[x] += int(xd/abs(xd))
            else:
                self.position[y] += int(yd/abs(yd))
        else:
            if (int(self.point[x]-self.position[x]) == 0) or (int(self.point[y]-self.position[y]) == 0):
                print("Destroy")
                self.Destroy()
                return

            if abs(xd) > abs(yd):
                self.position[x] += int(xd/abs(xd))
                # if abs(self.point[x]-self.position[x])  <= abs(yd):
                #     self.position[y] += int(yd/abs(yd))
            elif abs(xd) < abs(yd):
                self.position[y] += int(yd/abs(yd))
                # if abs(xd) >=  abs(self.point[y]-self.position[y]) :
                #     self.position[x] += int(xd/abs(xd))
            else:
                self.position[x] += int(xd/abs(xd))
                self.position[y] += int(yd/abs(yd))

    def getOrbit(self):
        return self.orbit

    def setOrbit(self,orbit):
        self.orbit = orbit

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

    def setPoint(self, point):
        if type(point) == type(list()):
           self.point = point
        else:
           print("Argument please in the list")

    def Destroy(self):
        del self
    
