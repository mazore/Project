from .ball_base import BallBase

class BallComplex(BallBase):
    def __init__(self, center_x, center_y, size, stiffness=1, **kwargs):
        num_steps = 30
        stiffness_outer = 0.9 * stiffness
        stiffness_inner = 0.1 * stiffness
        skin_size = 10

        super().__init__(center_x, center_y, size, num_steps, stiffness_outer, stiffness_inner, skin_size, **kwargs)
