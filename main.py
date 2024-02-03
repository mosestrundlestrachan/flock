import turtle
import math
from Boid import Boid
from Vector import Vector
from random import randint

def circle():
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.sety(-500)
    t.pendown()
    t.circle(500)
    t.hideturtle()

#turtle.tracer(0, 0)

def main():
    # Create boids
    no_of_boids = 10
    boids = []
    for n in range(no_of_boids):
        boid = Boid(randint(-175, 175), randint(-175, 175), 0,0)
        boids.append(boid)

    # Update boids
    while True:
        turtle.update()
        #avoid_same_location(boids, 25)  # Call avoid_same_location only once for all boids
        for boid in boids:
            boid.update(boids)






if __name__ == '__main__':
    circle()
    main()

""""
def avoid_same_location(boids, separation_distance):
    """""




"""""
for boid in boids:
        # Get all boids that are too close
        too_close_boids = [other_boid for other_boid in boids if
                           boid != other_boid and boid.distance(other_boid) < separation_distance]
        # If there are boids that are too close, move away from them
        if too_close_boids:
            # Calculate the average location of the too close boids
            avg_x = sum([other_boid.x for other_boid in too_close_boids]) / len(too_close_boids)
            avg_y = sum([other_boid.y for other_boid in too_close_boids]) / len(too_close_boids)
            average_location = (avg_x, avg_y)
            # Calculate the vector from the boid to the average location
            dx = boid.x - average_location[0]
            dy = boid.y - average_location[1]
            dist = math.sqrt(dx**2 + dy**2)
            move_away_vector = ((dx / dist) * separation_distance, (dy / dist) * separation_distance)
            # Move the boid slightly away from the average location
            boid.x += move_away_vector[0]
            boid.y += move_away_vector[1]
            """""
