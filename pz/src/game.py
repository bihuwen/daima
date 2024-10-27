import pygame
import image
from const import *
import sunflolwer
import data_object
import peashooter
import zombiebase
import time
import random

class Game(object):
    def __init__(self,ds):
        self.ds=ds
        self.back=image.Image(PATH_BACK, 0, (0,0), GEME_SIZE, 0)
        self.plants=[]
        self.summons=[]
        self.hasPlant=[]
        self.zoms=[]
        self.gold=100
        self.ZomTime=0
        self.goldFont=pygame.font.Font(None,60)
        for i in range(GRID_SIZE[0]):
            col = []
            for j in range(GRID_SIZE[1]):
                col.append(0)
            self.hasPlant.append(col)

    def renderFont(self):
        textImage=self.goldFont.render("Gold:"+str(self.gold),True,(0,0,0))
        self.ds.blit(textImage,(13,23))
        textImage=self.goldFont.render("Gold:"+str(self.gold),True,(255,255,255))
        self.ds.blit(textImage,(10,23))

    def draw(self):
        self.back.draw(self.ds)
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)
        for zom in self.zoms:
            zom.draw(self.ds)
        self.renderFont()
    
    def update(self):
        self.back.update()
        for plant in self.plants:
            plant.update()
            if plant.hasSummon():
                summ=plant.doSummon()
                self.summons.append(summ)
        for summon in self.summons:
            summon.update()
        for zom in self.zoms:
            zom.update()

        if time.time()-self.ZomTime>3:
            self.ZomTime=time.time()
            self.addZom(14,random.randint(0,4))
            

    def checkLoot(self,mousePos):
        for summon in self.summons:
            if not summon.canLoot():
                continue
            rect =summon.getRect()
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                self.gold+=summon.getPrice()
                return True
        return False

    def mouseClickHandler(self, btn):
        mousePos = pygame.mouse.get_pos()
        if self.checkLoot(mousePos):
            return
        if btn == 1:
            self.checkAddPlant(mousePos, 3)
        elif btn == 3:
            self.checkAddPlant(mousePos, 4)


    def getIndexByPos(self, pos):
        x = (pos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (pos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y

    def addSunFlower(self, x, y):
        '''if self.hasPlant[x][y] == 1 :    吃钱bug
            return
        self.hasPlant[x][y]=1'''
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = sunflolwer.SunFlower(3, pos)
        self.plants.append(sf)

    def addPerShooter(self, x, y):
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = peashooter.PeaShooter(PERSHOOTER, pos)
        self.plants.append(sf)

    def addZom(self,x,y):
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        zm=zombiebase.ZombieBase(1,pos)
        self.zoms.append(zm)

    def checkAddPlant(self, mousePos, objId):
        x, y = self.getIndexByPos(mousePos)
        if x<0 or x>=GRID_COUNT[0]:
            return
        if y<0 or y>=GRID_COUNT[1]:
            return
        if self.gold<data_object.data[objId]['PRICE']:
            return
        if self.hasPlant[x][y] == 1 :
            return
        self.hasPlant[x][y]=1
        self.gold-=data_object.data[objId]['PRICE']
        if objId==3:
            self.addSunFlower(x,y)
        elif  objId==4:
            self.addPerShooter(x,y)

    