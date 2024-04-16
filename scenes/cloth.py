from bodies import Cloth
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)


def cloth():
    return Simulation([
        Cloth(
            screen_center.x, screen_center.y, 10, 10, 30,
            initial_impulse='randomized'
        ),
    ], steps_per_frame=2)  # 2 steps per frame prevents cloth from being too stiff and overthinking. Particles should flow past each other well
