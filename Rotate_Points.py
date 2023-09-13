import math
import matplotlib.pyplot as plt


def rotate_point(x, y, angle):
    # Convert angle to radians
    angle_rad = math.radians(angle)

    # Calculate the new coordinates after rotation
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)

    return new_x, new_y


# Read the points from the text file
with open("points.txt", "r") as file:
    points = [tuple(map(float, line.strip().split(","))) for line in file]

# Specify the rotation angle in degrees
rotation_angle = -10

# Rotate each point and store the results
rotated_points = [rotate_point(x, y, rotation_angle) for x, y in points]

# Extract the x and y coordinates of the original and rotated points
x_original = [point[0] for point in points]
y_original = [point[1] for point in points]
x_rotated = [point[0] for point in rotated_points]
y_rotated = [point[1] for point in rotated_points]

# Create a scatter plot of the original and rotated points
plt.scatter(x_original, y_original, label="Original Points")
plt.scatter(x_rotated, y_rotated, label="Rotated Points")

# Set labels and title for the plot
plt.axis("scaled")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Rotation of Points")

# Add a legend
plt.legend()

# Display the plot
plt.show()
