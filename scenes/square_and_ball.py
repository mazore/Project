from bodies import BallSimple, Square
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)


def square_and_ball():
    return Simulation([
        BallSimple(
            screen_center.x / 2, screen_center.y + 100, 100,
            initial_impulse=Vector2(20, -15),
        ),
        Square(
            screen_center.x, Parameters.SIMULATION_HEIGHT - 100, 200, 200,
        ),
    ], steps_per_frame=14)
