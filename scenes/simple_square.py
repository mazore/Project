import random
from bodies import Square
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)


def simple_square():
    return Simulation([
        Square(
            screen_center.x, screen_center.y / 2, 200, 200,
            initial_impulse=Vector2(-random.uniform(-10, 10), -10),
            stiffness=0.03
        ),
    ], steps_per_frame=8)
