from threading import Thread
import threading
import pygame
import time
import random
pygame.init()
lock = threading.Lock()


# window size

win = pygame.display.set_mode((800,500))

# objects names

background = pygame.image.load("GRAY BG.png")
background = pygame.transform.scale(background,(800,500))

arrow = pygame.image.load("arrow-button.png")
arrow = pygame.transform.scale(arrow,(100, 75))

red_dot = pygame.image.load("red dot.png")
red_dot = pygame.transform.scale(red_dot,(50, 50))

start_button = pygame.image.load("Start-Button.png")
start_button = pygame.transform.scale(start_button,(75, 50))

redot_icon = pygame.image.load("redot icon.png")
redot_icon = pygame.transform.scale(redot_icon,(1000, 400))

settings_butoon = pygame.image.load("settings_button.png")
settings_butoon = pygame.transform.scale(settings_butoon,(45, 25))

rule_button = pygame.image.load("rule_button.png")
rule_button = pygame.transform.scale(rule_button,(25, 25))

redot_logo = pygame.image.load("redot logo.png")
redot_logo = pygame.transform.scale(redot_logo,(1250, 500))

back_button = pygame.image.load("back-button.png")
back_button = pygame.transform.scale(back_button,(50, 50))

file = open('data-base.txt', "r")
content = file.readlines()

# objects position

red_dot_x = random.randint(25, 800)
red_dot_y = random.randint(25, 500)


# when the game started

employees = []

def separator(list):
    for item in list:
        item += '\n'
        employees.append(item)
    file = open('data-base.txt', "a")
    file.writelines(employees)
    file.close()

def new_user():
    global user_text
    global score_text
    run4 = True
    user_text = ''
    input_rect = pygame.Rect(300,200,200,32)
    color_active = pygame.Color("white")
    color_passive = pygame.Color("gray")
    color = color_passive

    active = False

    while run4:
        text_score = ""
        pygame.time.delay(30)
        pygame.display.set_caption("Red Dot Game: ")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            
            if event.type == pygame.KEYDOWN:
                if active == True:

                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        if int(user_text_size) >= 186:
                            pass
                        else:
                            user_text += event.unicode
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:    
                    if user_text == "":
                        continue
                    else:
                        user_text = user_text[:-1]
                        file = open('data-base.txt', "r")
                        content = file.readlines()
                        for line in content:
                            name,score = line.strip().split("||")
                            if name == user_text:
                                score_text = score
                                run4 = False
                                main_menu()
                            pygame.display.update
                        score_text = "0"
                        separator([(user_text+'||'+score_text)])
                        
                        run4 = False
                        main_menu()
                        pygame.display.update
            
            mouse_buttons = pygame.mouse.get_pressed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if mx <= 450 and mx >= 350:
                        if my >= 300 and my <= 375:
                            if user_text == "":
                                continue
                            else:
                                file = open('data-base.txt', "r")
                                content = file.readlines()
                                for line in content:
                                    name,score = line.strip().split("||")
                                    if name == user_text:
                                        score_text = score
                                    else:
                                        score_text = "0"
                                separator([(user_text+'||'+score_text)])
                                run4 = False
                                main_menu()
                                pygame.display.update
        win.fill((150,200,255))

        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(win, color, input_rect, 0)
        font = pygame.font.SysFont("ariel", 32)
        font2 = pygame.font.SysFont("ariel", 65)

        text = font2.render("Enter Your Name:", True, (220, 0, 0))
        text_surface = font.render(user_text, True, (0,0,0))

        user_text_size = text_surface.get_width()

        win.blit(text_surface,(400 - user_text_size / 2, input_rect.y + 5))
        win.blit(text,(225, 100))
        win.blit(arrow,(350, 300))





        pygame.display.update()


def main_menu():
    run5 = True    
    while run5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            font = pygame.font.SysFont("ariel", 30)
            text = font.render("Hello: "+ str(user_text), True, (0, 0, 0))
            win.blit(background,(0,0))
            win.blit(rule_button,(700, 20))
            win.blit(settings_butoon,(730, 20))
            win.blit(redot_logo,(-225,60))
            win.blit(text,(20,20))
            win.blit(start_button,(360,450))


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if mx <= 435 and mx >= 360:
                        if my >= 460 and my <= 495 :
                            run5 = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if mx <= 725 and mx >= 702:
                        if my >= 23 and my <= 47:
                            run5 = False
                            rule()


        pygame.display.update()






def rule():
    run2 = True
    while run2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            font = pygame.font.SysFont("ariel", 40)
            font2 = pygame.font.SysFont("ariel", 100)


            text = font2.render("Rules:", True, (0, 0, 0))
            text2 = font.render("You got some seconds", True, (0, 0, 0))
            text3 = font.render("to click amount of clicks", True, (0, 0, 0))
            text4 = font.render("requested.", True, (0, 0, 0))
            text5 = font.render("Good luck", True, (0, 0, 0))



            win.blit(background,(0,0))
            win.blit(redot_icon,(15,150))
            win.blit(back_button,(700,25))
            win.blit(text,(50,50))
            win.blit(text2,(55,125))
            win.blit(text3,(55,160))
            win.blit(text4,(55,195))
            win.blit(text5,(55,230))


            mouse_buttons = pygame.mouse.get_pressed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if my <= 78 and my >= 28:
                        if mx >= 700 and mx <= 750:
                            run2 = False
                            main_menu()

            pygame.display.update()

def red_dot_position():
    global red_dot_x
    global red_dot_y
    global t_wait
    run3 = True
    t_wait = 1.5
    while run3:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        win.blit(background,(0,0))
        win.blit(red_dot,(red_dot_x,red_dot_y))               
        red_dot_x = random.randint(25, 800)
        red_dot_y = random.randint(25, 500)
        win.blit(background,(0,0))
        win.blit(red_dot,(red_dot_x,red_dot_y))
        last_score = score
        t_wait -= 0.01
        time.sleep(t_wait)
        click_check(last_score,score)
        pygame.display.update()




def the_game():
    global score
    run3 = True
    score = 0
    win.blit(background,(0,0))
    win.blit(red_dot,(red_dot_x,red_dot_y)) 
    while run3:
        pygame.time.delay(30)
        pygame.display.set_caption("Score: "+str(score))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            mouse_buttons = pygame.mouse.get_pressed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if my <= red_dot_y + 50 and my >= red_dot_y:
                        if mx >= red_dot_x and mx <= red_dot_x + 50:
                            score += 1
        
            pygame.display.update()

def click_check(last_score,score):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if score > last_score:
            run = False
            continue
        else:
            run = False
            run3 = False
            game_over()        


def game_over():
    run6 = True
    while run6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        font2 = pygame.font.SysFont("ariel", 100)
        text = font2.render("Game Over!", True, (0, 0, 0))
        text2 = font2.render(("Your Score Was "+str(score)), True, (0, 0, 0))
        text_w = text.get_width()
        text2_w = text2.get_width()
        win.blit(text,(400 - text_w / 2,100))
        win.blit(text2,(400 - text2_w / 2, 200))

new_user()

t1 = Thread(target=red_dot_position)
t2 = Thread(target=the_game)

t1.start()
t2.start()

t1.join()
t2.join()