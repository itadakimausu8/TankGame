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
         
         self.arrival = False

    def getType(self):
        return self.objType

    def move(self):
        x = 0
        y = 1
        xd = self.point[x]-self.orbit[x]
        yd = self.point[y]-self.orbit[y]


        if xd == 0 or yd == 0:
            if (self.point[x] == self.position[x]) and (self.point[y] == self.position[y]):
                self.arrival = True
                #self.Destroy()
                return
            if abs(xd) > 0:
                self.position[x] += int(xd/abs(xd))
            elif abs(yd) > 0:
                self.position[y] += int(yd/abs(yd))
                

            if (self.point[x] == self.position[x]) and (self.point[y] == self.position[y]):
                self.arrival = True
                #self.Destroy()
                return
        else:
            if (self.point[x] == self.position[x]) or (self.point[y] == self.position[y]):
                self.arrival = True
                #self.Destroy()
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

            if (self.point[x] == self.position[x]) or (self.point[y] == self.position[y]):
                self.arrival = True
                #self.Destroy()
                return

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
    
    def arrivalCheck(self):
        x = 0
        y = 1
        xd = self.point[x]-self.orbit[x]
        yd = self.point[y]-self.orbit[y]


        if xd == 0 or yd == 0:
            if (self.point[x] == self.position[x]) and (self.point[y] == self.position[y]):
                #self.Destroy()
                return True
        else:
            if (self.point[x] == self.position[x]) or (self.point[y] == self.position[y]):
                #self.Destroy()
                return True
        
        
        return False


    def getArrival(self):
        return  self.arrival

    

    def Destroy(self):
        del self
    
