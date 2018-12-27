import re
class TCPData:

    def __init__(self):
      self.myTankType = None
      self.myTankPos = None
      self.myTankHP = None
      self.myBulletType = None
      self.myBulletPos = None
      self.myBulletPoint = None
      self.enemyTankType = None
      self.enemyTankPos = None
      self.enemyTankHP = None
      self.enemyBulletType = None
      self.enemyBulletPos = None
      self.enemyBulletPoint = None


    def pushData(self):
        return "|"+str(self.myTankType) + "|"+str(self.myTankPos) + "|"+str(self.myTankHP) + "|"+str(self.myBulletType) + "|"+str(self.myBulletPos) + "|"+str(self.myBulletPoint) + "|"+str(self.enemyTankType) + "|"+str(self.enemyTankPos) + "|"+str(self.enemyTankHP) + "|"+str(self.enemyBulletType) + "|"+str(self.enemyBulletPos) + "|"+str(self.enemyBulletPoint)
    
    def setData(self, myTankType, myTankPos, myTankHP, myBulletType, myBulletPos, myBulletPoint,
                enemyTankType, enemyTankPos, enemyTankHP, enemyBulletType, enemyBulletPos, enemyBulletPoint):
      self.myTankType = myTankType
      self.myTankPos = myTankPos
      self.myTankHP = myTankHP
      self.myBulletType = myBulletType
      self.myBulletPos = myBulletPos
      self.myBulletPoint = myBulletPoint
      self.enemyTankType = enemyTankType
      self.enemyTankPos = enemyTankPos
      self.enemyTankHP = enemyTankHP
      self.enemyBulletType = enemyBulletType
      self.enemyBulletPos = enemyBulletPos
      self.enemyBulletPoint = enemyBulletPoint
    
    def setStringData(self, stringData):
        data_list = stringData.split("|")
        print("data_list:" + str(data_list))
        self.myTankType = int(data_list[1])
        self.myTankPos = int(data_list[2])
        self.myTankHP = int(data_list[3])
        self.myBulletType = self.toList(data_list[4])
        self.myBulletPos = self.toList(data_list[5])
        self.myBulletPoint = self.toList(data_list[6])
        self.enemyTankType = int(data_list[7])
        self.enemyTankPos = int(data_list[8])
        self.enemyTankHP = int(data_list[9])
        self.enemyBulletType = self.toList(data_list[10])
        self.enemyBulletPos = self.toList(data_list[11])
        self.enemyBulletPoint = self.toList(data_list[12])
        print("reData:" + self.pushData())

    def toList(self, content):
        pattern = '\d+'
        repatter = re.compile(pattern)
        results = repatter.findall(content)

        result_list = list()
        for result in results:
          result_list.append(int(result))

        return result_list

    def getMyTankType(self):
        return self.myTankType

    def getMyTankPos(self):
        return self.myTankType

    def getMyTankHP(self):
        return self.myTankHP

    def getMyBulletType(self):
        return self.myBulletType

    def getMyBulletPos(self):
        return self.myBulletPos

    def getMyBulletPoint(self):
        return self.myBulletPoint

    def getEnemyTankType(self):
        return self.enemyTankType

    def getEnemyTankPos(self):
        return self.enemyTankPos

    def getEnemyTankHP(self):
        return self.enemyTankHP

    def getEnemyBulletType(self):
        return self.enemyBulletType

    def getEnemyBulletPos(self):
        return self.enemyBulletPos

    def getEnemyBulletPoint(self):
        return self.enemyBulletPoint

    def setMyTankType(self,myTankType):
        self.myTankType = myTankType

    def setMyTankPos(self,myTankPos):
        self.myTankPos = myTankPos

    def setMyTankHP(self,myTankHP):
        self.myTankHP = myTankHP

    def setMyBulletType(self,myBulletType):
        self.myBulletType = myBulletType

    def setMyBulletPos(self,myBulletPos):
        self.myBulletPos = myBulletPos

    def setMyBulletPoint(self,myBulletPoint):
        self.myBulletPoint = myBulletPoint

    def setEnemyTankType(self,enemyTankType):
        self.enemyTankType = enemyTankType

    def setEnemyTankPos(self,enemyTankPos):
        self.enemyTankPos = enemyTankPos

    def setEnemyTankHP(self,enemyTankHP):
        self.enemyTankHP = enemyTankHP

    def setEnemyBulletType(self,enemyBulletType):
        self.enemyBulletType = enemyBulletType

    def setEnemyBulletPos(self,enemyBulletPos):
        self.enemyBulletPos = enemyBulletPos

    def setEnemyBulletPoint(self,enemyBulletPoint):
        self.enemyBulletPoint = enemyBulletPoint


    
