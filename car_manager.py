from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5



class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.chances = 6


    def new_car(self):
        random_chance = random.randint(1,self.chances)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.car_speed = STARTING_MOVE_DISTANCE
            car.goto(300, (random.randint(-250, 250)))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)


    def next_level(self):
        self.car_speed += MOVE_INCREMENT
        self.chances -= 1








