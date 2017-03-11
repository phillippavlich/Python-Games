#Poker game Fun
import random
from graphics import*

def Intro():
    print "This is an online poker game that will be a lot of fun. \nFollow the rules and let the odds ever be in your favour. \n"

def betting(Z,F,win,X1,X2):
    AA=input("How much would you like to bet: ")
    Z.modifymoney(AA)
    Phil=Rectangle(Point(X1,80),Point(X2,60))
    Phil.setFill("dark green")
    Phil.draw(win)
    F.append(AA)
    statement = Text(Point(X1+X2/float(2), 70), Z.getMoney())
    statement.setTextColor("black")
    statement.setSize(20)
    statement.draw(win)
    pt=win.getMouse()

def raising(Y,F,win,X1,X2):
    BA=input("How much would you like to raise to: ")
    Y.modifymoney(BA)
    Phil=Rectangle(Point(X1,80),Point(X2,60))
    Phil.setFill("dark green")
    Phil.draw(win)
    F.append(BA)
    statement = Text(Point(X1+X2/float(2), 70), Y.getMoney())
    statement.setTextColor("black")
    statement.setSize(20)
    statement.draw(win)
    pt=win.getMouse()

def calling(X,bet,F,win,X1,X2):
    X.modifymoney(bet)
    Phil=Rectangle(Point(X1,80),Point(X2,60))
    Phil.setFill("dark green")
    Phil.draw(win)
    F.append(bet)
    statement = Text(Point(X1+X2/float(2), 70), X.getMoney())
    statement.setTextColor("black")
    statement.setSize(20)
    statement.draw(win)
    pt=win.getMouse()

def checking(K):
    K.append(1)
    

def folding(J):
    J.append(1)

##NEED TO CREATE A FUNCTION FOR MATCHING A BET ASSUMING SOME OF YOUR MONEY WAS ALREADY PLACED IN THE POT AND SOMEONE RAISED IT!!!!!!!!!!
    
def playercreation(win,a):
    b=input("Enter the amount of money you want to start with: ")
    
    if a==2:
        c=raw_input("Enter your name: ")
        f=raw_input("Enter your name: ")
        A=player(c,0,b)
        B=player(f,1,b)
        
        statement = Text(Point(300, 25), A.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(700, 25), B.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(300, 70), A.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(700, 70), B.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)
        

    elif a==3:
        c=raw_input("Enter your name: ")
        f=raw_input("Enter your name: ")
        g=raw_input("Enter your name: ")
        A=player(c,0,b)
        B=player(f,1,b)
        C=player(g,2,b)

        statement = Text(Point(250, 25), A.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(500, 25), B.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(750, 25), C.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(250, 70), A.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(500, 70), B.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(750, 70), C.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)
      
    elif a==4:
        c=raw_input("Enter your name: ")
        f=raw_input("Enter your name: ")
        g=raw_input("Enter your name: ")
        k=raw_input("Enter your name: ")
        A=player(c,0,b)
        B=player(f,1,b)
        C=player(g,2,b)
        D=player(k,3,b)

        statement = Text(Point(200, 25), A.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(400, 25), B.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(600, 25), C.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(800, 25), D.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(200, 70), A.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(400, 70), B.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(600, 70), C.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(800, 70), D.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)
        
    else:
        c=raw_input("Enter your name: ")
        f=raw_input("Enter your name: ")
        g=raw_input("Enter your name: ")
        k=raw_input("Enter your name: ")
        q=raw_input("Enter your name: ")
        A=player(c,0,b)
        B=player(f,1,b)
        C=player(g,2,b)
        D=player(k,3,b)
        E=player(q,4,b)

        statement = Text(Point(200, 25), A.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(350, 25), B.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(500, 25), C.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(650, 25), D.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(800, 25), E.getPlayer())
        statement.setTextColor("black")
        statement.setSize(25)
        statement.draw(win)

        statement = Text(Point(200, 70), A.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(350, 70), B.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(500, 70), C.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(650, 70), D.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)

        statement = Text(Point(800, 70), E.getMoney())
        statement.setTextColor("black")
        statement.setSize(20)
        statement.draw(win)
    
    
