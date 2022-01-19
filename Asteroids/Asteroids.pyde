
#import libraries
add_library('minim')
import random


game_status = 1 #1 for start screen, 2 for playing, 3 for game over

head = 0 #angle of the ship

#start position of ship x and y
px = 600 
py = 400
laser_shot = False

#gives short imunity after hit
immune_count = 100
#location of ship
location = PVector(px, py)
#velocity of ship
velocity = PVector(0, 0)
#life count 
life_count = 5
#list of laser objects
laser_list = []
#counter for points
point_count = 0


    
    
def setup():
    global startfont, ship, hit, title, shot, location, explo
    size(1200, 800)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)
    frame = frameRate(60)
    #establishes audio
    minim = Minim(this)
    hit = minim.loadSample("hitHurt.wav")
    title = minim.loadFile("astSong.mp3")
    shot = minim.loadSample("laserShoot.wav")
    explo = minim.loadSample("explosion.wav")
    


def draw():
    global startfont, ship, py, px, ship, immune_count, game_status, location, velocity, force, laser_shot, laser_list, shot, astt, point_count, explo, asts
    background(0)
    
    if game_status == 1:
        #displays the start screen if the game status is = to 1
        startscreen()
    if game_status == 2:
        #displays the asteroid objects stored in astt, makes them move, makes them collide with ship and edges of screen
        for i in range(len(astt)):
            astt[i].move()
            astt[i].display()
            astt[i].collide()
        
        #creates the Player object as a ship and displays it and calls its movement function and its collisions with the edges of the screen
        ship = Player(px, py)
        ship.display()
        ship.update()
        ship.col()
        #continuously adds to the immunity counter
        immune_count += 1
        #displays number of lives
        fill(255)
        textSize(30)
        text("Lives:", 50, 50)
        life = Life()
        life.show()
        #displays number of points
        text(point_count, 600, 50)
        
        #calls the laser object and checks collisions with the asteroids
        if laser_shot == True:
            for i in reversed(range(len(laser_list))):
                laser_list[i].laser_show()
                laser_list[i].laser_update()
                for j in reversed(range(len(astt))):
                    #checks for collision 
                    if laser_list[i].laser_collide(astt[j]):
                        #checks if the size of the asteroid is greater than 10 
                        if (astt[j].r > 10):
                            #if the asteroid size is greater than 10 breaks it into two different smaller asteroids
                            newAsteroids = astt[j].ast_break()
                            astt = astt + newAsteroids 
                            laser_list.pop(i)
                            astt.pop(j)
                            #adds 10 points to the point counter
                            point_count += 10
                            explo.trigger()
                            break
                        else:
                            #if the size is smaller than 10 it removes the object from the list making it disapear 
                            astt.pop(j)
                            explo.trigger()
                            #adds 20 points because the smaller ones are harder to hit
                            point_count += 20
                            #creates a new big asteroid when small asteroids are destroyed
                            asts = 1
                            for x in range(asts):
                                 astt.append(Asteroid(PVector(random.uniform(0, 1200), random.uniform(0, 800)), 40))
        #if the life counter is = 0 changes the game status and displays the endscreen   
        if life_count == 0:
            game_status = 3
    if game_status == 3:
        endscreen()
    

    
class Life(object):
    #class to display the number of lives as triangles 
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
    #asteroid class
    def __init__(self, pos, r):
        global location
        #if there is pos summons new small asteroid in the positions old asteroid was destroyed
        if (pos):
            self.pos = pos.copy()
        #else summons asteroids somewhere random
        else:
            self.pos = PVector(random.uniform(0,1200), random.uniform(0, 800))
        
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.r = r
        #if there is an r it makes the new asteroids spawned spawn smaller
        if (r):
            self.r = self.r * 0.5
        #else spawns asteroid with normal size
        else:
            self.r = random.uniform(15, 50)
        self.id = id
        self.sides = random.randint(5, 15)
        self.off = []
        for i in range(self.sides):
            self.off.append(random.uniform(-self.r* 0.5, self.r*0.5))
            
    def move(self):
        #if the position of the asteroid reaches the edges of the screen collisions
        self.pos.x += self.vx
        self.pos.y += self.vy
        if self.pos.x > 1250:
            self.pos.x = -50
        elif self.pos.x < -50:
            self.pos.x = 1250
        if self.pos.y > 850:
            self.pos.y = -50
        elif self.pos.y < -50:
            self.pos.y = 850
    def display(self):
        #creates random shapes with random number of sides as asteroids using trig
        pushMatrix()
        stroke(255)
        strokeWeight(2)
        noFill()
        translate(self.pos.x, self.pos.y)
        beginShape() #starts creating shape
        for i in range(self.sides): #the shape will have a random number of sides
            angle = map(i, 0, self.sides, 0, TWO_PI) 
            x = (self.r + self.off[i]) * cos(angle)
            y = (self.r + self.off[i]) * sin(angle)
            vertex(x, y)
        endShape(CLOSE)
        popMatrix()
        
    def collide(self):
        global hit, asts, astt, life_count, immune_count, location
        #checks if the player hits the asteroid and makes the player los a life
        dx = dist(self.pos.x, self.pos.y, location.x, location.y)
        if (dx < self.r):
            if immune_count > 100:
                life_count -= 1
                immune_count = 0
                hit.trigger()

    def ast_break(self):
        #creates two new asteroids that are smaller when big asteroid is destroyed
        newAst = []
        newAst.append(Asteroid(self.pos, self.r))
        newAst.append(Asteroid(self.pos, self.r))
        return newAst


