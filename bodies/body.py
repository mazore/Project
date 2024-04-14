import pygame as pg

class Body:
    def __init__(self, particles, constraints, color=(48, 48, 48)):
        self.particles = particles
        self.constraints = constraints
        self.color = color

    def apply_initial_impulses(self):
        for particle in self.particles:
            if particle.initial_impulse is not None:
                particle.impulse(particle.initial_impulse)

    def draw(self, canvas):
        for particle in self.particles:
            pg.draw.circle(canvas, self.color, particle.position.intTuple(), particle.radius * 2, 0)
        for constraint in self.constraints:
            pos1 = constraint.particle1.position.intTuple()
            pos2 = constraint.particle2.position.intTuple()
            pg.draw.line(canvas, self.color, pos1, pos2, 1)
