from abc import ABCMeta, abstractmethod

class GameObject(object,metaclass=ABCMeta):
        
    @abstractmethod     
    def getType(self):
        pass
    

    @abstractmethod
    def getPosition(self):
        pass

    @abstractmethod
    def setPosition(self):
        pass

