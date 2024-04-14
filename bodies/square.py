from .body import Body
from constraint import Constraint
from material import Material
from parameters import Parameters
from particle import Particle

class Square(Body):
    def __init__(self, center_x, center_y, width, height, bounciness=0.2, initial_impulse=None, **kwargs):
        material = Material(0.2, bounciness, 1)
        particles = [
            Particle(material, center_x - width / 2, center_y + height / 2, 3),
            Particle(material, center_x - width / 2, center_y - height / 2, 3),
            Particle(material, center_x + width / 2, center_y - height / 2, 3),
            Particle(material, center_x + width / 2, center_y + height / 2, 3, initial_impulse),
        ]
        constraints = [
            Constraint(particles[0], particles[1], 0.05, True),
            Constraint(particles[1], particles[2], 0.05, True),
            Constraint(particles[2], particles[3], 0.05, True),
            Constraint(particles[3], particles[0], 0.05, True),
            Constraint(particles[0], particles[2], 0.05, False),
            Constraint(particles[1], particles[3], 0.05, False),
        ]

        super().__init__(particles, constraints, **kwargs)
