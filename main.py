from bodies import *
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2

if __name__ == '__main__':
    square = Square(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2, 200, 200, initial_impulse=Vector2(0, -10))
    ball1 = BallSimple(Parameters.SIMULATION_WIDTH / 2 - 200, Parameters.SIMULATION_HEIGHT / 2, 100, initial_impulse=Vector2(37, -3))
    # ball2 = BallComplex(Parameters.SIMULATION_WIDTH / 2 + 200, Parameters.SIMULATION_HEIGHT / 2 + 200, 100, initial_impulse=Vector2(-35, -5))
    simulation = Simulation([square, ball1])
    simulation.mainloop()
