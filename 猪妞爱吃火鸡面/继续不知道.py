import pygame
from sys import exit   #close everything

pygame.init()
screen = pygame.display.set_mode((1000,600))   #width,heigth
pygame.display.set_caption('猪妞爱吃火鸡面')
clock = pygame.time.Clock()  #设置游戏帧率
test_font = pygame.font.Font(None,50)


sky_surface = pygame.image.load(r"D:\猪妞爱吃火鸡面\角色情况\sky.jpg").convert()
ground_surface = pygame.image.load(r"D:\猪妞爱吃火鸡面\角色情况\ground.jpg").convert()
text_surface = test_font.render('XNXF',False,'Black')

enermy_surface = pygame.image.load(r"D:\猪妞爱吃火鸡面\角色情况\敌人\423e6a4ad3aa93fdca8d9c66f5bcdd41.png").convert_alpha()
enermy_x_position = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,-100))
    screen.blit(ground_surface,(0,500))
    screen.blit(text_surface,(400,100))
    enermy_x_position -= 4
    if enermy_x_position < -100:enermy_x_position = 1000
    screen.blit(enermy_surface,(enermy_x_position,320))
   
    pygame.display.update()
    clock.tick(60)
