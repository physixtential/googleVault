# Earth-moon system using Euler's method

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
G = 6.67408e-11
massEarth = 5.972e24
massMoon = massEarth #7.348e22

# Function for Euler integration
def eulerIntegrate(position, velocity, dt):
    return position + velocity * dt

# Function to calculate the gravitational force between two objects
def gravitationalForce(position1, position2, mass1, mass2):
    vectorBetween = position2 - position1
    distance = np.sqrt(vectorBetween[0]**2 + vectorBetween[1]**2)
    direction = vectorBetween / distance
    return G * mass1 * mass2 / distance**2 * direction

# Earth and moon position vectors
earthPosition = np.array([0.0, 0.0]) 
moonPosition = np.array([405e6, 0.0]) # Moon farthest from earth in m

# Zero momentum frame 0 = m1*v1 + m2*v2
# m1*v1 = -m2*v2
# v1 = -m2*v2/m1

# Earth and moon velocity vectors
moonVelocity = np.array([0.0, 500.0]) # Orbital velocity of moon in m/s
earthVelocity = -massMoon*moonVelocity/massEarth

# Set the time step for integration
dt = .01*24*60*60 # seconds

# Orbital period of the moon in seconds
# 27.322*24*60*60

# Lists to store positions for plotting
earthPositionList = []
moonPositionList = []

# Simulate the earth-moon system using Euler integration
for i in range(0, 10000):
    # Calculate the gravitational force on the earth
    earthForce = gravitationalForce(earthPosition, moonPosition, massEarth, massMoon)

    # Calculate the gravitational force on the moon
    moonForce = -earthForce

    # Update the earth's velocity
    earthVelocity = earthVelocity + earthForce / massEarth * dt

    # Update the moon's velocity
    moonVelocity = moonVelocity + moonForce / massMoon * dt

    # Update the earth's position
    earthPosition = eulerIntegrate(earthPosition, earthVelocity, dt)

    # Update the moon's position
    moonPosition = eulerIntegrate(moonPosition, moonVelocity, dt)

    # Add positions to the lists for plotting
    earthPositionList.append(earthPosition)
    moonPositionList.append(moonPosition)

# Convert the lists to numpy arrays
earthPositionList = np.array(earthPositionList)
moonPositionList = np.array(moonPositionList)

# Animate the earth-moon system using matplotlib animation
fig = plt.figure()
ax = plt.axes(xlim=(-5e8, 5e8), ylim=(-5e8, 5e8))
ax.set_aspect('equal', adjustable='box')
line, = ax.plot([], [], 'bo', markersize=10)
line2, = ax.plot([], [], 'ro', markersize=5)

# Add a trail to both objects
trail, = ax.plot([], [], 'b-', linewidth=1)
trail2, = ax.plot([], [], 'r-', linewidth=1)

# Function to initialize the animation
def init():
    line.set_data([], [])
    line2.set_data([], [])
    trail.set_data([], [])
    trail2.set_data([], [])
    return line, line2, trail, trail2

# Function to update the animation
def animate(i):
    line.set_data(earthPositionList[i, 0], earthPositionList[i, 1])
    line2.set_data(moonPositionList[i, 0], moonPositionList[i, 1])
    trail.set_data(earthPositionList[:i, 0], earthPositionList[:i, 1])
    trail2.set_data(moonPositionList[:i, 0], moonPositionList[:i, 1])
    return line, line2, trail, trail2

# Create animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=10000, interval=1, blit=True)

# Show the animation
plt.show()


# What happens if you change the time step?
# Why does the earth look slightly off center? Is the center of mass at the origin?
# Why do you need smaller time steps for elliptical orbits?
# What happens if you change the mass of the moon?
# What happens if you change the distance between the earth and the moon?
# What happens if you change the velocity of the moon?

