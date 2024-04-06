import pygame 
pygame.init()

# Размер экрана
w_and_s = 1000
color_box_x = 50 # Заданию длину прямоугольнка для выбора цветом он будет залит определоным цветом
color_box_y = 30 # А здесь ширину

screen = pygame.display.set_mode((w_and_s, w_and_s))
pygame.display.set_caption('Paint')

# Задаю цвета
radius = 3 # Задаю радиус, он выступает в своем роде кисть и им рисуют, им можно менять толщину
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0) 
ORANGE = (255, 165, 0)  

# Область для рисования
drawing_area = pygame.Surface((w_and_s - color_box_x - 20, w_and_s))

# Здесь создаю буллевые переменые для удобства в будущем 
run = True
drawing = False
previous_point = None
draw_circle = False
draw_square = False
draw_right_triang = False # Рисовать прямоугольный треугольник
draw_equal = False # Рисовать правильный(равносторонний) треугольник
draw_rhombus = False # Рисовать ромб
draw_rect = False # Рисоваить прямоугольник

r_circle = 20 # Задаю радиус круга как готовую фигуру
side_square = 50 # Задаю длину стороны квадрата как готовую фигуру
color = RED # Изначальный цвет для рисовки

eraser = pygame.image.load('eraser.png') # Фото ластика
rectanglep = pygame.image.load('figures/rectanglep.png')
circlep = pygame.image.load('figures/circlep.png')
equilp = pygame.image.load('figures/equilp.png')
squarep = pygame.image.load('figures/squarep.png')
right_trianglep = pygame.image.load('figures/right_trianglep.png')
rhombus = pygame.image.load('figures/rhombusp.png')


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # Для прекращения работы программы
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                if event.pos[0] > color_box_x + 20:  # Если клик произошел в области для рисования
                    drawing = not drawing # Использую,чтобы при повторном нажатии он перестовал рисовать
                    if not drawing:
                        previous_point = None 

    if drawing:
        x, y = pygame.mouse.get_pos() # Получает местоложение курсора
        current_point = (x - color_box_x - 20, y)  # Сдвигаю координаты мыши, чтобы они соответствовали области для рисования
        if previous_point is not None: # Прекращает следовать за предыдущей точкой, если было повторное нажатие
            pygame.draw.line(drawing_area, color, previous_point, current_point, radius)
        previous_point = current_point
    

    screen.fill((255, 255, 255))
    
    # Отрисовываю поле выбора цвета
    pygame.draw.rect(screen, RED, (10, 10, color_box_x, color_box_y))
    pygame.draw.rect(screen, GREEN, (10, 50, color_box_x, color_box_y))
    pygame.draw.rect(screen, BLUE, (10, 90, color_box_x, color_box_y))
    screen.blit(eraser, (10, 130)) # Ластик
    pygame.draw.rect(screen, YELLOW, (10, 170, color_box_x, color_box_y))
    pygame.draw.rect(screen, ORANGE, (10, 210, color_box_x, color_box_y))
    screen.blit(rectanglep,(10,250))
    screen.blit(circlep,(10,290))
    screen.blit(equilp,(10,330))
    screen.blit(squarep,(10,370))
    screen.blit(right_trianglep,(10,410))
    screen.blit(rhombus,(10,450))

    # Переношу рисованное на основное окно
    screen.blit(drawing_area, (color_box_x + 20, 0))
    
    # Обработка выбора цвета
    if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши нажата
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Проверяю, находится ли мышь на поле выбора цвета
        if 10 <= mouse_x <= color_box_x + 10:
            if 10 <= mouse_y <= 40:
                color = RED
                radius = 3
            elif 50 <= mouse_y <= 80:
                color = GREEN
                radius = 3
            elif 90 <= mouse_y <= 120:
                color = BLUE
                radius = 3
            elif 130 <= mouse_y <= 160: # Это своего рода ластик
                color = BLACK 
                radius = 20
            elif 170 <= mouse_y <= 200: 
                color = YELLOW 
                radius = 3
            elif 210 <= mouse_y <= 240: 
                color = ORANGE
                radius = 3
            elif 250 <= mouse_y <= 280:
                draw_rect = True
            elif 290 <= mouse_y <= 320:
                draw_circle = True
            elif 330 <= mouse_y <= 360:
                draw_equal = True
            elif 370 <= mouse_y <= 400:
                draw_square = True
            elif 410 <= mouse_y <= 440:
                draw_right_triang = True
            elif 450 <= mouse_y <=480:
                draw_rhombus = True
    if draw_rect and pygame.mouse.get_pressed()[2]:
        u,i = pygame.mouse.get_pos()
        pygame.draw.rect(drawing_area, color,(u-35,i-50,70,100))
        draw_rect = False
    # Но рисовать он будет только после нажатие на правую кнопку мыши и по положению этого курсора
    if draw_circle and pygame.mouse.get_pressed()[2]:
        q,w = pygame.mouse.get_pos()
        q -= r_circle // 2
        w -= r_circle // 2
        pygame.draw.circle(drawing_area, color, (q,w), r_circle)
        draw_circle = False # Это позволяет забыть после отрисовки фигуры, что позволяет рисовать его не только один раз, а большое количество
    
    if draw_equal and pygame.mouse.get_pressed()[2]:
        x,y = pygame.mouse.get_pos()
        coordin = [(x,y-43),(x+50,y + 43),(x-50,y+43)]
        pygame.draw.polygon(drawing_area,color,coordin)
        draw_equal = False
    
    #Для этого я и сделал такие переменые как "r,t,d,f", а [2] говоприт о правой кнопки мыши
    if draw_square and pygame.mouse.get_pressed()[2]:
        e,r = pygame.mouse.get_pos()
        e -= side_square // 2
        r -= side_square // 2
        pygame.draw.rect(drawing_area, color, (e,r, side_square, side_square))
        draw_square = False
    
    if draw_right_triang and pygame.mouse.get_pressed()[2]:
        t, y = pygame.mouse.get_pos()
        pygame.draw.polygon(drawing_area, color, [(t, y), (t + 100, y), (t + 100, y + 100)])
        draw_right_triang = False

    if draw_rhombus and pygame.mouse.get_pressed()[2]:
        o, p = pygame.mouse.get_pos()
        pygame.draw.polygon(drawing_area, color, [(o, p - 50), (o + 50, p), (o, p + 50), (o - 50, p)])
        draw_rhombus = False

    pygame.display.flip()

pygame.quit()
