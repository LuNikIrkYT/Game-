import pygame
import time
import random
W = 823
H = 825
FPS = 5



x_hero = 7
y_hero = 7

x_box = 2
y_box = 7

x_home = 2
y_home = 1

name = input("Как тебя зовут? ")
hod = 0

programm_name = "Игра"

print('------------------------------------------------------------------')

pygame.init()
musictime = pygame.mixer.music.load("sounds/die_sound.mp3")

#pygame.mixer.music.play(2)

if random.randint(1, 50) == 50: #дополнение с шансом 1:50
    icon = pygame.image.load('__doors__/shadow.bmp')
    print('Shadow is loaded.')
    time.sleep(1)
    bg = pygame.image.load('__doors__/fon_blood.bmp')
    print('Blood room is loaded.')
    time.sleep(1)
    programm_name = "DOORS 2D"
    print('DOORS ROBLOX scripts are loaded.')
else: #на случай, если шанс не сработает
    icon = pygame.image.load('__rooms__/app.bmp')
    bg = pygame.image.load('__rooms__/fon.bmp') #создаём фон
    
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption(programm_name)

#координаты главного героя
x = W / 2
y = H / 2
# x_1 и y_1 - координаты "посылки"
x_1 = x / 3
y_1 = y
# x_2 и y_2 - координаты "дома"
x_2 = x_1
y_2 = y / 5

speed = 55
clock = pygame.time.Clock()

cube_1 = pygame.image.load('__rooms__/cube1.bmp')
cube1_rect = cube_1.get_rect(center = (x, y))

cube_2 = pygame.image.load('__rooms__/cube2.bmp')
cube2_rect = cube_2.get_rect(center = (x_1, y_1))

home = pygame.image.load('__rooms__/home.bmp')
home_rect = home.get_rect(center = (x_2, y_2))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(name, ', игра окончена. Всего ходов:', hod ,'.')
            exit()
    keys = pygame.key.get_pressed()
    #пишем код для главного героя
    if keys[pygame.K_LEFT]:
        dx = -1
        dy = 0
        
        cube1_rect.x -= speed

        if cube1_rect.x < 0:
            cube1_rect.x = 0
        
        hod += 1
        print('<---')
        if cube1_rect.x == cube2_rect.x and cube1_rect.y == cube2_rect.y:
            x_1 -= speed
            cube2_rect.x -= speed
            
    if keys[pygame.K_RIGHT]:
        cube1_rect.x += speed

        if cube1_rect.x < 0:
            cube1_rect.x = 0
        if cube1_rect.x == cube2_rect.x and cube1_rect.y == cube2_rect.y:
            cube2_rect.x += speed
        hod += 1
        print('--->')
            
    if keys[pygame.K_DOWN]:
        cube1_rect.y += speed

        if cube1_rect.y < 0:
            cube1_rect.y = 0
            
        hod += 1
        print('↓')
            
    if keys[pygame.K_UP]: #код UP
        cube1_rect.y -= speed
        
        if cube1_rect.y < 0:
            cube1_rect.y = 0
        print('↑')
                
    #пишем код для "дома"
    if x_box == x_home and y_box == y_home:
        print('Новое достижение!')
        time.sleep(2)
        print('A-1000')
        print('Я не чуствую своих ног...')
        time.sleep(5)
        print()
        print('Всего ходов:', hod, '! Через несколько секунд закроется окно.')
        time.sleep(5)
        exit()
     
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255, 255, 255), (x / 1.065, y / 1.065, 50, 50))
    pygame.draw.rect(screen, (255, 255, 255), (x_1 / 1.065, y_1 / 1.065, 50, 50))
    screen.blit(bg, (0, 0))
    screen.blit(home, home_rect)
    screen.blit(cube_1, cube1_rect)
    screen.blit(cube_2, cube2_rect)
    
    
    pygame.display.update()
    clock.tick(FPS)