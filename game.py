#Паспорт игры
#Название: RedMan
#Жанр: аркада,риключения
#Идея: игрок управляет красным персонажем,
#собирает предметы и избегает препятствий(микробов).
#размер окна: 600 x 600
import pygame
#константы и фон
WIDTH=600
HEIGHT=600
FPS=60
BG_COLOR=(25, 30, 55)
#инициализация Pygame и окна
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RedMan")
clock=pygame.time.Clock()
#главный цикл
running=True
while running:
    clock.tick(FPS)
    #Обработка событий
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #изменение состояния объектов и пока объектов нет
    #отрисовка
    screen.fill(BG_COLOR)
    pygame.display.update()
pygame.quit()
   
