# Experiment - 12 : Matplotlib - Plots & Visualizations
# ============================================================

import matplotlib.pyplot as plt
import numpy as np


# Q1. WAP to plot a simple graph using plot()

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.plot(x, y, linestyle='--', color='r', marker='o', label="Data Line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid()
plt.show()

# Output:
# [A line chart is displayed with dashed red line, circle markers,
#  grid, legend and title "Simple Line Plot"]


# -------------------------------------------------------

# Q2. WAP to draw the scatter and bar plot

# Scatter plot
x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 7]
plt.scatter(x, y, color='b', label="Scatter Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values     = [3, 7, 8, 5]
plt.bar(categories, values, color='g', label="Bar Data")
plt.xlabel("Categories")
plt.legend()
plt.show()

# Output:
# [Scatter plot with blue dots displayed]
# [Bar chart with green bars for categories A, B, C, D displayed]


# -------------------------------------------------------

# Q3. WAP to draw Histograms and Box plots

# Histogram
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
plt.hist(data, bins=5, color='purple', label="Histogram Data")
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Box plot
data = [3, 8, 5, 6, 9, 10, 15, 20, 21]
plt.boxplot(data)
plt.title("Box plot")
plt.show()

# Output:
# [Purple histogram with 5 bins displayed]
# [Box plot showing median, quartiles and outliers displayed]


# -------------------------------------------------------

# Q4. WAP to draw Pie Charts and Contour plots

# Pie chart
sizes   = [15, 30, 45, 10]
labels  = ['A', 'B', 'C', 'D']
colors  = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0)
plt.title("Pie Chart")
plt.axis('equal')
plt.show()

# Contour plot
x    = np.linspace(-5, 5, 50)
y    = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z    = np.sin(np.sqrt(x ** 2 + y ** 2))
plt.contour(x, y, z, levels=10, cmap='viridis')
plt.title("Contour Plot")
plt.colorbar()
plt.show()

# Output:
# [Pie chart with 4 colored slices, one exploded, displayed]
# [Viridis-colored contour plot displayed]


# -------------------------------------------------------

# Q5. WAP to draw the 3D-plot

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
x   = [1, 2, 3, 4, 5]
y   = [5, 6, 7, 8, 9]
z   = [2, 3, 3, 3, 2]
ax.scatter(x, y, z, color='r', label="3D Points")
ax.set_title("3D Scatter Plot")
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
plt.legend()
plt.show()

# Output:
# [3D scatter plot with red points and labeled axes displayed]
