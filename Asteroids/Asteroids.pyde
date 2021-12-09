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
        

    
