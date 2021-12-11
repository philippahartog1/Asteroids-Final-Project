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
life_count = 5
poly = PVector()
random_poly = []
for i in range(5):
    random_poly.append(poly)
    
def setup():
    global startfont, ship
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
            astt[i].update()
        ship = Player()
        ship.display()
    
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
    def update(self):
        global ship
        # self.pos.add(self.vel)
        # print(self.vel)
        ship = Player()
        areaOrig = abs( (ship.x2 - ship.x1)*(ship.y3 - ship.y1) - (ship.x3 - ship.x1) *(ship.y2 - ship.y1) )
        area1 = abs( (ship.x1 - self.x)*(ship.y2 - self.y) - (ship.x2-self.x)*(ship.y1-self.y) )
        area2 = abs( (ship.x2 - self.x)*(ship.y3 - self.y) - (ship.x3 - self.x)*(ship.y2-self.y) )
        area3 = abs( (ship.x3 - self.x)*(ship.y1-self.y) - (ship.x1 - self.x)+(ship.y3 - self.y) )
        if (area1 + area2 + area3) == areaOrig:
            life_count -= 1

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


asts = 10
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

def mousePressed():
    global game_status
    if game_status == 1:
        if (mouseX > 400 and mouseX < 757) and (mouseY > 550 and mouseY < 605):
            game_status = 2
#vel = PVector(0, 0)
#force = PVector.fromAngle(head1)
def keyPressed():
    global playery, playervy, playerx, playervx, r, ship, head1
    if keyCode == 'UP' or key == 'w':
        #ship.boost()
        pass
        

    elif keyCode == 'LEFT' or key == 'a':
        head1 -= 0.1
    elif keyCode == 'RIGHT' or key == 'd':
        head1 += 0.1




# class Player(object):
#     def __init__(self, vx, vy):
#         global head1
#         self.vx = vx
#         self.vy = vy
#         self.playerx = 0
#         self.playery = 0
#         self.head = head1
    
#     def display(self):
#         translate(600, 400)
#         rotate(self.head)
#         line(self.playerx, self.playery, self.playerx + 10, self.playery +25)
#         line(self.playerx, self.playery, self.playerx - 10, self.playery +25)
#         line(self.playerx -10, self.playery +25, self.playerx, self.playery +20)
#         line(self.playerx +10, self.playery+25, self.playerx , self.playery+20)
    
        
class Player(object):
    def __init__(self):
        global head1, vel, astt
        self.pos = PVector(width/2, height/2)
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.x3 = 0
        self.y3 = 0
        self.head = head1
        self.vel = PVector(0, 0)
    def display(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.head + PI/2)
        triangle(-self.x1 +10, self.y1 -10, self.x2 - 10, self.y2 -10, self.x3, -self.y3 +10)
        #triangle(-self.r, self.r, self.r, self.r, 0, -self.r)
        popMatrix()
    # def update(self):
    #     # self.pos.add(self.vel)
    #     # print(self.vel)


    def boost(self):
        force = PVector.fromAngle(self.head)
        self.vel.set(0+1, 0+1)
        print(force)
        print(self.vel)
        

        
        

        
        
        
    
