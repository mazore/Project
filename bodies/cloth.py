import random

from .body import Body
from particle import Particle
from constraint import Constraint
from material import Material
from vector2 import Vector2

# Optimal steps per frame: 2
class Cloth(Body):
    def __init__(self, center_x, center_y, num_rows, num_cols, node_spacing, stiffness=1, initial_impulse=None, **kwargs):
        fixed_material = Material(0, 0, 0)
        material = Material(0.2, 0.2, 1)

        left_x = center_x - num_cols * node_spacing / 2
        top_y = center_y - num_rows * node_spacing / 2

        particles = []  # 2d array that is flattened before being passed to the super constructor
        for row_number in range(num_rows):
            row = []
            for col_number in range(num_cols):
                particle_x = left_x + col_number * node_spacing
                particle_y = top_y + row_number * node_spacing
                mat = fixed_material if row_number == 0 else material
                row.append(Particle(mat, particle_x, particle_y, 0))
            particles.append(row)

        constraints = []
        for row_number in range(num_rows):  # Horizontal constraints
            for col_number in range(num_cols - 1):
                p1 = particles[row_number][col_number]
                p2 = particles[row_number][col_number + 1]
                constraints.append(Constraint(p1, p2, stiffness, True))
        for col_number in range(num_cols):  # Vertical constraints
            for row_number in range(num_rows - 1):
                p1 = particles[row_number][col_number]
                p2 = particles[row_number + 1][col_number]
                constraints.append(Constraint(p1, p2, stiffness, True))

        if type(initial_impulse) is Vector2:
            for i in range(num_cols):
                particles[-1][i].initial_impulse = initial_impulse  # Apply initial impulse to bottom row of the cloth
        elif initial_impulse == 'randomized':
            for i in range(num_cols):  # Apply random impulse to each particle in the bottom row of the cloth
                # particles[-1][i].initial_impulse = Vector2(5, random.random() * -10)
                particles[-1][i].force(Vector2(5, random.random() * -500))

        # Flatten particles 2d array into a 1d array
        particles = [particle for row in particles for particle in row]

        super().__init__(particles, constraints, **kwargs)
