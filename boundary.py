from vector2 import Vector2

class Boundary:
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
        projection = self.get_projection(position)
        if not (0 < projection < 1):
            return False
        return -10 < self.normal.dot(position - self.p1) < 0

    def collision_point(self, position):
        """Finds the closest point on this boundary line to the given position"""
        position_vector = position - self.p1
        projection = position_vector.dot(self.vector) / self.vector.magnitude_squared()  # Calculate the projection of the position vector onto the line's direction vector
        closest_point = self.p1 + self.vector * projection
        return closest_point

    def __repr__(self):
        return f'Boundary({self.p1}, {self.p2})'
