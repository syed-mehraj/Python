import turtle
import time
import random
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'black', 'purple', 'pink', 'brown']
def get_no_of_racers():
    while True:
        racers = input('ENTER THE NUMBER OF RACERS (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print("enter in proper number system")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("inter the racers between 2-10")
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('turtle racing!')




racers = get_no_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors) #what is does is colors[:2]=first two elements of colours
winner = race(colors)
print(winner)
