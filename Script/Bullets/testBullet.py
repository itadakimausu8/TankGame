from Script.Bullet import Bullet

class testBullet(Bullet):

    def __init__(self,point):
        super(testBullet, self).__init__(1, 1, 1,1,point)
        self.image_path = "assets/bullet_16x16.png"
        self.postion = [0, 0]

    def getImage(self):
        return self.image_path

    
    
