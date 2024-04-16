import pygame as pg

class Body:
    """The base class for all bodies that can be simulated."""
    NUM_BODIES = 0

    def __init__(self, particles, constraints, color=(48, 48, 48)):
        self.particles = particles
        self.constraints = constraints
        self.color = color
        self.id = Body.NUM_BODIES  # Unique for each body
        Body.NUM_BODIES += 1

    def apply_initial_impulses(self):
        for particle in self.particles:
            if particle.initial_impulse is not None:
                particle.impulse(particle.initial_impulse)

    def draw(self, canvas):
        for particle in self.particles:  # Draw a circle for each particle
            pg.draw.circle(canvas, self.color, particle.position.intTuple(), particle.radius * 2, 0)
        for constraint in self.constraints:  # Draw a line for each constraint
            pos1 = constraint.particle1.position.intTuple()
            pos2 = constraint.particle2.position.intTuple()
            pg.draw.line(canvas, self.color, pos1, pos2, 1)
