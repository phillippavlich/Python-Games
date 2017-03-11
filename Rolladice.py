#dice

from graphics import*

class Button:

    def __init__(self, win, center, width, height, label):
        w,h=width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin= x+w, x-w
        self.ymax, self.ymin= y+h, y-h
        p1= Point(self.xmin, self.ymin)
        p2= Point(self.xmax, self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill("light green")
        self.rect.draw(win)
        self.label=Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self,p):
        return self.active and self.xmin<=p.getX()<=self.xmax \
              and self.ymin<=p.getY()<=self.ymax

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active=True

    def deactivate(self):
        self.label.setFill("red")
        self.rect.setWidth(1)
        self.active=False

class DieView:
    def __init__(self, win, center, size):
        self.win=win
        self.background="white"
        self.foreground="black"
        self.psize=0.1*size
        hsize=size/2.0
        offset=0.6*hsize
        cx,cy=center.getX(), center.getY()
        p1=Point(cx-hsize, cy-hsize)
        p2=Point(cx+hsize, cy+hsize)
        rect=Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

        self.pips=[self.__makePip(cx-offset,cy-offset), self.__makePip(cx-offset,cy),
        self.__makePip(cx-offset,cy+offset), self.__makePip(cx,cy),
        self.__makePip(cx+offset,cy-offset), self.__makePip(cx+offset,cy),
        self.__makePip(cx+offset,cy+offset)]

        self.onTable=[[], [3], [2,4], [2,3,4], [0,2,4,6], [0,2,3,4,6], [0,1,2,4,5,6]]

        self.setValue(0)

    def __makePip(self,x,y):
        pip=Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        for pip in self.pips:
            pip.setFill(self.background)
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

from random import randrange
from graphics import GraphWin, Point

def main():
    win=GraphWin("Dice Roller")
    win.setCoords(0,0,10,10)
    win.setBackground("blue")

    die1=DieView(win, Point(3,7),2)
    die2=DieView(win, Point(7,7),2)
    rollButton=Button(win,Point(5,4.5),6,1,"Roll Dice")
    rollButton.activate()
    quitButton= Button(win, Point(5,1), 2, 1, "Quit")
    pt=win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1=randrange(1,7)
            die1.setValue(value1)
            value2=randrange(1,7)
            die2.setValue(value2)
            quitButton.activate()
        pt=win.getMouse()
    win.close()

main()
