from bodies import *
from parameters import Parameters
import random
import pygame as pg
from simulation import Simulation
from vector2 import Vector2

screen_center = Vector2(Parameters.SIMULATION_WIDTH / 2, Parameters.SIMULATION_HEIGHT / 2)


def main():
    print_menu()
    option = input()
    while option not in [str(i+1) for i in range(8)]:
        print('Invalid option. Please select a valid option.')
        print_menu()
        option = input()

    simulation = [
        get_simulation_simple_square,
        get_simulation_simple_ball,
        get_simulation_more_complex_ball,
        get_simulation_square_and_ball_collisions,
        get_simulation_simple_rope,
        get_simulation_rope_and_balls_collisions,
        get_simulation_cloth,
    ][int(option) - 1]()

    simulation.mainloop()


def print_menu():
    print('\n\n========== Soft Body Simulation ==========')
    print('Select an option:')
    print('1: Simple square')
    print('2: Simple ball')
    print('3: More complex ball')
    print('4: Square and ball collisions')
    print('5: Simple rope')
    print('6: Rope and balls collisions')
    print('7: Cloth')
    print('8: Sandbox\n')


def get_simulation_simple_square():
    return Simulation([
        Square(
            screen_center.x, screen_center.y / 2, 200, 200,
            initial_impulse=Vector2(-random.uniform(-10, 10), -10),
            stiffness=0.03
        ),
    ], steps_per_frame=8)

def get_simulation_simple_ball():
    return Simulation([
        BallSimple(
            screen_center.x / 2, screen_center.y, 100,
            initial_impulse=Vector2(50, -30)
        ),
    ], steps_per_frame=10)

def get_simulation_more_complex_ball():
    return Simulation([
        BallComplex(
            screen_center.x / 2, screen_center.y / 2, 100,
            initial_impulse=Vector2(0, 0), bounciness=1, stiffness=0.25, mass=15
        ),
    ], steps_per_frame=18)

def get_simulation_square_and_ball_collisions():
    return Simulation([
        # BallComplex(
        #     screen_center.x / 2, screen_center.y + 100, 100,
        #     initial_impulse=Vector2(100, -40)
        # ),
        BallSimple(
            screen_center.x / 2, screen_center.y + 100, 100,
            initial_impulse=Vector2(20, -10)
        ),
        Square(
            screen_center.x, Parameters.SIMULATION_HEIGHT - 100, 200, 200
        ),
    ], steps_per_frame=14)

def get_simulation_simple_rope():
    return Simulation([
        Rope(screen_center.x, screen_center.y / 2, 10, 40, stiffness=0.1, initial_impulse=Vector2(10, 0))
    ], steps_per_frame=10)

def get_simulation_rope_and_balls_collisions():
    return Simulation([
        Rope(screen_center.x, screen_center.y / 2, 10, 40, initial_impulse=Vector2(10, 0)),
        BallSimple(screen_center.x / 2, screen_center.y / 2, 100, initial_impulse=Vector2(10, 0)),
    ], steps_per_frame=10)

def get_simulation_cloth():
    return Simulation([
        Cloth(
            screen_center.x, screen_center.y, 10, 10, 30,
            initial_impulse='randomized'
        ),
    ], steps_per_frame=2)

if __name__ == '__main__':
    main()
