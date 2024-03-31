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

r_circle = 20 # Задаю радиус круга как готовую фигуру
side_square = 50 # Задаю длину стороны квадрата как готовую фигуру
color = RED # Изначальный цвет для рисовки

eraser = pygame.image.load('eraser.png') # Фото ластика

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
            elif 170 <= mouse_y <= 200: # В этой областе не только можно будет выбирать цвет, но и круг этого же цвета
                color = YELLOW # выбрать цвет и нажать на правую кнопку мыши
                radius = 3
                draw_circle = True
            elif 210 <= mouse_y <= 240: # ТОже самое, но и квадрат
                color = ORANGE
                radius = 3
                draw_square = True
    
    # Но рисовать он будет только после нажатие на правую кнопку мыши и по положению этого курсора
    if draw_circle and pygame.mouse.get_pressed()[2]:
        r,t = pygame.mouse.get_pos()
        pygame.draw.circle(drawing_area, color, (r,t), r_circle)
        draw_circle = False # Это позволяет забыть после отрисовки фигуры, что позволяет рисовать его не только один раз, а большое количество
    
    #ДЛя этого я и сделал такие переменые как "r,t,d,f", а [2] говоприт о правой кнопки мыши
    if draw_square and pygame.mouse.get_pressed()[2]:
        d,f = pygame.mouse.get_pos()
        pygame.draw.rect(drawing_area, color, (d,f, side_square, side_square))
        draw_square = False
   
    pygame.display.flip()

pygame.quit()
