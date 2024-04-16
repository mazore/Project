from vector2 import Vector2
from parameters import Parameters

class Particle:
    """Represents one point of mass, which is the foundation of this simulation. It is simulated
    with Verlet integration, which basically means that the velocity is calculated every step by the
    difference between the current and previous positions.
    """
    def __init__(self, material, x, y, radius, initial_impulse=None):
        self.position = Vector2(x, y)
        self.previous_pos = Vector2(x, y)
        self.material = material
        self.radius = radius
        self.initial_impulse = initial_impulse

        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

    def accelerate(self, vector):
        """Apply an acceleration to the particle"""
        self.acceleration += vector

    def force(self, force):
        """Apply a force to the particle"""
        if self.material.mass > 0:
            self.acceleration += force / self.material.mass

    def impulse(self, vector):
        """Apply an impulse to the particle"""
        if self.material.mass != 0:
            self.position += vector / self.material.mass

    def simulate(self):
        """Simulate the particle's position based on its velocity and acceleration using Verlet
        integration. This process happens several times per frame
        """

        if self.material.mass == 0:
            return  # If the particle has no mass then it is fixed in place, and doesn't move

        self.velocity = (self.position * 2) - self.previous_pos
        self.previous_pos = self.position
        self.position = self.velocity + self.acceleration * Parameters.TIME_DELTA**2
        self.velocity = self.position - self.previous_pos
        self.acceleration = Vector2(0, 0)

    def reset_acceleration(self):
        """Reset the acceleration to zero"""
        self.acceleration = Vector2(0, 0)

    def simulate_boundaries(self, static_boundaries, other_bodies):
        """Given constraints of the edges of the simulation (static_boundaries), and the edges of
        other bodies in the simlation, this function adjusts the position of this particle based on
        those factors
        """
        boundaries = [*static_boundaries]

        for other_body in other_bodies:
            for constraint in other_body.constraints:
                if constraint.is_boundary:
                    boundaries.append(constraint.get_boundary())

        for boundary in boundaries:
            if boundary.should_collide(self.position):
                self.adjust_position(boundary.normal, boundary.collision_point(self.position))

    def adjust_position(self, boundary_normal, boundary_point):
        """This is a version of the below adjust_position_2d with an abstraction made to generalize
        it to a constraint between two arbitrary points (represented by the Constrain object).
        """
        unit_boundary_normal = boundary_normal.normalized()  # The unit vector of the boundary normal
        displacement = self.position - self.previous_pos
        normal_displacement = displacement.dot(unit_boundary_normal)  # The displacement in the direction of the normal

        self.position = boundary_point - (self.position - boundary_point)  # Reflect across the boundary
        self.previous_pos = self.position + unit_boundary_normal * (self.material.bounce * normal_displacement)  # Move the previous position to apply appropriate amount of bounce

    def wall_boundaries(self):
        """This is legacy code that used to be used to simulate collisions with the walls"""
        if self.position.x < 0:
            self.adjust_position_2d('x', 0)
        elif self.position.x > Parameters.SIMULATION_WIDTH:
            self.adjust_position_2d('x', Parameters.SIMULATION_WIDTH)
        if self.position.y < 0:
            self.adjust_position_2d('y', 0)
        elif self.position.y > Parameters.SIMULATION_HEIGHT:
            self.adjust_position_2d('y', Parameters.SIMULATION_HEIGHT)

    def adjust_position_2d(self, axis, bounded_val):
        """This is legacy code that used to be used to adjust the position of the particle to not
        go outside the boundaries of the simulation. It is now replaced by the more general function
        adjust_position.
        """
        other_axis = 'y' if axis == 'x' else 'x'

        displacement = self.position - self.previous_pos

        self.position[axis] = bounded_val - (self.position[axis] - bounded_val)  # Reflect across the boundary
        self.previous_pos[axis] = self.position[axis] + self.material.bounce * displacement[axis]

        parallel_displacement = displacement[other_axis]
        # perpendicular_displacement = displacement[axis] * self.material.friction

        parallel_displacement_direction = parallel_displacement
        if parallel_displacement != 0:
            parallel_displacement_direction /= abs(parallel_displacement)

        self.position[other_axis] -= parallel_displacement
        # if abs(perpendicular_displacement) >= abs(parallel_displacement):  # Bounce
        #     # if parallel_displacement * parallel_displacement_direction > 0:  # Same sign
        #     self.position[other_axis] -= parallel_displacement
        # else:  # Sliding
        #     if perpendicular_displacement * parallel_displacement_direction > 0:  # Same sign
        #         self.position[other_axis] -= perpendicular_displacement