#creates a list of asteroid objects    
asts = 20
astt = []
for i in range(asts):
    astt.append(Asteroid(PVector(random.uniform(0, 1200), random.uniform(0, 800)), random.uniform(15, 70)))

class laser(object):
    def __init__(self, loc, angle):
        global head, location, head, velocity, force, astt
        self.l = PVector(loc.x, loc.y)
        self.go = PVector.fromAngle(angle)
        self.go.mult(5)
    def laser_show(self):
        #displays the laser
        pushMatrix()
        stroke(255)
        strokeWeight(4)
        point(self.l.x, self.l.y)
        popMatrix()
    def laser_update(self):
        #makes the laser move
        self.l.add(self.go)
    def laser_collide(self, asteroid):
        #checks if the laser has collided with an asteroid
        global laser_list
        d = dist(self.l.x, self.l.y, asteroid.pos.x, asteroid.pos.y)
        if (d < asteroid.r):
            return True
        else:
            return False
            



        

def startscreen():
    global startfont, ship, title, location
    #function to display the start screen
    background(0)
    fill(255)
    textFont(startfont)
    textSize(100)
    text("ASTEROIDS", 340, 200)
    textSize(60)
    text("PLAY GAME", 450, 600)
    stroke(255)
    strokeWeight(3)
    noFill()
    rect(435, 550, 360, 60, 7)
    textSize(40)
    text("W to move forward", 350, 300)
    text("A and D to turn", 350, 370)
    text("SPACE BAR to shoot laser", 350, 440)
    title.play()
    
    
def endscreen():
    global startfont, point_count
    #function to display the end screen
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
    global game_status, life_count, point_count, title, location, velocity, head, astt
    if game_status == 1:
        #if 'play game' is pressed switches the games status to 2
        if (mouseX > 435 and mouseX < 795) and (mouseY > 550 and mouseY < 610):
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
        #empties the list and then refills it with asteroids
        asts = 20
        del astt[:]
        for i in range(asts):
            astt.append(Asteroid(PVector(random.uniform(0, 1200), random.uniform(0, 800)), 40))
            
            
def keyPressed():
    global head, ship, laser_shot, shot, location, laser_list, astt
    if key == 'w' or key == 'W':
        #makes ship go forward in direction faced
        ship.boost()
    if key == 'd' or key == 'D':
        #turns ship
        head += 0.1
    if key == 'a' or key == 'A':
        #turns ship
        head -= 0.1
    if key == ' ':
        #shoots the laser
        laser_shot = True
        shot.trigger()
        laser_list.append(laser(location, head))
    



 
class Player(object):
    def __init__(self, px, py):
        global location, velocity
        self.location = location
        self.velocity = velocity
    
    def display(self):
        #displays the ship
        noFill()
        strokeWeight(5)
        stroke(255)
        pushMatrix()
        translate(self.location.x, self.location.y)
        rotate(head + PI/2)
        triangle(-10, 15, 0, -15, 10, 15)    
        popMatrix()

    def update(self):
        #updates the ships position
        self.location.add(self.velocity)
        self.velocity.mult(0.98)
    
    def boost(self):
        global force
        #make the ship move from the angle it is facing
        force = PVector.fromAngle(head)
        self.velocity.add(force)
    
    def col(self):
        #checks if the ship has reached the border 
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = 1200
        
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = 800




        



        

        
        
        
    
