from .ball_base import BallBase

class BallSimple(BallBase):
    def __init__(self, center_x, center_y, size, **kwargs):
        num_steps = 10
        stiffness_outer = 0.5
        stiffness_inner = 0.1
        skin_size = 50

        super().__init__(center_x, center_y, size, num_steps, stiffness_outer, stiffness_inner, skin_size, **kwargs)
