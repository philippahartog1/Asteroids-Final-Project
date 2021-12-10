add_library('minim')
import random

game_status = 1 #1 for start screen, 2 for playing, 3 for game over
playerx = 0
laserx = 600
playery = 0
lasery = 400
playervy = 0
playervx = 0
laservx = 2
laservy = 2
r = 0
def setup():
    global startfont
    size(1200, 800)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)
    frame = frameRate(60)



def draw():
    global startfont, playery, playervy, playerx, playervx
    background(0)
    startscreen()
    if game_status == 2:
        for i in range(asts):
            astt[i].move()
            astt[i].display()
    player()
    playery -= playervy
    playerx -= playervx
    if playerx < -2000:
        playerx = 2000
    elif playerx > 2000:
        playerx = -2000
    if playery < -500:
        playery = 500
    elif playery > 500:
        playery = -500




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
    global playery, playervy, playerx, playervx, r
    if keyCode == 'UP' or key == 'w':
        playervy = 3
    elif keyCode == 'LEFT' or key == 'a':
        r -= 2
    elif keyCode == 'DOWN' or key == 's':
        playervy = -3
    elif keyCode == 'RIGHT' or key == 'd':
        r += 2
    
def player():
    if game_status == 2:
        stroke(255)
        pushMatrix()
        translate(width/2, height/2)
        rotate(radians(r))
        #tri(200)
        #triangle(playerx, playery, playerx+10, playery+25, playerx-10, playery+25)
        line(playerx, playery, playerx + 10, playery +25)
        line(playerx, playery, playerx - 10, playery +25)
        line(playerx -10, playery +25, playerx, playery +20)
        line(playerx +10, playery+25, playerx , playery+20)
        popMatrix()
# def tri(length):
#     triangle(playerx, -playery, -playerx*sqrt(3)/2, playery/2, playerx*sqrt(3)/2, playery/2)        
        
        
            
