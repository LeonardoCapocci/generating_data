import matplotlib.pyplot as plt

from randomwalk import RandomWalk

for x in range(5):
    # Make a random walk.

    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points
    plt.style.use('classic')
    fix, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=15)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none',
                s=100)

    plt.show()