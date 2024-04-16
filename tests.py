"""We can create a test suite for the physics engine by running a few simulations and checking if
the outcomes are as expected. This is a simple way to ensure that everything is working as intended.
We check just the first particle of the first body, and as there's no randomness incorporated in these
examples, we accept it as a passed test only if it's within 10 pixels of the expected value.
"""

from bodies import *
from parameters import Parameters
from simulation import Simulation
from vector2 import Vector2


acceptance_threshold = 10
expected_outcomes = [
    Vector2(100, 800),
    Vector2(90.19171976088822, 43.924289256361085),
    Vector2(427.47302300818905, 13.710402284091483),
]


if __name__ == '__main__':
    # Test 1: Simple square
    simulation = Simulation([
        Square(200, 200, 200, 200, stiffness=1)
    ], steps_per_frame=8)
    for i in range(300):
        simulation.simulate()
    dist_from_expected = simulation.bodies[0].particles[0].position.distance(expected_outcomes[0])
    if dist_from_expected < acceptance_threshold:
        print('Test 1 passed')
    else:
        print('Test 1 failed, off by', dist_from_expected)

    # Test 2: Manipulating gravity with a simple ball
    simulation = Simulation([
        BallSimple(500, 200, 50)
    ], steps_per_frame=8)
    Parameters.GRAVITY = Vector2(0, -9.8)  # Manipulate gravity
    for i in range(500):
        simulation.simulate()
    dist_from_expected = simulation.bodies[0].particles[0].position.distance(expected_outcomes[1])
    if dist_from_expected < acceptance_threshold:
        print('Test 2 passed')
    else:
        print('Test 2 failed, off by', dist_from_expected)

    # Test 3: Two bodies colliding
    simulation = Simulation([
        BallSimple(500, 100, 50),
        BallSimple(500, 200, 50)
    ], steps_per_frame=8)
    for i in range(100):
        simulation.simulate()
    dist_from_expected = simulation.bodies[0].particles[0].position.distance(expected_outcomes[2])
    if dist_from_expected < acceptance_threshold:
        print('Test 3 passed')
    else:
        print('Test 3 failed, off by', dist_from_expected)
