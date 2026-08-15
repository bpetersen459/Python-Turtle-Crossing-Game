from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speeds = ["slowest", "slow", "normal", "fast", "fastest"]
        self.create_cars()
        self.hideturtle()
        self.no_overlap()
        self.move()

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=random.randrange(300, 320), y=random.randrange(-200, 280))
            self.all_cars.append(new_car)

    def no_overlap(self):
        for i in range(1, len(self.all_cars)):
            current = self.all_cars[i]
            previous = self.all_cars[i - 1]
            if current.distance(previous) < 10:
                current.goto(x=random.randrange(-300, 320), y=random.randrange(-280, 280))

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(MOVE_INCREMENT)
