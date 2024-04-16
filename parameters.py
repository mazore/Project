from vector2 import Vector2

class Parameters:
    """Contains important settings for the simulation"""
    SIMULATION_WIDTH = 1000  # In pixels
    SIMULATION_HEIGHT = 800  # In pixels
    MAX_GRAB_RADIUS = 50  # How close the mouse has to be to a particle to grab it
    GRAB_STRENGTH = 10  # Multiplier of the force applied to a grabbed particle
    FRAME_RATE = 24  # Frames per second
    STEPS_PER_FRAME = 4  # Number of physics steps per frame
    TIME_DELTA = 1 / STEPS_PER_FRAME  # Time between physics steps
    GRAVITY = Vector2(0, 2)  # Vector2(0, 9.8)  # Acceleration due to gravity
