import image
import time
import data_object

class ObjectBase(image.Image):
    def __init__(self,id,pos):
       self.id=id
       self.preIndexTime=0
       self.prePosionTime=0
       self.preSummonTime=0
       super(ObjectBase,self).__init__(
           self.getData()['PATH'],
           0,
           pos,
           self.getData()['SIZE'],
           self.getData()['IMAGE_INDEX_MAX']
           )
    
    def getData(self):
        return data_object.data[self.id]
    
    def getPositionCD(self):
        return self.getData()['POSITION_CD']

    def getImageIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']

    def getSummonCD(self):
        return self.getData()['SUMMON_CD']

    def getSpeed(self):
        return self.getData()['SPEED']

    def canLoot(self):
        return self.getData()['CAN_LOOT']

    def getPrice(self):
        return self.getData()['PRICE']
    def update(self):
        self.checkSummon()
        self.checkImageIndex()
        self.checkPosition()

    def checkSummon(self):
        if time.time()-self.preSummonTime<=self.getSummonCD():#延时
            return
        self.preSummonTime=time.time()
        self.preSummon()

    def checkImageIndex(self):
        if time.time()-self.preIndexTime<=self.getImageIndexCD():#延时
            return
        self.preIndexTime=time.time()

        idx=self.pathIndex+1#切换图片
        if idx>=self.pathIndexCount:
            idx=0
        self.updateIndex(idx)

    def checkPosition(self):
        if time.time()-self.prePosionTime <= self.getPositionCD():#延时
            return False
        self.prePosionTime=time.time()
        speed=self.getSpeed()
        self.pos=(self.pos[0]+speed[0],self.pos[1]+speed[1])#平移
        return True
    
    def preSummon(self):
        pass

    def hasSummon(self):
        pass
    
    def doSummon(self):
        pass