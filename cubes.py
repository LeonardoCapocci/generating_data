import matplotlib.pyplot as plt

x_values = range(0, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax. scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=5)

# Titles
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

plt.tick_params(size=12)

plt.savefig('cubes.png', bbox_inches='tight')
plt.show()