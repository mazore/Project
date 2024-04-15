from vector2 import Vector2

class Parameters:
    SIMULATION_WIDTH = 1000
    SIMULATION_HEIGHT = 800
    MAX_GRAB_RADIUS = 50
    GRAB_STRENGTH = 10
    FRAME_RATE = 24
    STEPS_PER_FRAME = 4
    TIME_DELTA = 1 / STEPS_PER_FRAME
    GRAVITY = Vector2(0, 2)  # Vector2(0, 9.8)
