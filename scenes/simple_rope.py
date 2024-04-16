from bodies import Rope
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)


def simple_rope():
    return Simulation([
        Rope(screen_center.x, screen_center.y / 2, 10, 40, stiffness=0.1, initial_impulse=Vector2(10, 0)),
    ], steps_per_frame=10)
