import pygame as pg
from boundary import Boundary
from parameters import Parameters
from vector2 import Vector2

SW = Parameters.SIMULATION_WIDTH
SH = Parameters.SIMULATION_HEIGHT

class Simulation:
    def __init__(self, bodies):
        self.bodies = bodies

        self.static_boundaries = [
            # Edges of the screen
            Boundary(Vector2(SW, 0), Vector2(0, 0)),
            Boundary(Vector2(SW, SH), Vector2(SW, 0)),
            Boundary(Vector2(0, SH), Vector2(SW, SH)),
            Boundary(Vector2(0, 0), Vector2(0, SH)),
        ]


        pg.init()
        self.canvas = pg.display.set_mode((Parameters.SIMULATION_WIDTH, Parameters.SIMULATION_HEIGHT))
        pg.display.set_caption('Soft Body Simulation')

        for body in self.bodies:
            body.apply_initial_impulses()

    def mainloop(self):

        i = 0
        while True:
            i += 1
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.simulate()
            self.render()
            pg.display.update()
            pg.time.delay(1000 // Parameters.FRAME_RATE)

    def simulate(self):
        for _ in range(Parameters.STEPS_PER_FRAME):
            for body in self.bodies:
                for particle in body.particles:
                    particle.accelerate(Parameters.GRAVITY)
                    particle.simulate()
                    particle.simulate_boundaries(self.static_boundaries)
                    particle.reset_acceleration()

            for body in self.bodies:  # Update all the constraints after all the particles have updated
                for constraint in body.constraints:
                    constraint.update()

    def render(self):
        self.canvas.fill((255, 255, 255))  # White background
        for body in self.bodies:
            body.draw(self.canvas)
        for boundary in self.static_boundaries:
            pg.draw.line(self.canvas, (255, 48, 48), boundary.p1.intTuple(), boundary.p2.intTuple(), 1)
        pg.display.update()
