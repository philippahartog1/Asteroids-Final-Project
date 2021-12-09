add_library('minim')
import random

game_status = 1 #1 for start screen, 2 for playing, 3 for game over

def setup():
    global startfont
    size(1200, 800)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)


def draw():
    global startfont
    background(0)
    startscreen()
    if game_status == 2:
        for i in range(asts):
            astt[i].move()
            astt[i].display()

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
    def display(self):
        fill(255)
        ellipse(self.x, self.y, 50, 50)

asts = 10
astt = []
for i in range(asts):
    astt.append(asteroidMove(3, 4, 5, 5))

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
        

    
