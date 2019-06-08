import random
import curses

#initialize screen
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh,sw,0,0)
w.keypad(True)
w.timeout(100)

#create snakes initial position
snake_x = sw/4
snake_y = sh/2

#snake initial coordinate (length = 3)
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2],
]

#initializing food
food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

#initial movement towards right
key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    #remains the same if key is invalid
    key = key if next_key == -1 else next_key

    #see if the game is lost
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    #add new head to the snake list
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head)

    #gameplay conditions
    if snake[0]==food:
        food = None
        while food is None:
            food = [random.randint(1, sh), random.randint(1, sw)]
            if food in snake:
                food = None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], ACS_CKBOARD)