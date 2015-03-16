import pygame, random, sys, os, platform, pickle, time
from pygame.locals import *
pygame.init()
try:
    with open('chips.dat', 'rb') as f:
        Chips = pickle.load(f)
except:
    Chips = {
        "chips": 0,
        "IPhone": 0,
        "IPhoneCost": 10,
        "Computer": 0,
        "ComputerCost": 4000,
        "ChipsPerSecond": 0,
        "IPad": 0,
        "IPadCost": 150,
        "Robot": 0,
        "RobotCost": 4000
    }
    print("file not created yet")

Info = pygame.display.Info()
zoom = 1.3

WIDTH = int(Info.current_w / zoom)
HEIGHT = int(Info.current_h / zoom)

def SText(screen,text,var,X,Y,color,size=25):
    myfont = pygame.font.SysFont("monospace", size, True)
    var = myfont.render(text, 25, color)
    screen.blit(var, (X, Y))

def load_image(file_name, transparent=False):
    try: image = pygame.image.load(file_name)
    except pygame.error as message:
        raise SystemExit(message)
        print("couldn't load " + file_name)
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

def button(screen,x,y,size_W,size_H, color=(0,0,0),text="",text_color=(255,255,255),effect=False,border_width=0):
    pygame.draw.rect(screen, color, (x, y, size_W, size_H), border_width)
    
def main():
    Loops = 0
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    backround_image=load_image("GREENchip.png", True)
    IPhone=load_image("iphoner.jpg", True)
    Computer=load_image("computer.jpg", True)
    Robot=load_image("Robot.jpg", True)
    Ipad=load_image("Ipad.jpg", True)
    t1 = int(time.time())
    Sec1 = int(time.time())
    while True:
        pygame.draw.rect(screen, (0,0,0), (0, 0, WIDTH, HEIGHT))
        
        pygame.draw.rect(screen, (100,210,150), (0, 0, WIDTH-250, HEIGHT))
        
        pygame.draw.rect(screen, (255,0,0), (0, 0, WIDTH-250, HEIGHT))
        
        
        screen.blit(pygame.transform.scale(backround_image, (800, 400)), (40,40))
        
        myfont = pygame.font.SysFont("monospace", 25, True)
        
        High_Score = myfont.render("Chips:" + str(Chips['chips']), 25, (255,255,255))
        
        screen.blit(High_Score, (WIDTH-600, 0))
        
        button(screen,WIDTH-250,100,250,75,(255,255,255))
        screen.blit(pygame.transform.scale(IPhone, (100, 75)), (WIDTH-100,100))
        
        SText(screen, "IPhone", "IPhone", WIDTH-240, 115, (10,10,10), 40)
        SText(screen, str(Chips["IPhoneCost"]) + " chips", "IPhoneCost", WIDTH-240, 150, (0,0,0))
        SText(screen, "2 chips per second", "IPhoneRegard", WIDTH-240, 100, (0,0,0), 15)
        SText(screen, str(Chips["IPhone"]), "NumOfIPhones", WIDTH-25, 130, (0,0,0), 20)
        
        button(screen,WIDTH-250,180,250,75,(255,255,255))
        screen.blit(pygame.transform.scale(Ipad, (50, 60)), (WIDTH-85,200))
        
        SText(screen, "IPad", "IPad", WIDTH-240, 195, (10,10,10), 30)
        SText(screen, str(Chips["IPadCost"]) + " chips", "ComputerCost", WIDTH-240, 230, (0,0,0))
        SText(screen, "5 chips per second", "IPadRegard", WIDTH-240, 180, (0,0,0), 15)
        SText(screen, str(Chips["IPad"]), "NumOfIpad", WIDTH-20, 210, (0,0,0), 20)
        
        SText(screen, str(Chips["ChipsPerSecond"]) + " chips per second", "ChipsPerSecond", 400, 25, (255,255,255))
        
        button(screen,WIDTH-250,260,250,75,(255,255,255))
        screen.blit(pygame.transform.scale(Computer, (70, 40)), (WIDTH-85,280))
        
        SText(screen, "Computer", "Computer", WIDTH-240, 275, (10,10,10), 30)
        SText(screen, str(Chips["ComputerCost"]) + " chips", "ComputerCost", WIDTH-240, 310, (0,0,0))
        SText(screen, "20 chips per second", "ComputerRegard", WIDTH-240, 260, (0,0,0), 15)
        SText(screen, str(Chips["Computer"]), "NumOfComputer", WIDTH-20, 290, (0,0,0), 20)
        
        screen.blit(pygame.transform.scale(Robot, (60, 60)), (WIDTH-90,360))
        
        pygame.display.flip()
        for events in pygame.event.get():
            if events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    with open('chips.dat', 'wb') as f:
                        pickle.dump(Chips, f, pickle.HIGHEST_PROTOCOL)
                    sys.exit()
            if events.type == MOUSEBUTTONDOWN:
                MouseX = pygame.mouse.get_pos()[0]
                MouseY = pygame.mouse.get_pos()[1]
                if MouseX > 80 and MouseY > 80 and MouseX < 800 and MouseY < 400:
                    Chips["chips"] += 1
                if MouseX > WIDTH-250 and MouseY > 100 and MouseX < WIDTH and MouseY < 175:
                        if Chips["chips"] > Chips["IPhoneCost"]:
                            Chips["chips"] -= Chips["IPhoneCost"]
                            Chips["IPhone"] += 1
                            Chips["IPhoneCost"] += int(Chips["IPhoneCost"] / 3)
                if MouseX > WIDTH-250 and MouseY > 180 and MouseX < WIDTH and MouseY < 255:
                        if Chips["chips"] > Chips["IPadCost"]:
                            Chips["chips"] -= Chips["IPadCost"]
                            Chips["IPad"] += 1
                            Chips["IPadCost"] += int(Chips["IPadCost"] / 3)
                if MouseX > WIDTH-250 and MouseY > 260 and MouseX < WIDTH and MouseY < 335:
                        if Chips["chips"] > Chips["ComputerCost"]:
                            Chips["chips"] -= Chips["ComputerCost"]
                            Chips["Computer"] += 1
                            Chips["ComputerCost"] += int(Chips["ComputerCost"] / 3)
                            
        t2 = int(time.time())
        Sec2 = int(time.time())
        if Sec2 - Sec1 > 0:
            Chips["ChipsPerSecond"] = Chips["IPhone"] * 2 + Chips["IPad"] * 5 + Chips["Computer"] * 20
            Chips["chips"] += 2 * Chips['IPhone']
            Chips["chips"] += 5 * Chips['IPad']
            Chips["chips"] += 20 * Chips['Computer']
            Sec1 = int(time.time())
        if t2 - t1 > 2:
            myfont = pygame.font.SysFont("monospace", 25, True)
            Save = myfont.render("Saved", 25, (255,255,255))
            screen.blit(Save, (WIDTH-600, 0))
            print("Saving...")
            with open('chips.dat', 'wb') as f:
                pickle.dump(Chips, f, pickle.HIGHEST_PROTOCOL)
            t1 = int(time.time())
        
main()
