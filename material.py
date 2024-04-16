class Material:
    """Material class for particles"""
    def __init__(self, friction, bounce, mass):
        self.friction = friction  # 0-1, how easily particles can slide on the ground
        self.bounce = bounce  # 0-1, how elastic particles act
        self.mass = mass  # 0 for fixed point, higher means that forces will have less impact
