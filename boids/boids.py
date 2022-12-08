"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

#import random

# boids_x = [random.uniform(-450, 50.0) for x in range(50)]
# boids_y = [random.uniform(300.0, 600.0) for x in range(50)]
# boid_x_velocities = [random.uniform(0, 10.0) for x in range(50)]
# boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(50)]
# boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

boids_x = [-300.0, 20.0, 3.0]
boids_y = [420, 480, 540]
boids_x_velocities = [1.0, 2.0, 7.0]
boids_y_velocities = [-15.0, 10.0, 15.0]
boids = (boids_x, boids_y, boids_x_velocities, boids_y_velocities)

def update_boids(boids):
    x_pos, y_pos, x_vel, y_vel = boids
    number_of_boids = len(x_pos)

    for i in range(number_of_boids):
        for j in range(number_of_boids):
            diff_x = x_pos[j] - x_pos[i]
            diff_y = y_pos[j] - y_pos[i]
            # Fly towards the middle
            x_vel[i] = x_vel[i] + (diff_x) * 0.01 / number_of_boids
            y_vel[i] = y_vel[i] + (diff_y) * 0.01 / number_of_boids
            # Fly away from nearby boids
            if (diff_x) ** 2 + (diff_y) ** 2 < 100:
                x_vel[i] = x_vel[i] + (diff_x)
                y_vel[i] = y_vel[i] + (diff_y)
            # Try to match speed with nearby boids
            if (diff_x) ** 2 + (diff_y) ** 2 < 10000:
                x_vel[i] = x_vel[i] + (x_vel[j] - x_vel[i]) * 0.125 / number_of_boids
                y_vel[i] = y_vel[i] + (y_vel[j] - y_vel[i]) * 0.125 / number_of_boids
        # Move according to velocities
        x_pos[i] = x_pos[i] + x_vel[i]
        y_pos[i] = y_pos[i] + y_vel[i]
    
    print(x_pos, y_pos, x_vel, y_vel)

update_boids(boids)
print("hi")