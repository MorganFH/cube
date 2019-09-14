from constants import SIDES, CORNERS, PIECETYPES


class Cube:
    """
    The actual cube object.
    Initialized with a size n, generating an nxnxn cube.
    The cube consists of 6 sides, represented by Side objects.
    """

    def __init__(self, size):
        # TODO: make a smarter, less redundant initialization that actually takes size into account
        self.sides = [Side(size, color) for color in SIDES.keys()]

        for a, b, c in CORNERS:
            a = self.sides[SIDES[a]]
            b = self.sides[SIDES[b]]
            c = self.sides[SIDES[c]]

            # Set corner pieces
            a.set_corner(CornerPiece([a, b, c]))

            # Set edge pieces
            a.set_edge(EdgePiece([a, b]))
            a.set_edge(EdgePiece([a, c]))
            b.set_edge(EdgePiece([b, c]))

    def __str__(self):
        return "\n".join(side.__str__() for side in self.sides)

    def turn_side(self, side, clockwise=True):
        # update the orientation for each edge and corner of the current side
        pass


class Side:
    """
    One side of the cube, identified by its center color.
    """

    def __init__(self, size, center_color):
        self.size = size  # TODO: actually use this
        self.center_color = center_color
        self.center = CenterPiece([self])
        self.edges = []
        self.corners = []

    def set_edge(self, edge):
        if self.is_piece_already_added(edge, self.edges):
            return
        self.edges.append(edge)
        for side in edge.sides:
            side.set_edge(edge)

    def set_corner(self, corner):
        if self.is_piece_already_added(corner, self.corners):
            return
        self.corners.append(corner)
        for side in corner.sides:
            side.set_corner(corner)

    # TODO: remove/modify this and initialize smarter
    def is_piece_already_added(self, piece, existing_pieces):
        for existing_piece in existing_pieces:
            if existing_piece.orientation == piece.orientation:
                return True
        return False

    def __repr__(self):
        return f"Side {self.center_color}"

    def __str__(self):
        return (
            f"\nSide {self.center_color}, with {len(self.edges)} edges and {len(self.corners)} corners\n"
            + str(self.center)
            + "\n"
            + "\n".join(str(edge) for edge in self.edges)
            + "\n"
            + "\n".join(str(corner) for corner in self.corners)
        )


class Piece:
    """
    One piece of the cube. 
    One of three different types: Center, edge or corner.
    """

    def __init__(self, _type, sides):
        self._type = _type
        self.sides = sides
        self.orientation = {
            side.center_color: side for side in sides
        }  # mapping from color to side object
        self.colors = [side.center_color for side in sides]


class CenterPiece(Piece):
    """
    A center piece, consisting of one color face.
    """

    def __init__(self, side):
        super().__init__(PIECETYPES["center"], side)

    def __str__(self):
        return f"Center: {self.colors[0]}"


class EdgePiece(Piece):
    """
    An edge piece, consisting of two color faces.
    """

    def __init__(self, sides):
        super().__init__(PIECETYPES["edge"], sides)

    def __str__(self):
        return f"Edge: {self.orientation}"


class CornerPiece(Piece):
    """
    A corner piece, consisting of three color faces.
    """

    def __init__(self, sides):
        super().__init__(PIECETYPES["corner"], sides)

    def __str__(self):
        return f"Corner: {self.orientation}"


if __name__ == "__main__":
    cube = Cube(3)
    print(cube)
