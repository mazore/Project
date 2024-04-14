from vector2 import Vector2

class Parameters:
    SIMULATION_WIDTH = 1000
    SIMULATION_HEIGHT = 800
    FRAME_RATE = 30
    STEPS_PER_FRAME = 12
    TIME_DELTA = 1 / STEPS_PER_FRAME
    GRAVITY = Vector2(0, 2)  # Vector2(0, 9.8)
