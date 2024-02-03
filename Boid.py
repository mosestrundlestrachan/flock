import turtle
from random import randint
from Vector import Vector
import random
import math

class Boid:

    def border(self, distance, xmin, xmax, ymin, ymax):
        self.turtle.forward(distance)
        new_x = self.turtle.xcor() + distance * math.cos(
            math.radians(self.turtle.heading()))
        new_y = self.turtle.ycor() + distance * math.cos(
            math.radians(self.turtle.heading()))
        if new_x < xmin:
            new_x = xmin
            self.turtle.setheading(180 - self.turtle.heading())
        elif new_x > xmax:
            new_x = xmax
            self.turtle.setheading(180 - self.turtle.heading())
        if new_y < ymin:
            new_y = ymin
            self.turtle.setheading(-self.turtle.heading())
        elif new_y > ymax:
            new_y = ymax
            self.turtle.setheading(-self.turtle.heading())
        self.turtle.goto(new_x, new_y)

    def __init__(self, startx, starty, x, y):
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(randint(startx - 50, startx + 50), randint(starty - 50, starty + 50))
        self.angle = random.uniform(0.0, 2.0 * math.pi)
        self.velocity = turtle.Vec2D(1, 0)
        self.x = x
        self.y = y

    def cohere(self, boids):
        if len(boids) < 10:
            return turtle.pos()
        center_x, center_y = (0, 0)  # initialize to (0, 0)
        for boid in boids:
            if boid != self:
                center_x += boid.turtle.xcor()
                center_y += boid.turtle.ycor()
        center_x /= len(boids) - 1
        center_y /= len(boids) - 1
        center = (center_x, center_y)
        self.turtle.goto(center)
        return center

    def separate(self, boids):
        separation = (0, 0)
        for boid in [b for b in boids if b != self]:
            if self.distance(boid) < 2:
                separation = (separation[1] - (boid.turtle.xcor() - self.turtle.xcor()),
                              separation[0] - (boid.turtle.ycor() - self.turtle.ycor()))
        return separation

    def align(self, boids):
        if len(boids) < 2:
            return self.turtle.pos()

        x_list = []
        y_list = []

        for boid in [b for b in boids if b != self]:
            x_list.append(boid.turtle.xcor())
            y_list.append(boid.turtle.ycor())

        averageX = sum(x_list) / len(x_list)
        averageY = sum(y_list) / len(y_list)

        self.turtle.setheading(self.turtle.towards(averageX, averageY))
        self.turtle.forward(3)

    def flock(self, boids):
        cohesion = self.cohere(boids)
        separation = self.separate(boids)
        alignment = self.align(boids)
        self.velocity += (cohesion + separation + alignment)
        self.velocity = self.velocity.normalize()
        self.turtle.setheading(self.velocity.heading())
        self.turtle.forward(3)


    def position(self):
        return self.turtle.xcor(), self.turtle.ycor()

    def distance(self, other):
        return self.turtle.distance(other.turtle)

    def update(self, boids):
        neighbors = [b for b in boids if self.distance(b) < 150]
        self.cohere(neighbors)
        self.align(neighbors)
        self.separate(neighbors)
        self.turtle.setheading(.5)
        self.turtle.forward(3)

