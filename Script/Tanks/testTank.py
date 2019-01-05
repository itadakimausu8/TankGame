from Script.Tank import Tank
class testTank(Tank):

    def __init__(self):
        #__init__(hp,bullet,speed)
        super(testTank,self).__init__(50,50,1,1)
        self.__image_path = "assets/tank_16x16.png"
        self.postion = [0,0]
        
    def getImage(self):
        return self.__image_path


    
    