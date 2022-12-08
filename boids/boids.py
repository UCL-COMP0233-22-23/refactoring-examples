"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

def initialise_boids(lower_bound_x, upper_bound_x, lower_bound_y, upper_bound_y,
lower_bound_velocity_x, upper_bound_velocity_x, lower_bound_velocity_y,upper_bound_velocity_y, total_boids):
    boids_x = []
    boids_y = []
    boid_x_velocities = []
    boid_y_velocities = []

    for x in range (total_boids):
        boids_x.append(random.uniform(lower_bound_x,upper_bound_x))
        boids_y.append(random.uniform(lower_bound_y,upper_bound_y))
        boid_x_velocities.append(random.uniform(lower_bound_velocity_x, upper_bound_velocity_x))
        boid_y_velocities.append(random.uniform(lower_bound_velocity_y, upper_bound_velocity_y))
    
    return (boids_x,boids_y,boid_x_velocities,boid_y_velocities)


def update_boids(boids):
    xs,ys,xvs,yvs=boids
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
    # Move according to velocities
    for i in range(len(xs)):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]

if __name__ == '__main__':
    print(initialise_boids(-450, 50, 300, 600, 0, 10.0, -20, 20, 50))