import random
game_status = 3
def setup():
    global startfont
    size(1200, 600)
    startfont = createFont("OCR A Extended", 16)
    print(startfont)
def draw():
    endscreen()
    points()
    mousePressed()
    startscreen()
    stars()
def endscreen():
    if game_status == 3:
        global startfont
        background(0)
        textFont(startfont)
        textSize(175)
        text("GAME OVER", 100, 200)
        for i in range(1,6):
            if not(frameCount % i == 0):
                textSize(20)
                strokeWeight(5)
                text("Click anywhere to play again", 420, 300)
            
def points():
    textFont(startfont)
    textSize(50)
    strokeWeight(9)
    text("Your score is:", 200, 450)
def startscreen():
    if game_status == 2:
        background(0)
def mousePressed():
    game_status == 2
def stars():
    for i in range(30):
        fill(255,255,255)
        x = random.randint(0, 1200)
        y = random.randint(0, 600)
        ellipse(x, y, 2, 2)
