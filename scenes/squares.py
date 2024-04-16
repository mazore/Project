from bodies import Rope, Square
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)


colors = [
    '#00b894',
    '#0984e3',
    '#e84393',
    '#e17055',
]


def squares():
    return Simulation([
        Square(
            screen_center.x, Parameters.SIMULATION_HEIGHT - 100, 200, 200, stiffness=0.06, color=colors[0]
        ),
        Square(
            screen_center.x, screen_center.y, 100, 100, stiffness=0.03, color=colors[1]
        ),
        Square(
            screen_center.x / 2, screen_center.y, 200, 100, stiffness=0.2, color=colors[2]
        ),
        Square(
            screen_center.x * 3 / 2, screen_center.y, 100, 100, stiffness=0.1, color=colors[3]
        ),
    ], steps_per_frame=14)
