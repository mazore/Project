"""Here we import all relevant scenes in this package and add them to a dictionary by name for easy use"""

from .simple_square import simple_square
from .simple_ball import simple_ball
from .complex_ball import complex_ball
from .squares import squares
from .square_and_ball import square_and_ball
from .simple_rope import simple_rope
from .cloth import cloth

scenes = {
    'simple_square': simple_square,
    'simple_ball': simple_ball,
    'complex_ball': complex_ball,
    'squares': squares,
    'square_and_ball': square_and_ball,
    'simple_rope': simple_rope,
    'cloth': cloth,
}
