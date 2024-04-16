from .body import Body
from particle import Particle
from constraint import Constraint
from material import Material

class Rope(Body):
    """A simple rope made of a chain of particles and constraints. The rope is fixed at the top and
    can swing around. The last particle in the chain can be given an initial impulse to start a swing.
    """
    def __init__(self, x, y, num_nodes, node_spacing, mass=10, initial_impulse=None, stiffness=0.05, **kwargs):
        fixed_material = Material(0, 0, 0)
        material = Material(0.2, 0.2, mass / num_nodes)

        particles = []
        constraints = []
        previous = Particle(fixed_material, x, y, 4)
        for i in range(1, num_nodes):  # Already added the first one
            particle_y = y + i * node_spacing
            particle = Particle(material, x, particle_y, 4)
            if previous is not None:
                constraints.append(Constraint(previous, particle, stiffness, True))
            particles.append(particle)
            previous = particle

        particles[-1].initial_impulse = initial_impulse  # Apply initial impulse to last particle in the chain

        super().__init__(particles, constraints, **kwargs)
