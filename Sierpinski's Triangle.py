import random
import pygame
from pygame import gfxdraw

pygame.init()

screen = pygame.display.set_mode((1000, 800))
#setting up the co-ordinates of the vertices
pointX = 425
pointY = 50
point1X = 100
point1Y = 500
point2X = 700
point2Y = 500

#function to generate fractals
def mid(x1,y1,x2,y2):
    x=(x1+x2)/2
    y=(y1+y2)/2
    return x,y

#function for vertices and the pointing the tracer
def point(x,y):
    s = pygame.Surface((8, 8))
    s.fill((255, 0, 0))
    r, r.x, r.y = s.get_rect(), x, y
    screen.blit(s, r)

#function for drawing the points
def drawpoint(x,y):
    s=pygame.Surface((4,4))
    s.fill((10,150,0))
    r,r.x,r.y=s.get_rect(),x,y
    screen.blit(s,r)

#the control loop
running = True
while(running):
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x=(pointX+point1X)/2
    y=(pointY+point1Y)/2
    #setting the number of iterations as 10000
    for i in range(1,10000):
        a=random.randint(1,3)
        if(a==1):
            x,y=mid(x,y,pointX,pointY)
        elif(a==2):
            x,y=mid(x,y,point1X,point1Y)
        elif(a==3):
            x,y=mid(x,y,point2X,point2Y)
        drawpoint(x,y)
    #plotting vertices as red
    point(x,y)
    point(pointX,pointY)
    point(point1X,point1Y)
    point(point2X,point2Y)
    pygame.display.update()
