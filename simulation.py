import math
import pygame as pg
import time
from bodies import *
from boundary import Boundary
from parameters import Parameters
from vector2 import Vector2

SW = Parameters.SIMULATION_WIDTH
SH = Parameters.SIMULATION_HEIGHT

class Simulation:
    """Manages all bodies necessary in the scene. It creates a pygame canvas, configures it, and
    runs the mainloop.
    """
    def __init__(self, bodies, steps_per_frame=4):
        self.bodies = bodies
        self.grabbed_particle = None  # If a particle is grabbed by the mouse

        Parameters.STEPS_PER_FRAME = steps_per_frame
        Parameters.TIME_DELTA = 1 / steps_per_frame

        self.static_boundaries = [
            # Edges of the screen
            Boundary(Vector2(SW, 0), Vector2(0, 0)),
            Boundary(Vector2(SW, SH), Vector2(SW, 0)),
            Boundary(Vector2(0, SH), Vector2(SW, SH)),
            Boundary(Vector2(0, 0), Vector2(0, SH)),
        ]

        # Setup pygame
        pg.init()
        self.canvas = pg.display.set_mode((Parameters.SIMULATION_WIDTH, Parameters.SIMULATION_HEIGHT))
        pg.display.set_caption('Soft Body Simulation')

        for body in self.bodies:
            body.apply_initial_impulses()

    def mainloop(self):
        """First checks the user input for mouse actions (dragging bodies), quits if pygame has sent
        that event, simulates the movement of all particles and constraints, and renders all bodies.
        Makes sure the frame rate is not exceeded
        """
        while True:
            frame_start = time.time_ns()

            self.check_user_input()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                # if event.type == pg.MOUSEBUTTONDOWN:
                #     if event.button == 3:
                #         self.bodies.append(Square(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], 100, 100, stiffness=0.03))
            self.simulate()
            self.render()
            pg.display.update()

            compute_time = (time.time_ns() - frame_start) / 1_000_000  # In milliseconds
            inter_frame_delay = 1000 / Parameters.FRAME_RATE
            if compute_time < inter_frame_delay:
                pg.time.delay(int(inter_frame_delay - compute_time))

    def simulate(self):
        """Simulates Verlet integration on all particles and spring (Hooke's) physics on all constraints"""
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
        """Renders all bodies on the canvas"""
        self.canvas.fill((255, 255, 255))  # White background
        for body in self.bodies:
            body.draw(self.canvas)
        pg.display.update()

    def check_user_input(self):
        """Checks for mouse grabbing a particle and applies a force to it if it is grabbed"""
        if pg.mouse.get_pressed()[0]:  # Left click
            if self.grabbed_particle is None:
                closest = self.closest_particle_to_mouse()
                if closest[1] < Parameters.MAX_GRAB_RADIUS ** 2:
                    self.grabbed_particle = closest[0]
            if self.grabbed_particle is not None:
                mouse_pos = Vector2(*pg.mouse.get_pos())
                force = (mouse_pos - self.grabbed_particle.position) * Parameters.GRAB_STRENGTH
                self.grabbed_particle.force(force)
        else:
            self.grabbed_particle = None

    def closest_particle_to_mouse(self):
        """Finds the closest particle to the mouse cursor and returns a tuple containing it and the
        distance from the mouse to it, squared. This is used to avoid taking the square root, which
        is slow
        """
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
