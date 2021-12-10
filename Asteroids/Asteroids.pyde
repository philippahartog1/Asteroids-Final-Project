add_library('minim')
import random

game_status = 1 #1 for start screen, 2 for playing, 3 for game over
laserx = 600
lasery = 400
# playervy = 0
# playervx = 0
laservx = 2
laservy = 2
head1 = 0

def setup():
    global startfont
    size(1200, 800)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)
    frame = frameRate(60)



def draw():
    global startfont, playery, playervy, playerx, playervx, ship
    background(0)
    startscreen()
    if game_status == 2:
        for i in range(asts):
            astt[i].move()
            astt[i].display()
        ship = Player()
        ship.display()
        #ship.turn(90)
    

class asteroidMove(object):
    def __init__(self, x1, y1, vx1, vy1):
        self.x = x1
        self.y = y1
        self.vx = vx1
        self.vy = vy1
            
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > 1500 or self.x < -300:
            self.vx *= -1
        if self.y > 1300 or self.y < -300:
            self.vy *= -1
class smallAst(asteroidMove):
    def __init__(self, x1, y1, vx1, vy1):
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

asts = 10
astt = []
for i in range(asts):
    astt.append(smallAst(random.uniform(0,1200), random.uniform(0, 800),random.uniform(1, 5), random.uniform(1, 5)))

def startscreen():
    global startfont
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

def mousePressed():
    global game_status
    if game_status == 1:
        if (mouseX > 400 and mouseX < 757) and (mouseY > 550 and mouseY < 605):
            game_status = 2

def keyPressed():
    global playery, playervy, playerx, playervx, r, ship, head1
    if keyCode == 'UP' or key == 'w':
        print("ss")
    elif keyCode == 'LEFT' or key == 'a':
        head1 -= 0.1
    elif keyCode == 'RIGHT' or key == 'd':
        head1 += 0.1

class Player(object):
    def __init__(self):
        global head1
        self.pos = PVector(width/2, height/2)
        self.r = 10
        self.head = head1
    def display(self):
        translate(self.pos.x, self.pos.y)
        rotate(self.head)
        triangle(-self.r, self.r, self.r, self.r, 0, -self.r)

        
        
        
    
