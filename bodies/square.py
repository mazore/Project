from .body import Body
from constraint import Constraint
from material import Material
from parameters import Parameters
from particle import Particle

class Square(Body):
    def __init__(self, center_x, center_y, width, height, mass=20, bounciness=0.2, stiffness=0.05, initial_impulse=None, **kwargs):
        num_particles = 4
        material = Material(0.2, bounciness, mass / num_particles)
        particles = [
            Particle(material, center_x - width / 2, center_y + height / 2, 3),
            Particle(material, center_x - width / 2, center_y - height / 2, 3),
            Particle(material, center_x + width / 2, center_y - height / 2, 3),
            Particle(material, center_x + width / 2, center_y + height / 2, 3, initial_impulse),
        ]
        constraints = [
            Constraint(particles[0], particles[1], stiffness, True),
            Constraint(particles[1], particles[2], stiffness, True),
            Constraint(particles[2], particles[3], stiffness, True),
            Constraint(particles[3], particles[0], stiffness, True),
            Constraint(particles[0], particles[2], stiffness, False),
            Constraint(particles[1], particles[3], stiffness, False),
        ]

        super().__init__(particles, constraints, **kwargs)
