import math
import pygame as pg
import time
from boundary import Boundary
from parameters import Parameters
from vector2 import Vector2

SW = Parameters.SIMULATION_WIDTH
SH = Parameters.SIMULATION_HEIGHT

class Simulation:
    def __init__(self, bodies, steps_per_frame=4):
        self.bodies = bodies
        self.grabbed_particle = None

        Parameters.STEPS_PER_FRAME = steps_per_frame
        Parameters.TIME_DELTA = 1 / steps_per_frame

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
        while True:
            self.check_user_input()

            frame_start = time.time_ns()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.simulate()
            self.render()
            pg.display.update()

            compute_time = (time.time_ns() - frame_start) / 1_000_000  # In milliseconds
            inter_frame_delay = 1000 / Parameters.FRAME_RATE
            if compute_time < inter_frame_delay:
                pg.time.delay(int(inter_frame_delay - compute_time))

    def simulate(self):
        for _ in range(Parameters.STEPS_PER_FRAME):
            for body in self.bodies:
                other_bodies = [b for b in self.bodies if b.id != body.id]
                for particle in body.particles:
                    particle.accelerate(Parameters.GRAVITY)
                    particle.simulate()
                    particle.simulate_boundaries(self.static_boundaries, other_bodies)
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

    def check_user_input(self):
        if pg.mouse.get_pressed()[0]:  # Left click
            if self.grabbed_particle is None:
                closest = self.closest_particle_to_mouse()
                if closest[1] < Parameters.MAX_GRAB_RADIUS ** 2:
                    self.grabbed_particle = closest[0]
            if self.grabbed_particle is not None:
                mouse_pos = Vector2(*pg.mouse.get_pos())
                # self.grabbed_particle.position = mouse_pos
                # self.grabbed_particle.previous_pos = mouse_pos
                force = (mouse_pos - self.grabbed_particle.position) * Parameters.GRAB_STRENGTH
                self.grabbed_particle.force(force)
        else:
            self.grabbed_particle = None

    def closest_particle_to_mouse(self):
        mouse_pos = Vector2(*pg.mouse.get_pos())
        closest = None
        closest_dist = math.inf
        for body in self.bodies:
            for particle in body.particles:
                dist_squared = (particle.position.x - mouse_pos.x)**2 + (particle.position.y - mouse_pos.y)**2
                if dist_squared < closest_dist:
                    closest = particle
                    closest_dist = dist_squared
        return closest, closest_dist
