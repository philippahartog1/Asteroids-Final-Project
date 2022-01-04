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
    global startfont, ship, speed_count, py, px, ship,  laservx, laservy, lser, immune_count, ax, ay, game_status, location, velocity, force
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
        ship.update()
        ship.col()
        lser = laser(px, py)
        immune_count += 1
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
        global px, py, asts, astt, hit, location
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
            dx = self.x - location.x
            dy = self.y - location.y
            dist_squared = dx * dx + dy * dy
            if dist_squared < 500:
                if immune_count > 100:
                    life_count -=1
                    hit.trigger()
                    immune_count = 0


asts = 10
astt = []
for i in range(asts):
    astt.append(smallAst(random.uniform(0,1200), random.uniform(0, 800),random.uniform(0.1, 1), random.uniform(0.1, 1), i))

class laser(object):
    def __init__(self, px_, py_):
        global head, location, shoot
        self.lx = location.x
        self.ly = location.y
        self.go = shoot
    def laser_show(self):
        stroke(255, 0, 0)
        fill(255, 0, 0)
        pushMatrix()
        translate(self.lx, self.ly)
        rotate(radians(head))
        ellipse(0, 0, 5, 5)
        popMatrix()
    def laser_move(self):
        pass

shoot = PVector(2, 0)
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
    
        

        
def mousePressed():
    global game_status
    if game_status == 1:
        if (mouseX > 400 and mouseX < 757) and (mouseY > 550 and mouseY < 605):
            game_status = 2
            
            
def keyPressed():
    global head, py, px, ship
    if key == 'w':
        ship.boost()
    if key == 'd':
        head += 0.1
    if key == 'a':
        head -= 0.1
    if key == 'p':
        lser.laser_show()
        lser.laser_move()
            

    
    

location = PVector(px, py)

velocity = PVector(0, 0)
force = PVector.fromAngle(head)

class Player(object):
    def __init__(self, px, py):
        global location, velocity
        #self.x = px
        #self.y = py
        self.location = location
        self.velocity = velocity
    
    def display(self):
        noFill()
        strokeWeight(5)
        stroke(255)
        pushMatrix()
        translate(self.location.x, self.location.y)
        rotate(head + PI/2)
        triangle(-10, 15, 0, -15, 10, 15)    
        popMatrix()
    def update(self):
        self.location.add(self.velocity)
        self.velocity.mult(0.97)
    
    def boost(self):
        force = PVector.fromAngle(head)
        self.velocity.add(force)
    
    def col(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = 1200
        
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = 800




        



        

        
        
        
    