class player:
    def __init__(self,c,d,e):
        self.c=c
        self.d=d
        self.E=e
    def getPlayer(self):
        return self.c
    def getPosition(self):
        return self.d
    def getMoney(self):
        return self.E
    def modifymoney(self,AA):
        self.E=self.E-AA
        return self.E
    def earnmoney(self,AAA):
        self.E=self.E+AAA
        return self.E

class Button:

    def __init__(self, win, center, width, height, label):
        w,h=width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin= x+w, x-w
        self.ymax, self.ymin= y+h, y-h
        p1= Point(self.xmin, self.ymin)
        p2= Point(self.xmax, self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill("orange")
        self.rect.draw(win)
        self.label=Text(center, label)
        self.label.draw(win)
        self.deactivate()
        

    def clicked(self,p):
        return self.activate and self.xmin<=p.getX()<=self.xmax \
                and self.ymin<=p.getY()<=self.ymax

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill("orange")
        self.rect.setWidth(30)
        self.active=True
        return self.active

    def deactivate(self):
        self.label.setFill("yellow")
        self.rect.setWidth(30)
        self.active=False
        return self.active

class cards:
    def __init__(self, win, center, size):
        self.win=win
        cx, cy=center.getX(), center.getY()
        self.size=size
        self.number=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        self.suit=["CLUBS", "SPADES", "DIAMONDS", "HEARTS"]

        p1=Point(cx-(0.5*self.size),cy-(0.5*self.size))
        p2=Point(cx+(0.5*self.size),cy+(0.5*self.size))
        frame=Rectangle(p1,p2)
        frame.draw(win)
        frame.setFill("white")
        
    def setValue(self,win,cx,cy,h):
        
        d=random.randint(0,12)
        e=random.randint(0,3)
        
        for i in range(len(h)):
            if h[i]==d and h[i+1]==e:
                d=random.randint(0,12)
                e=random.randint(0,3)
                for i in range(len(h)):
                    if h[i]==d and h[i+1]==e:
                        d=random.randint(0,12)
                        e=random.randint(0,3)
                        for i in range(len(h)):
                            if h[i]==d and h[i+1]==e:
                                d=random.randint(0,12)
                                e=random.randint(0,3)
                                for i in range(len(h)):
                                    if h[i]==d and h[i+1]==e:
                                        d=random.randint(0,12)
                                        e=random.randint(0,3)
                                        for i in range(len(h)):
                                            if h[i]==d and h[i+1]==e:
                                                d=random.randint(0,12)
                                                e=random.randint(0,3)
                                                for i in range(len(h)):
                                                    if h[i]==d and h[i+1]==e:
                                                        d=random.randint(0,12)
                                                        e=random.randint(0,3)
                                                        for i in range(len(h)):
                                                            if h[i]==d and h[i+1]==e:
                                                                d=random.randint(0,12)
                                                                e=random.randint(0,3)
                                                                for i in range(len(h)):
                                                                    if h[i]==d and h[i+1]==e:
                                                                        d=random.randint(0,12)
                                                                        e=random.randint(0,3)
                                                                        for i in range(len(h)):
                                                                            if h[i]==d and h[i+1]==e:
                                                                                d=random.randint(0,12)
                                                                                e=random.randint(0,3)
                                                                                for i in range(len(h)):
                                                                                    if h[i]==d and h[i+1]==e:
                                                                                        d=random.randint(0,12)
                                                                                        e=random.randint(0,3)
               
        statement = Text(Point(cx, cy), self.number[d])
        statement.setTextColor("blue")
        statement.setSize(20)
        statement.draw(win)
        statement2 = Text(Point(cx, cy+30), self.suit[e])
        statement2.setTextColor("blue")
        statement2.setSize(10)
        statement2.draw(win)
        h.insert(-1,d)
        h.insert(-1,e)

        

def main():
    win=GraphWin("Welcome to virtual poker",1000,750)
    win.setBackground("dark green")
    Intro()
    a=input("Enter the number of players you want (2-5): ")
    playercreation(win,a)
    
    card1=cards(win, Point(270,300),100)
    card2=cards(win, Point(385,300),100)
    card3=cards(win, Point(500,300),100)
    card4=cards(win, Point(615,300),100)
    card5=cards(win, Point(730,300),100)
    
    
    match=Button(win,Point(300,210),30,30,"match")
    match.activate()
    check=Button(win,Point(380,210),30,30,"Check")
    check.activate()
    bet=Button(win,Point(460,210),30,30,"Bet")
    bet.activate()
    call=Button(win,Point(540,210),30,30,"Call")
    call.activate()
    Raise=Button(win,Point(620,210),30,30,"Raise")
    Raise.activate()
    fold=Button(win,Point(700,210),30,30,"Fold")
    fold.activate()
    quitButton= Button(win, Point(950,700), 30, 30, "Quit")
    quitButton.activate()
    
    #if a==4:ASSUMING THIS IS FOR FOUR PLAYer
    pt=win.getMouse()
    
    while not quitButton.clicked(pt):
        J=[]
        Z=["A","B","C","D","A","B","C","D","A","B","C","D","A","B","C","D","A","B","C","D","A","B","C","D","A","B","C","D","A","B","C","D","A","B","C","D","A","B","C","D"]
        h=[15]
        F=[]
        i=0
#############################################################################################
        #V="F" ######TAKE THIS OUT WHEN THE PROBLEM IS FIXED
        V="lose"
        K=[]
        while V!="next" and V!="end":
            for H in range(i, len(J),4):
                if J[H]==1:
                    i+=1
##might need a try and except statement here!!!!!!!!
                else:
                    pt=win.getMouse()
                    if check.clicked(pt):
                        checking(K)
                        J.append(0)
                    elif bet.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        elif Z[i]=="B":
                            X1=350
                            X2=450
                        elif Z[i]=="C":
                            X1=550
                            X2=650
                        elif Z[i]=="D":
                            X1=750
                            X2=850
                        betting(Z[i],F,win,X1,X2)
                        K.append(2)
                        J.append(0)
        
                    elif fold.clicked(pt):
                        folding(J)
                    elif Raise.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        if Z[i]=="B":
                            X1=350
                            X2=450
                        if Z[i]=="C":
                            X1=550
                            X2=650
                        if Z[i]=="D":
                            X1=750
                            X2=850
                        raising(Z[i],F,win,X1,X2)
                        K.append(2)
                        J.append(0)
                    elif call.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        if Z[i]=="B":
                            X1=350
                            X2=450
                        if Z[i]=="C":
                            X1=550
                            X2=650
                        if Z[i]=="D":
                            X1=750
                            X2=850
                        calling(Z,F[-1],F,win,X1,X2)
                        K.append(1)
                        J.append(0)

                    i+=1
                    if J.count(1)==3:
                        for g in range(0, len(J)):
                            if J[g]==0:
                                UU=g
                                ZZ=Z[UU]
                                if ZZ=="A":
                                    X1=150
                                    X2=250
                                if ZZ=="B":
                                    X1=350
                                    X2=450
                                if ZZ=="C":
                                    X1=550
                                    X2=650
                                if ZZ=="D":
                                    X1=750
                                    X2=850
                        for u in range(0,len(F)):
                            ZZ.earnmoney(F[i])
                            Phil=Rectangle(Point(X1,80),Point(X2,60))
                            Phil.setFill("dark green")
                            Phil.draw(win)
                            statement = Text(Point(X1+X2/float(2), 70), ZZ.getMoney())
                            statement.setTextColor("black")
                            statement.setSize(20)
                            statement.draw(win)
                            V="end"
                    elif J.count(1)==2 and K[-1]==1:
                        V="next"
                    elif J.count(1)==1 and K[-1]==1 and K[-2]==1:
                        V="next"
                    elif K[-1]==1 and K[-2]==1 and K[-3]==1 and K[-4]==1:
                        V="next"
                    elif K[-1]==1 and K[-2]==1 and K[-3]==1 and K[-4]==2:
                        V="next"

               
        if V!="end":
            card1.setValue(win,270,290,h)
            card2.setValue(win,385,290,h)
            card3.setValue(win,500,290,h)
            
        V="lose"
        K=[]
        while V!="next" and V!="end":
            for H in range(i, len(J),4):
                if J[H]==1:
                    i+=1
                else:
                    pt=win.getMouse()
                    if check.clicked(pt):
                        checking(K)
                        J.append(0)
                    elif bet.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        elif Z[i]=="B":
                            X1=350
                            X2=450
                        elif Z[i]=="C":
                            X1=550
                            X2=650
                        elif Z[i]=="D":
                            X1=750
                            X2=850
                        betting(Z[i],F,win,X1,X2)
                        K.append(2)
                        J.append(0)
        
                    elif fold.clicked(pt):
                        folding(J)
                    elif Raise.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        if Z[i]=="B":
                            X1=350
                            X2=450
                        if Z[i]=="C":
                            X1=550
                            X2=650
                        if Z[i]=="D":
                            X1=750
                            X2=850
                        raising(Z[i],F,win,X1,X2)
                        K.append(2)
                        J.append(0)
                    elif call.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        if Z[i]=="B":
                            X1=350
                            X2=450
                        if Z[i]=="C":
                            X1=550
                            X2=650
                        if Z[i]=="D":
                            X1=750
                            X2=850
                        calling(Z,F[-1],F,win,X1,X2)
                        K.append(1)
                        J.append(0)

                    i+=1
                    if K[-1]==1 and K[-2]==1 and K[-3]==1 and K[-4]==1:
                        V="next"
                    if K[-1]==1 and K[-2]==1 and K[-3]==1 and K[-4]==2:
                        V="next"
                    elif J.count(1)==1 and K[-1]==1 and K[-2]==1:
                        V="next"
                    elif J.count(1)==2 and K[-1]==1:
                        V="next"
                    elif J.count(1)==3:
                        for g in range(0, len(J)):
                            if J[g]==0:
                                UU=g
                                ZZ=Z[UU]
                                if ZZ=="A":
                                    X1=150
                                    X2=250
                                if ZZ=="B":
                                    X1=350
                                    X2=450
                                if ZZ=="C":
                                    X1=550
                                    X2=650
                                if ZZ=="D":
                                    X1=750
                                    X2=850
                        for u in range(0,len(F)):
                            ZZ.earnmoney(F[i])
                            Phil=Rectangle(Point(X1,80),Point(X2,60))
                            Phil.setFill("dark green")
                            Phil.draw(win)
                            statement = Text(Point(X1+X2/float(2), 70), ZZ.getMoney())
                            statement.setTextColor("black")
                            statement.setSize(20)
                            statement.draw(win)
                            V="end"
        
        if V!="end":
            card4.setValue(win,615,290,h)

        V="lose"
        K=[]
        while V!="next" and V!="end":
            for H in range(i, len(J),4):
                if J[H]==1:
                    i+=1
                else:
                    pt=win.getMouse()
                    if check.clicked(pt):
                        checking(K)
                        J.append(0)
                    elif bet.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        elif Z[i]=="B":
                            X1=350
                            X2=450
                        elif Z[i]=="C":
                            X1=550
                            X2=650
                        elif Z[i]=="D":
                            X1=750
                            X2=850
                        betting(Z[i],F,win,X1,X2)
                        K.append(2)
                        J.append(0)
        
                    elif fold.clicked(pt):
                        folding(J)
                    elif Raise.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        if Z[i]=="B":
                            X1=350
                            X2=450
                        if Z[i]=="C":
                            X1=550
                            X2=650
                        if Z[i]=="D":
                            X1=750
                            X2=850
                        raising(Z[i],F,win,X1,X2)
                        K.append(2)
                        J.append(0)
                    elif call.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        if Z[i]=="B":
                            X1=350
                            X2=450
                        if Z[i]=="C":
                            X1=550
                            X2=650
                        if Z[i]=="D":
                            X1=750
                            X2=850
                        calling(Z,F[-1],F,win,X1,X2)
                        K.append(1)
                        J.append(0)

                    i+=1
                    if K[-1]==1 and K[-2]==1 and K[-3]==1 and K[-4]==1:
                        V="next"
                    if K[-1]==1 and K[-2]==1 and K[-3]==1 and K[-4]==2:
                        V="next"
                    elif J.count(1)==1 and K[-1]==1 and K[-2]==1:
                        V="next"
                    elif J.count(1)==2 and K[-1]==1:
                        V="next"
                    elif J.count(1)==3:
                        for g in range(0, len(J)):
                            if J[g]==0:
                                UU=g
                                ZZ=Z[UU]
                                if ZZ=="A":
                                    X1=150
                                    X2=250
                                if ZZ=="B":
                                    X1=350
                                    X2=450
                                if ZZ=="C":
                                    X1=550
                                    X2=650
                                if ZZ=="D":
                                    X1=750
                                    X2=850
                        for u in range(0,len(F)):
                            ZZ.earnmoney(F[i])
                            Phil=Rectangle(Point(X1,80),Point(X2,60))
                            Phil.setFill("dark green")
                            Phil.draw(win)
                            statement = Text(Point(X1+X2/float(2), 70), ZZ.getMoney())
                            statement.setTextColor("black")
                            statement.setSize(20)
                            statement.draw(win)
                            V="end"
        
        
        if V!="end":
            card5.setValue(win,730,290,h)

        V="lose"
        K=[]
        while V!="next" and V!="end":
            for H in range(i, len(J),4):
                if J[H]==1:
                    i+=1
                else:
                    pt=win.getMouse()
                    if check.clicked(pt):
                        checking(K)
                        J.append(0)
                    elif bet.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        elif Z[i]=="B":
                            X1=350
                            X2=450
                        elif Z[i]=="C":
                            X1=550
                            X2=650
                        elif Z[i]=="D":
                            X1=750
                            X2=850
                        betting(Z[i],F,win,X1,X2)
                        K.append(2)
                        J.append(0)
        
                    elif fold.clicked(pt):
                        folding(J)
                    elif Raise.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        if Z[i]=="B":
                            X1=350
                            X2=450
                        if Z[i]=="C":
                            X1=550
                            X2=650
                        if Z[i]=="D":
                            X1=750
                            X2=850
                        raising(Z[i],F,win,X1,X2)
                        K.append(2)
                        J.append(0)
                    elif call.clicked(pt):
                        if Z[i]=="A":
                            X1=150
                            X2=250
                        if Z[i]=="B":
                            X1=350
                            X2=450
                        if Z[i]=="C":
                            X1=550
                            X2=650
                        if Z[i]=="D":
                            X1=750
                            X2=850
                        calling(Z,F[-1],F,win,X1,X2)
                        K.append(1)
                        J.append(0)

                    i+=1
                    if K[-1]==1 and K[-2]==1 and K[-3]==1 and K[-4]==1:
                        V="next"
                    if K[-1]==1 and K[-2]==1 and K[-3]==1 and K[-4]==2:
                        V="next"
                    elif J.count(1)==1 and K[-1]==1 and K[-2]==1:
                        V="next"
                    elif J.count(1)==2 and K[-1]==1:
                        V="next"
                    elif J.count(1)==3:
                        for g in range(0, len(J)):
                            if J[g]==0:
                                UU=g
                                ZZ=Z[UU]
                                if ZZ=="A":
                                    X1=150
                                    X2=250
                                if ZZ=="B":
                                    X1=350
                                    X2=450
                                if ZZ=="C":
                                    X1=550
                                    X2=650
                                if ZZ=="D":
                                    X1=750
                                    X2=850
                        for u in range(0,len(F)):
                            ZZ.earnmoney(F[i])
                            Phil=Rectangle(Point(X1,80),Point(X2,60))
                            Phil.setFill("dark green")
                            Phil.draw(win)
                            statement = Text(Point(X1+X2/float(2), 70), ZZ.getMoney())
                            statement.setTextColor("black")
                            statement.setSize(20)
                            statement.draw(win)
                            V="end"

##FIND A way to determine who wins if not everyone folds!!!!!!!!!!!!!!
        
            
        pt=win.getMouse()
        
        card1=cards(win, Point(270,300),100)
        card2=cards(win, Point(385,300),100)
        card3=cards(win, Point(500,300),100)
        card4=cards(win, Point(615,300),100)
        card5=cards(win, Point(730,300),100)
        
    win.close()
main()
##create a point system to see who wins, most points wins money, if tied split
