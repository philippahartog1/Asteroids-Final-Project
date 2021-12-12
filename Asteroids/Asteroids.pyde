add_library('minim')
import random

game_status = 1 #1 for start screen, 2 for playing, 3 for game over
laserx = 600
lasery = 400
# playervy = 0
# playervx = 0
laservx = 2
laservy = 2
head = 0

px = 600
py = 400
xspeed = 0
yspeed = 0
speed_count = 0
life_count = 5

    
def setup():
    global startfont, ship
    size(1200, 800)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)
    frame = frameRate(60)




def draw():
    global startfont, ship, yspeed, speed_count, py, px, ship, xspeed
    background(0)
    startscreen()
    if game_status == 2:
        for i in range(asts):
            astt[i].move()
            astt[i].display()

        ship = Player(px, py)
        ship.display()
        py += yspeed
        px += xspeed
        speed_count += 1
        ship_move()
        
        text(life_count, 200, 200)

    

class asteroidMove(object):
    def __init__(self, x1, y1, vx1, vy1):
        global ship, playerx
        self.x = x1
        self.y = y1
        self.vx = vx1
        self.vy = vy1
            
    def move(self):
        global ship
        self.x += self.vx
        self.y += self.vy
        if self.x > 1200 or self.x < 0:
            self.vx *= -1
        if self.y > 800 or self.y < 0:
            self.vy *= -1


class smallAst(asteroidMove):
    def __init__(self, x1, y1, vx1, vy1):
        global ship
        asteroidMove.__init__(self, x1, y1, vx1, vy1)
        
    
    def display(self):
        stroke(255)
        line(self.x, self.y, self.x+5, self.y+10)
        line(self.x+5, self.y+10, self.x-20, self.y+20)
        line(self.x-20, self.y+20, self.x-20, self.y+10)
        line(self.x-20, self.y+10, self.x-30, self.y+10)
        line(self.x-30, self.y+10, self.x-30, self.y-10)
        line(self.x-30, self.y-10, self.x-15, self.y-15)
        line(self.x-15, self.y-15, self.x, self.y)
        #ellipse(self.x, self.y, 50, 50)


asts = 20
astt = []
for i in range(asts):
    astt.append(smallAst(random.uniform(0,1200), random.uniform(0, 800),random.uniform(0.1, 1), random.uniform(0.1, 1)))

class laser(object):
    def __init__(self):
        pass



def startscreen():
    global startfont, ship
    if game_status == 1:
        background(0)
        fill(255)
        textFont(startfont)
        textSize(100)
        text("ASTEROIDS", 340, 200)
        textSize(60)
        text("PLAY GAME", 420, 600)
        stroke(255)
        strokeWeight(3)
        noFill()
        rect(400, 550, 360, 60, 7)
        
        
def ship_move():
    global speed_count, px, py, yspeed, xspeed
    if speed_count > 200 and xspeed < 0:
        xspeed += 0.5
        speed_count = 0
    elif speed_count > 200 and yspeed < 0:
        yspeed += 0.5
        speed_count = 0
    elif speed_count > 200 and xspeed > 0:
        xspeed -= 0.5
        speed_count = 0
    elif speed_count > 200 and yspeed > 0:
        yspeed -= 0.5
        speed_count = 0
    if px < 0:
        px = 1200
    if py < 0:
        py = 800
    if py > 800:
        py = 0
    if px > 1200:
        px = 0    
        
        
def mousePressed():
    global game_status
    if game_status == 1:
        if (mouseX > 400 and mouseX < 757) and (mouseY > 550 and mouseY < 605):
            game_status = 2
            
            
def keyPressed():
    global head, yspeed, ship, xspeed, speed_count, py, px
    if key == 'w' or keyCode == UP:
        if yspeed > -10:
            yspeed -= 0.5
        if head < 0 or head > 0:
            head += 3
        #xspeed -= 1
    elif key == 'a' or keyCode == LEFT:
        if xspeed > -5:
            xspeed -= 0.5
        if head > -90:
            head -= 3
    elif key == 'd' or keyCode == RIGHT:
        if xspeed < 5:
            xspeed += 0.5
        if head < 90:
            head += 3
    elif key == 's' or keyCode == DOWN:
        if yspeed < 10:
            yspeed += 0.5

class Player(object):
    def __init__(self, px, py):
        self.x = px
        self.y = py
    
    def display(self):
        noFill()
        strokeWeight(5)
        stroke(255)
        pushMatrix()
        translate(self.x, self.y)
        rotate(radians(head))
        triangle(-10, 15, 0, -15, 10, 15)    
        popMatrix()



        

        
        
        
    
