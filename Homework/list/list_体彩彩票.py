import random
import time
import os

# 初始化游戏
WIDTH = 20
HEIGHT = 10
snake = [(WIDTH//2, HEIGHT//2)]
food = None
direction = 'right'
score = 0
game_over = False

# 生成食物
def generate_food():
    global food
    while food is None:
        x = random.randint(1, WIDTH-2)
        y = random.randint(1, HEIGHT-2)
        if (x, y) not in snake:
            food = (x, y)

# 移动蛇
def move():
    global snake, food, game_over, score
    head = snake[-1]
    if direction == 'up':
        new_head = (head[0], head[1]-1)
    elif direction == 'down':
        new_head = (head[0], head[1]+1)
    elif direction == 'left':
        new_head = (head[0]-1, head[1])
    elif direction == 'right':
        new_head = (head[0]+1, head[1])
    if new_head[0] == 0 or new_head[0] == WIDTH-1 or new_head[1] == 0 or new_head[1] == HEIGHT-1 or new_head in snake:
        game_over = True
        return
    snake.append(new_head)
    if new_head == food:
        score += 1
        food = None
    else:
        snake.pop(0)

# 绘制游戏画面
def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Score: %d' % score)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print('O', end='')
            elif (x, y) == food:
                print('X', end='')
            elif y == 0 or y == HEIGHT-1 or x == 0 or x == WIDTH-1:
                print('#', end='')
            else:
                print(' ', end='')
        print()

# 处理输入事件
def handle_input(key):
    global direction
    if key == 'up' and direction != 'down':
        direction = 'up'
    elif key == 'down' and direction != 'up':
        direction = 'down'
    elif key == 'left' and direction != 'right':
        direction = 'left'
    elif key == 'right' and direction != 'left':
        direction = 'right'

# 游戏主循环
while not game_over:
    generate_food()
    draw()
    move()
    if game_over:
        print('Game over! Your score is %d.' % score)
        break
    time.sleep(0.2)
    key = input('Please enter a direction (up/down/left/right): ')
    handle_input(key)

