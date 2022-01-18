add_library('minim')
import random

game_status = 1 #1 for start screen, 2 for playing, 3 for game over
laservx = 0
laservy = 0
head = 0
lhead = 0
px = 600
py = 400
laser_shot = False
immune_count = 100
location = PVector(px, py)
shoot = PVector(0, 0)
shiploc = []
velocity = PVector(0, 0)
life_count = 5
laser_num = 1
laser_list = []
    
def setup():
    global startfont, ship, hit, title, shot, location
    size(1200, 800)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)
    frame = frameRate(60)
    minim = Minim(this)
    hit = minim.loadSample("hitHurt.wav")
    title = minim.loadFile("astSong.mp3")
    shot = minim.loadSample("laserShoot.wav")
    shot.shiftGain(shot.getGain(), 1, -200)





def draw():
    global startfont, ship, speed_count, py, px, ship, lser, immune_count, ax, ay, game_status, location, velocity, force, laserloc, laser_shot, laser_num, laser_list, shot, locposx, locposy, shiploc, asteroid
    background(0)
    if game_status == 1:
        startscreen()
    if game_status == 2:
        for i in range(asts):
            astt[i].move()
            astt[i].display()
            astt[i].collide()

        ship = Player(px, py)
        ship.display()
        ship.update()
        ship.col()
        immune_count += 1
        fill(255)
        textSize(30)
        text("Lives:", 50, 50)
        life = Life()
        life.show()
        laserloc = PVector(location.x, location.y) 


        if laser_shot == True:
            for i in range(len(laser_list)):
                laser_list[i].laser_show()
                laser_list[i].laser_update()
                laser_list[i].laser_collide()
            if len(shiploc) == 2:
                shiploc.pop(0)

            
        if life_count == -1:
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

    

class Asteroid(object):
    def __init__(self, x1, y1, vx1, vy1, id):
        global location
        self.x = x1
        self.y = y1
        self.vx = vx1
        self.vy = vy1
        self.r = random.uniform(5, 40)
        self.id = id
        self.sides = random.randint(5, 15)
        self.off = []
        for i in range(self.sides):
            self.off.append(random.uniform(-5, 15))
            
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > 1200 or self.x < 0:
            self.vx *= -1
        if self.y > 800 or self.y < 0:
            self.vy *= -1
    def display(self):
        pushMatrix()
        stroke(255)
        strokeWeight(2)
        noFill()
        translate(self.x, self.y)
        beginShape()
        for i in range(self.sides):
            angle = map(i, 0, self.sides, 0, TWO_PI)
            x = (self.r + self.off[i]) * cos(angle)
            y = (self.r + self.off[i]) * sin(angle)
            vertex(x, y)
        endShape(CLOSE)
        popMatrix()
        
    def collide(self):
        global px, py, asts, astt, life_count, immune_count, location
        for i in range(self.id, asts):
            dx = self.x - location.x 
            dy = self.y - location.y 
            dist_squared = dx * dx + dy * dy
            if dist_squared < 400:
                if immune_count > 100:
                    life_count -=1
                    hit.trigger()
                    immune_count = 0


asts = 10
astt = []
for i in range(asts):
    astt.append(Asteroid(random.uniform(0,1200), random.uniform(0, 800),random.uniform(0.1, 1), random.uniform(0.1, 1), i))

class laser(Asteroid):
    def __init__(self, loc, angle):
        global head, location, shoot, laserloc, head, velocity, force, shiploc, astt
        self.l = PVector(loc.x, loc.y)
        self.go = PVector.fromAngle(angle)
        self.go.mult(5)
    def laser_show(self):
        pushMatrix()
        stroke(255)
        strokeWeight(4)
        point(self.l.x, self.l.y)
        popMatrix()
    def laser_update(self):
        self.l.add(self.go)
    def laser_collide(self):
        global laser_list, laser_num
        d = dist(self.l.x, self.l.y, astt[i].x, astt[i].y)
        if (d < astt[i].r):
            print('owo')
            return True
        else:
            return False
            



        

def startscreen():
    global startfont, ship, title, location
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
    global head, py, px, ship, laser_shot, laser_num, shot, location, shiploc, laser_list, astt
    if key == 'w':
        ship.boost()
    if key == 'd':
        head += 0.1
    if key == 'a':
        head -= 0.1
    if key == 'p':
        laser_num += 1
        laser_shot = True
        shot.trigger()
        laser_list.append(laser(location, head))


            

  
    



 
class Player(object):
    def __init__(self, px, py):
        global location, velocity
        self.location = location
        self.velocity = velocity
    
    def display(self):
        global locposx, locposy
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
        self.velocity.mult(0.98)
    
    def boost(self):
        global force
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




        



        

        
        
        
    
