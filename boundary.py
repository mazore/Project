from vector2 import Vector2

class Boundary:
    """Represents a boundary that particles will not be able to cross. It is defined by two points
    in space, and the normal vector is calculated based on the direction vector between the two points.
    It's important that bodies are linked by constraints in a clockwise direction so the normal vector
    points outwards.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.vector = p2 - p1
        self.normal = Vector2(self.vector.y, -self.vector.x).normalized()

    def get_projection(self, position):
        """Calculate the projection of the position vector onto the line's direction vector"""
        position_vector = position - self.p1
        return position_vector.dot(self.vector) / self.vector.magnitude_squared()

    def should_collide(self, position):
        """Determines if the given position is in a location that warrents a collision."""
        projection = self.get_projection(position)
        if not (0 < projection < 1):
            return False  # If not within the bounds of the line segment
        return -10 < self.normal.dot(position - self.p1) < 0  # -10 is an arbitrary sort of width of the constraint

    def collision_point(self, position):
        """Finds the closest point on this boundary line to the given position"""
        position_vector = position - self.p1
        projection = position_vector.dot(self.vector) / self.vector.magnitude_squared()  # Calculate the projection of the position vector onto the line's direction vector
        closest_point = self.p1 + self.vector * projection
        return closest_point
