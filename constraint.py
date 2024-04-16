from boundary import Boundary

class Constraint:
    """Works to maintain a distance between its two particles based on Hooke's spring mechanics."""
    def __init__(self, particle1, particle2, stiffness, is_boundary):
        self.particle1 = particle1
        self.particle2 = particle2
        self.stiffness = stiffness  # Hooke's law spring constant, 0 (no stiffness) to 1 (most rigid)
        self.is_boundary = is_boundary  # Generally true if on the edge of the body

        self.target_dist = particle1.position.distance(particle2.position)

    def update(self):
        """Uses hooke's law to apply a force to either or both of the particles."""
        displacement = self.particle2.position - self.particle1.position
        force = displacement.normalized() * 0.5 * self.stiffness * (displacement.length() - self.target_dist)  # From hooke's law

        # Consider if one of the particles are fixed
        if self.particle1.material.mass != 0 and not self.particle2.material.mass:  # Particle 2 is fixed
            self.particle1.impulse(2 * force)
        elif not self.particle1.material.mass and self.particle2.material.mass != 0:  # Particle 1 is fixed
            self.particle2.impulse(-2 * force)
        else:  # Neither particle is fixed
            self.particle1.impulse(force)
            self.particle2.impulse(-force)

    def get_boundary(self):
        """Returns a boundary object that represents this line segment"""
        return Boundary(self.particle1.position, self.particle2.position)
