from boundary import Boundary

class Constraint:
    def __init__(self, particle1, particle2, stiffness, is_boundary):
        self.particle1 = particle1
        self.particle2 = particle2
        self.stiffness = stiffness  # Hooke's law spring constant, 0 (no stiffness) to 1 (most rigid)
        self.is_boundary = is_boundary

        self.target_dist = particle1.position.distance(particle2.position)

    def update(self):
        D = self.particle2.position - self.particle1.position
        F = D.normalized() * 0.5 * self.stiffness * (D.length() - self.target_dist)  # From hooke's law
        if self.particle1.material.mass != 0.0 and not self.particle2.material.mass:
            self.particle1.impulse(2 * F)
        elif not self.particle1.material.mass and self.particle2.material.mass != 0.0:
            self.particle2.impulse(-2 * F)
        else:
            self.particle1.impulse(F)
            self.particle2.impulse(-F)

    def get_boundary(self):
        return Boundary(self.particle1.position, self.particle2.position)
