import turtle
import random

width = 500
height = 500
foodsize = random.randint(10, 20)
delay = 100

offsets = {
    "up" : (0, 20),
    "down" : (0, -20),
    "left" : (-20, 0),
    "right" : (20, 0)
}

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_down():
    if snake_dir != "up":
        snake_dir = "down"

def go_right():
    if snake_dir != "left":
        snake_dir = "right"

def go_left():
    if snake_dir != "right":
        snake_dir = "left"

def food_collision():
    global food_position

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1)**2 + (x2 - x1)**2)**0.5
    return distance

def get_random_food_position():
    x = random.randint(-width/2 + foodsize, width/2 - foodsize)
    y = random.randint(-height/2 + foodsize, height/2 - foodsize)
    return x,y