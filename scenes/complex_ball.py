from bodies import BallComplex
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)


def complex_ball():
    return Simulation([
        BallComplex(
            screen_center.x / 2, screen_center.y / 2, 100,
            initial_impulse=Vector2(0, 0), bounciness=1, stiffness=0.25, mass=15
        ),
    ], steps_per_frame=18)
