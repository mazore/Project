import math

from .body import Body
from constraint import Constraint
from material import Material
from parameters import Parameters
from particle import Particle

class BallBase(Body):
    """The base class for two (or more) types of balls. A configuration with two layers of skins
    (outer and inner), that are connected by more stiff constraints, and a point in the middle that
    is connected to all the particles of the inner skin with a less stiff constraint.
    """
    def __init__(self, center_x, center_y, size,
                 num_steps, stiffness_outer, stiffness_inner, skin_size,
                 bounciness=0.2, initial_impulse=None, mass=20, **kwargs):

        num_particles = num_steps * 2 + 1
        material = Material(1, bounciness, mass / num_particles)
        # material = Material(1, bounciness, 1)
        particles = []
        constraints = []

        inner_size = size - skin_size

        # Center anchor point
        particles.append(Particle(material, center_x, center_y, 2, initial_impulse))

        # Generate particles
        outer = []
        inner = []
        for i in range(num_steps):
            angle = i / num_steps * (2 * math.pi)
            outer_offset = (2 * math.pi) / (2 * num_steps)
            outer_x = center_x + size * math.cos(angle + outer_offset)
            outer_y = center_y + size * math.sin(angle + outer_offset)
            outer.append(Particle(material, outer_x, outer_y, 2))
            inner_x = center_x + inner_size * math.cos(angle)
            inner_y = center_y + inner_size * math.sin(angle)
            inner.append(Particle(material, inner_x, inner_y, 2))
        particles.extend(outer)
        particles.extend(inner)

        # Connect outer skin
        for i in range(1, num_steps):
            constraints.append(Constraint(outer[i - 1], outer[i], stiffness_outer, True))
        constraints.append(Constraint(outer[len(outer)-1], outer[0], stiffness_outer, True))

        # Connect inner skin
        for i in range(1, num_steps):
            constraints.append(Constraint(inner[i - 1], inner[i], stiffness_outer, False))
        constraints.append(Constraint(inner[len(inner)-1], inner[0], stiffness_outer, False))

        # Connect outer and inner skins
        for i in range(num_steps):
            constraints.append(Constraint(outer[i], inner[i], stiffness_outer, False))
        for i in range(1, num_steps):
            constraints.append(Constraint(outer[i-1], inner[i], stiffness_outer, False))
        constraints.append(Constraint(outer[len(outer)-1], inner[0], stiffness_outer, False))

        # Connect inner skins to anchor point
        for i in range(num_steps):
            constraints.append(Constraint(particles[0], inner[i], stiffness_inner, False))

        super().__init__(particles, constraints, **kwargs)
