add_library('minim')
import random

game_status = 1 #1 for start screen, 2 for playing, 3 for game over
laservx = 0
laservy = 0
head = 0
lhead = 0
px = 600
py = 400

immune_count = 100
xspeed = 0
yspeed = 0
speed_count = 0
life_count = 5

    
def setup():
    global startfont, ship, hit, title
    size(1200, 800)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)
    frame = frameRate(60)
    minim = Minim(this)
    hit = minim.loadSample("hitHurt.wav")
    title = minim.loadFile("astSong.mp3")




def draw():
    global startfont, ship, yspeed, speed_count, py, px, ship, xspeed, laservx, laservy, lser, immune_count, ax, ay, game_status
    background(0)
    if game_status == 1:
        startscreen()
    if game_status == 2:
        for i in range(asts):
            astt[i].move()
            astt[i].display()
            astt[i].collide()
        
        al = alien()
        al.alShow()
        al.alMove()
        ship = Player(px, py)
        ship.display()
        lser = laser()
        py += yspeed
        px += xspeed
        immune_count += 1
        speed_count += 1
        ship_move()
        fill(255)
        textSize(30)
        text("Lives:", 50, 50)
        life = Life()
        life.show()
        #title.pause()
        if life_count == 0:
            game_status = 3
            
    if game_status == 3:
        background(0)

            

class Life(object):
    def __init__(self):
        global life_count
        self.x = 175
        self.y = 45
    def show(self):
        for i in range(life_count):
            stroke(255)
            noFill()
            triangle(self.x, self.y, self.x +5, self.y -10, self.x + 10, self.y)
            self.x += 20

    

class asteroidMove(object):
    def __init__(self, x1, y1, vx1, vy1, id):
        self.x = x1
        self.y = y1
        self.vx = vx1
        self.vy = vy1
            
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > 1200 or self.x < 0:
            self.vx *= -1
        if self.y > 800 or self.y < 0:
            self.vy *= -1
            


class smallAst(asteroidMove):
    def __init__(self, x1, y1, vx1, vy1, id):
        global px, py, asts, astt, hit
        asteroidMove.__init__(self, x1, y1, vx1, vy1, id)
        self.id = id
        
    
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
        
    def collide(self):
        global px, py, asts, astt, life_count, immune_count
        for i in range(self.id, asts):
            dx = self.x - px
            dy = self.y - py
            dist_squared = dx * dx + dy * dy
            if dist_squared < 400:
                if immune_count > 100:
                    life_count -=1
                    hit.trigger()
                    immune_count = 0


asts = 10
astt = []
for i in range(asts):
    astt.append(smallAst(random.uniform(0,1200), random.uniform(0, 800),random.uniform(0.1, 1), random.uniform(0.1, 1), i))

class laser(object):
    def __init__(self):
        global px, py, head, lhead
        self.lx = px #PVector(px, py)
        self.ly = py
        self.go = PVector(20, 20)
        #self.ly = py
    def laser_show(self):
        pushMatrix()
        translate(0.01, 5)
        rotate(radians(lhead))
        stroke(255, 0, 0)
        fill(255, 0, 0)
        rect(self.lx, self.ly, 0.02, 10)
        popMatrix()
    def laser_move(self):
        # newV = self.l.add(self.go)
        # return newV
        pass

class alien(object):
    def __init__(self):
        self.ax = 30 #random.randrange(-100, 1300)
        self.ay = 30 #random.randrange(-100, 900)
        self.vx = 2
        self.vy = 2
    def alShow(self):
        stroke(255)
        fill(255)
        ellipse(self.ax+35, self.ay+25, 40, 10)
        noFill()
        curve(self.ax + 20, self.ay + 100, self.ax + 20, self.ay + 20, self.ax + 50, self.ay + 20, self.ax + 60, self.ay + 100)
    def alMove(self):
        self.ax += self.vx
        self.ay += self.vy
        

def startscreen():
    global startfont, ship, title
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
    title.play()
    
        
def ship_move():
    global speed_count, px, py, yspeed, xspeed
    if speed_count > 20 and xspeed < 0:
        xspeed += 0.5
        speed_count = 0
    elif speed_count > 20 and yspeed < 0:
        yspeed += 0.5
        speed_count = 0
    elif speed_count > 20 and xspeed > 0:
        xspeed -= 0.5
        speed_count = 0
    elif speed_count > 20 and yspeed > 0:
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
    global head, yspeed, ship, xspeed, speed_count, py, px, laservy, lser, lhead
    if key == 'w' or keyCode == UP:
        if yspeed > -5:
            yspeed -= 0.5
        if head < 0 or head > 0:
            head += 3
            lhead += 3
        #xspeed -= 1
    elif key == 'a' or keyCode == LEFT:
        if xspeed > -3:
            xspeed -= 0.5
        if head > -90:
            head -= 3
            lhead -= 3
    elif key == 'd' or keyCode == RIGHT:
        if xspeed < 3:
            xspeed += 0.5
        if head < 90:
            head += 3
            lhead += 3
    elif key == 's' or keyCode == DOWN:
        if yspeed < 5:
            yspeed += 0.5
    if key == 'p':
        lser.laser_show()
        lser.laser_move()
            

    
    
    
    
    
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



        

        
        
        
    
