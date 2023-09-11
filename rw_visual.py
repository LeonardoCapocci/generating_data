import matplotlib.pyplot as plt

from randomwalk import RandomWalk

# Make a random walk.

rw = RandomWalk()
rw.fill_walk()

# Plot the points
plt.style.use('classic')
fix, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values)
ax.set_aspect('equal')
plt.show()