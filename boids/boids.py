"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random



def distance(x1,x2,y1,y2):
    return (x1-x2)**2 + (y1-y2)**2

class boids:
    def __init__(self):
        self.num = boid_num
        self.boids_x = boids_x
        self.boids_y = boids_y
        self.boid_x_velocities = boid_x_velocities
        self.boid_y_velocities = boid_y_velocities

    def update_boids(self):
        pos_x = self.boids_x
        pos_y = self.boids_y
        vel_x = self.boid_x_velocities
        vel_y = self.boid_y_velocities
        # Fly towards the middle
        for i in range(self.num):
            for j in range(self.num):
                vel_x[i]=vel_x[i]+(pos_x[j]-pos_x[i])*0.01/self.num

        for i in range(self.num):
            for j in range(self.num):
                vel_y[i]=vel_y[i]+(pos_y[j]-pos_y[i])*0.01/self.num

        # Fly away from nearby boids
        for i in range(self.num):
            for j in range(self.num):
                if distance(pos_x[j],pos_x[i],pos_y[j],pos_y[i]) < 100:
                    vel_x[i]=vel_x[i]+(pos_x[i]-pos_x[j])
                    vel_y[i]=vel_y[i]+(pos_y[i]-pos_y[j])
        # Try to match speed with nearby boids
        for i in range(self.num):
            for j in range(self.num):
                if distance(pos_x[j],pos_x[i],pos_y[j],pos_y[i]) < 10000:
                    vel_x[i]=vel_x[i]+(vel_x[j]-vel_x[i])*0.125/self.num
                    vel_y[i]=vel_y[i]+(vel_y[j]-vel_y[i])*0.125/self.num
        self.boid_x_velocities = vel_x
        self.boid_y_velocities = vel_y
        # Move according to velocities
        for i in range(self.num):
            pos_x[i]=pos_x[i]+vel_x[i]
            pos_y[i]=pos_y[i]+vel_y[i]
        self.boids_x = pos_x
        self.boids_y = pos_y
        return self


boid_num = 50
boids_x=[random.uniform(-450,50.0) for x in range(boid_num)]
boids_y=[random.uniform(300.0,600.0) for x in range(boid_num)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(boid_num)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(boid_num)]
# boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

boids1 = boids(boid_num,boids_x,boids_y,boid_x_velocities,boid_y_velocities)
boids1.update_boids(boids1)
# print(boids1.boids_x)
