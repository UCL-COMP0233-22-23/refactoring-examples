"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

boid_num = 50
boids_x=[random.uniform(-450,50.0) for x in range(boid_num)]
boids_y=[random.uniform(300.0,600.0) for x in range(boid_num)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(boid_num)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(boid_num)]
# boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)


class boids:
    def __init__(self):
        self.num = boid_num
        self.boids_x = boids_x
        self.boids_y = boids_y
        self.boid_x_velocities = boid_x_velocities
        self.boid_y_velocities = boid_y_velocities

def update_boids(boids):
    xs = boids.boids_x
    ys = boids.boids_y
    xvs = boids.boid_x_velocities
    yvs = boids.boid_y_velocities
    # Fly towards the middle
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)

    for i in range(len(xs)):
        for j in range(len(xs)):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)

    # Fly away from nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
    boids.boid_x_velocities = xvs
    boids.boid_y_velocities = yvs
    # Move according to velocities
    for i in range(len(xs)):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]
    boids.boids_x = xs
    boids.boids_y = ys
    return boids

boids1 = boids(boid_num,boids_x,boids_y,boid_x_velocities,boid_y_velocities)
update_boids(boids1)
# print(boids.boids_x)
