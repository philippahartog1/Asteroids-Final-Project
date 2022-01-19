add_library('minim')
import random
from Player import Player

game_status = 1 #1 for start screen, 2 for playing, 3 for game over

head = 0

px = 600
py = 400
laser_shot = False
immune_count = 100
location = PVector(px, py)
shoot = PVector(0, 0)

velocity = PVector(0, 0)
life_count = 5
laser_num = 1
laser_list = []
point_count = 0
def setup():
    global startfont, ship, hit, title, shot, location, explo
    size(1200, 800)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)
    frame = frameRate(60)
    minim = Minim(this)
    hit = minim.loadSample("hitHurt.wav")
    title = minim.loadFile("astSong.mp3")
    shot = minim.loadSample("laserShoot.wav")
    explo = minim.loadSample("explosion.wav")
    






def draw():
    global startfont, ship, py, px, ship, lser, immune_count, game_status, location, velocity, force, laserloc, laser_shot, laser_num, laser_list, shot, locposx, locposy, asteroid, astt, point_count, explo
    background(0)
    if game_status == 1:
        startscreen()
    if game_status == 2:
        for i in range(len(astt)):
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
        text(point_count, 600, 50)

        if laser_shot == True:
            for i in reversed(range(len(laser_list))):
                laser_list[i].laser_show()
                laser_list[i].laser_update()
                for j in reversed(range(len(astt))):
                    if laser_list[i].laser_collide(astt[j]):
                        if (astt[j].r > 10):
                            newAsteroids = astt[j].ast_break()
                            astt = astt + newAsteroids 
                            astt.pop(j)
                            laser_list.pop(i)
                            point_count += 10
                            explo.trigger()
                            break
            
        if life_count == 0:
            game_status = 3
    if game_status == 3:
        endscreen()
    

    
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
    def __init__(self, pos, r):
        global location
        if (pos):
            self.pos = pos.copy()
        else:
            self.pos = PVector(random.uniform(0,1200), random.uniform(0, 800))
        self.vx = random.uniform(0.33, 1)
        self.vy = random.uniform(0.33, 1)
        self.r = 50
        if (r):
            self.r = self.r * 0.5
        else:
            self.r = random.uniform(15, 50)
        self.id = id
        self.sides = random.randint(5, 15)
        self.off = []
        for i in range(self.sides):
            self.off.append(random.uniform(-self.r* 0.5, self.r*0.5))
            
    def move(self):
        self.pos.x += self.vx
        self.pos.y += self.vy
        if self.pos.x > 1200 or self.pos.x < 0:
            self.vx *= -1
        if self.pos.y > 800 or self.pos.y < 0:
            self.vy *= -1
    def display(self):
        pushMatrix()
        stroke(255)
        strokeWeight(2)
        noFill()
        translate(self.pos.x, self.pos.y)
        beginShape()
        for i in range(self.sides):
            angle = map(i, 0, self.sides, 0, TWO_PI)
            x = (self.r + self.off[i]) * cos(angle)
            y = (self.r + self.off[i]) * sin(angle)
            vertex(x, y)
        endShape(CLOSE)
        popMatrix()
        
    def collide(self):
        global hit, asts, astt, life_count, immune_count, location
        dx = dist(self.pos.x, self.pos.y, location.x, location.y)
        if (dx < self.r):
            if immune_count > 100:
                life_count -= 1
                immune_count = 0
                hit.trigger()
                
        else:
            pass

    def ast_break(self):
        newAst = []
        newAst.append(Asteroid(self.pos, self.r))
        newAst.append(Asteroid(self.pos, self.r))
        return newAst
        


asts = 10
astt = []
for i in range(asts):
    astt.append(Asteroid(PVector(random.uniform(0, 1200), random.uniform(0, 800)), 40))

class laser(Asteroid):
    def __init__(self, loc, angle):
        global head, location, shoot, laserloc, head, velocity, force, astt
        #super(laser, self).__init__()
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
    def laser_collide(self, asteroid):
        global laser_list, laser_num
        d = dist(self.l.x, self.l.y, asteroid.pos.x, asteroid.pos.y)
        if (d < asteroid.r):
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
    
    
def endscreen():
    global startfont, point_count
    background(0)
    textFont(startfont)
    textSize(175)
    text("GAME OVER", 100, 200)
    textSize(50)
    text('Score:', 420, 300)
    text(point_count, 620, 300)
    for i in range(1,6):
        if not(frameCount % i == 0):
            textSize(20)
            strokeWeight(5)
            text("Click anywhere to play again", 420, 400)

    
def mousePressed():
    global game_status, life_count, point_count, title, location, velocity, head
    if game_status == 1:
        if (mouseX > 400 and mouseX < 757) and (mouseY > 550 and mouseY < 605):
            game_status = 2
    if game_status == 3:
        game_status = 1
        life_count = 5
        point_count = 0
        location.x = 600
        location.y = 400
        velocity.x = 0
        velocity.y = 0
        head = 0
        title.loop()
            
            
def keyPressed():
    global head, ship, laser_shot, laser_num, shot, location, laser_list, astt
    if key == 'w' or key == 'W':
        ship.boost()
    if key == 'd' or key == 'D':
        head += 0.1
    if key == 'a' or key == 'A':
        head -= 0.1
    if key == ' ':
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




        



        

        
        
        
    
