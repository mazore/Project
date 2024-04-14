from bodies import *
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)

if __name__ == '__main__':
    simulation = Simulation([
        # Square(
        #     screen_center.x * 3 / 2, screen_center.y, 200, 200,
        #     initial_impulse=Vector2(-5, -10)
        # ),
        # Square(
        #     screen_center.x, Parameters.SIMULATION_HEIGHT - 100, 200, 200
        # ),
        # BallSimple(
        #     screen_center.x / 2, screen_center.y, 100,
        #     initial_impulse=Vector2(20, -40)
        # ),
        Cloth(
            screen_center.x, screen_center.y, 10, 10, 30,
            stiffness=0.5, initial_impulse='randomized'
        ),
        # Rope(
        #     screen_center.x, screen_center.y / 2, 5, 70,
        #     initial_impulse=Vector2(5, 0)
        # )
        # BallComplex(
        #     screen_center.x / 2 + 200, screen_center.y / 2 + 200, 100,
        #     initial_impulse=Vector2(-35, -5)
        # )
    ])
    simulation.mainloop()
