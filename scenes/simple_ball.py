from bodies import BallSimple
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)


def simple_ball():
    return Simulation([
        BallSimple(
            screen_center.x / 2, screen_center.y, 100,
            initial_impulse=Vector2(50, -30)
        ),
    ], steps_per_frame=10)
