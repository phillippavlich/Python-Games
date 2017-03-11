from graphics import *

def main():
    win = GraphWin("House", 500, 500)

    statement = Text(Point(250, 30), "This Is My House")
    statement.setTextColor("blue")
    statement.setSize(20)
    statement.draw(win)
    
    p1 = win.getMouse()
    p2 = win.getMouse()

    frame = Rectangle(p1, p2)
    frame.setOutline("black")
    frame.setFill("purple")
    frame.draw(win)
    
    p3 = win.getMouse()
    x0 = abs(p2.getX() - p1.getX())
    x = abs(p3.getX() - p1.getX())
    x1 = x - (0.10*x0)
    xdoor1 = p1.getX() + x1
    xdoor2 = xdoor1 + 0.2*x0

    door = Rectangle(Point(xdoor1, p1.getY()), Point(xdoor2, p3.getY()))
    door.setOutline("black")
    door.setFill("green")
    door.draw(win)

    p4 = win.getMouse()

    x4 = p4.getX() + 0.075*x0
    x5 = p4.getY() + 0.075*x0
    x6 = p4.getX() - 0.075*x0
    x7 = p4.getY() - 0.075*x0


    window = Rectangle(Point(x4,x5), Point(x6,x7))
    window.setOutline("black")
    window.setFill("white")
    window.draw(win)


    p5 = win.getMouse()
    x2 = 0.5 * x0
    x3 = x2 + p1.getX()

    roof = Polygon(p2, Point(p1.getX(), p2.getY()), Point(x3, p5.getY()))
    roof.setOutline("brown")
    roof.setFill("magenta")
    roof.draw(win)

    win.setBackground("black")

    path = Rectangle(Point(xdoor1, p1.getY()), Point(xdoor2, 500))
    path.setFill("gray")
    path.draw(win)

    center = Point(400, 100)
    moon = Circle(center, 75)
    moon.setOutline("yellow")
    moon.setFill("white")
    moon.draw(win)


    for i in range(15):
        p6 = win.getMouse()
        stars = Point(p6.getX(), p6.getY())
        stars.setFill("yellow")
        stars.draw(win)
        
    for i in range(15):
        p6 = win.getMouse()
        stars = Point(p6.getX(), p6.getY())
        stars.setFill("white")
        stars.draw(win)    

    win.getMouse()
    doormessage = p3.getY() - 10


    message = Text(Point(xdoor2, doormessage), "Come on in...")
    message.setTextColor("pink")
    message.setSize(20)
    message.draw(win)

    dooropen = Rectangle(Point(xdoor1, p1.getY()), Point(xdoor2, p3.getY()))
    dooropen.setOutline("black")
    dooropen.setFill("white")
    dooropen.draw(win)

    pathlight = Rectangle(Point(xdoor1, p1.getY()), Point(xdoor2, 500))
    pathlight.setFill("yellow")
    pathlight.draw(win)

    win.getMouse()

    message.undraw()
    
    framechange = Rectangle(p1, p2)
    framechange.setOutline("black")
    framechange.setFill("red")
    framechange.draw(win)

    roofchange = Polygon(p2, Point(p1.getX(), p2.getY()), Point(x3, p5.getY()))
    roofchange.setOutline("brown")
    roofchange.setFill("dark orange")
    roofchange.draw(win)

    windowchange = Rectangle(Point(x4,x5), Point(x6,x7))
    windowchange.setOutline("black")
    windowchange.setFill("yellow")
    windowchange.draw(win)

    doorchange = Rectangle(Point(xdoor1, p1.getY()), Point(xdoor2, p3.getY()))
    doorchange.setOutline("black")
    doorchange.setFill("yellow")
    doorchange.draw(win)

    pathchange = Rectangle(Point(xdoor1, p1.getY()), Point(xdoor2, 500))
    pathchange.setFill("gray")
    pathchange.draw(win)

    

    happy = Text(Point(350, 450), "Happy Halloween!")
    happy.setTextColor("orange")
    happy.setSize(20)
    happy.draw(win)

    win.getMouse()
    
    center2 = Point(200, 200)
    blank = Circle(center, 800)
    blank.setOutline("blue")
    blank.setFill("yellow")
    blank.draw(win)

    win.getMouse()

    happy2 = Text(Point(250, 250), "Sorry, this is the end \n of our presentation :(")
    happy2.setTextColor("dark green")
    happy2.setSize(20)
    happy2.draw(win)
    
    win.getMouse()
    win.close()
main()    
