"""6.009 Lab 3 -- HyperMines"""

import sys
sys.setrecursionlimit(10000)
# NO ADDITIONAL IMPORTS

#A function that, given an N-D array, a tuple/list of coordinates, and a value, replaces the value at those coordinates in the array with the given value.
#A function that, given a list of dimensions and a value, creates a new N-D array with those dimensions, where each value in the array is initialized as the given value.
#A function that, given a game, returns the state of that game ('ongoing', 'defeat', or 'victory').
#A function that, given a list of dimensions and a tuple/list of coordinates, returns or yields all valid neighbors of the given coordinates.
#A function that, given a list of dimensions, returns or yields all possible coordinates in that dimensions.


class HyperMinesGame:
    def __init__(self, dimensions, bombs):
        """Start a new game.

        This method should properly initialize the "board", "mask",
        "dimensions", and "state" attributes.

        Args:
           dimensions (list): Dimensions of the board
           bombs (list): Bomb locations as a list of lists, each an
                         N-dimensional coordinate
        """ 
        self.dimensions = dimensions
        self.mask = self.make_board(dimensions, False)
        self.board = self.make_board(dimensions, 0)

        for bomb in bombs: # initialize bombs (will fail if dimensions > 2)
            self.set_coords(bomb, '.')

        for bomb in bombs:
            for neighbor in self.neighbors(bomb):
                neighbor_val = self.get_coords(neighbor)
                if neighbor_val != '.':
                    self.set_coords(neighbor, neighbor_val + 1)

        self.state = 'ongoing'


    def get_coords(self, coords):
        """Get the value of a square at the given coordinates on the board.

        (Optional) Implement this method to return the value of a square at the given
        coordinates.

        Args:
            coords (list): Coordinates of the square

        Returns:
            any: Value of the square
        """
        value = self.board
        for coord in coords:
            value = value[coord]

        return value

    def set_coords(self, coords, value):
        """Set the value of a square at the given coordinates on the board.

        (Optional) Implement this method to set the value of a square at the given
        coordinates.

        Args:
            coords (list): Coordinates of the square
        """
        subsec = self.board
        for coord in coords:
            if len(subsec) == 1:
                subsec[coord] = value
                break
            else:
                subsec = subsec[coord]

    def make_board(self, dimensions, elem):
        """Return a new game board

        (Optional) Implement this method to return a board of N-Dimensions.

        Args:
            dimensions (list): Dimensions of the board
            elem (any): Initial value of every square on the board

        Returns:
            list: N-Dimensional board
        """
        if len(dimensions) == 1:
            return [elem] * dimensions[0]
        return [make_board(self, dimensions[:-1]) for e in range(dimensions[-1])]

    def is_in_bounds(self, coords):
        """Return whether the coordinates are within bound

        (Optional) Implement this method to check boundaries for N-Dimensional boards.

        Args:
            coords (list): Coordinates of a square

        Returns:
            boolean: True if the coordinates are within bound and False otherwise
        """

        for c in range(len(coords)):
            if coords[c] < 0 and coords[c] > self.dimensions[c]:
                return False
        return True

    def neighbors(self, coords):
        """Return a list of the neighbors of a square

        (Optional) Implement this method to return the neighbors of an N-Dimensional square.

        Args:
            coords (list): List of coordinates for the square (integers)

        Returns:
            list: coordinates of neighbors
        """
        neighbors = []
        for c in range(len(coords)):
            new_n1 = coords.copy()
            new_n1[c] -= 1
            new_n2 = coords.copy()
            new_n2[c] += 1
            if is_in_bounds(self, new_n1):
                neighbors.append(new_n1)
            if is_in_bounds(self, new_n2):
                neighbors.append(new_n2)
        return neighbors

    def is_victory(self):
        """Returns whether there is a victory in the game.

        A victory occurs when all non-bomb squares have been revealed.
        (Optional) Implement this method to properly check for victory in an N-Dimensional board.

        Returns:
            boolean: True if there is a victory and False otherwise
        """


        for dim in self.dimensions:
            if self.get_coords() == '.' and self.mask[row][col]: # A bomb square has been revealed
                return False
            if self.board[row][col] != '.' and not self.mask[row][col]: # A non-bomb square is not yet revealed
                return False
        return True

    def dig(self, coords):
        """Recursively dig up square at coords and neighboring squares.

        Update the mask to reveal square at coords; then recursively reveal its
        neighbors, as long as coords does not contain and is not adjacent to a
        bomb.  Return a number indicating how many squares were revealed.  No
        action should be taken and 0 returned if the incoming state of the game
        is not "ongoing".

        The updated state is "defeat" when at least one bomb is visible on the
        board after digging, "victory" when all safe squares (squares that do
        not contain a bomb) and no bombs are visible, and "ongoing" otherwise.

        Args:
           coords (list): Where to start digging

        Returns:
           int: number of squares revealed
        """
        raise NotImplementedError


    def render(self, xray=False):
        """Prepare the game for display.

        Returns an N-dimensional array (nested lists) of "_" (hidden squares),
        "." (bombs), " " (empty squares), or "1", "2", etc. (squares
        neighboring bombs).  The mask indicates which squares should be
        visible.  If xray is True (the default is False), the mask is ignored
        and all cells are shown.

        Args:
           xray (bool): Whether to reveal all tiles or just the ones allowed by
                        the mask

        Returns:
           An n-dimensional array (nested lists)
        """
        if xray:


        return self.board

    # ***Methods below this point are for testing and debugging purposes only. Do not modify anything here!***

    def dump(self):
        """Print a human-readable representation of this game."""
        lines = ["dimensions: %s" % (self.dimensions, ),
                 "board: %s" % ("\n       ".join(map(str, self.board)), ),
                 "mask:  %s" % ("\n       ".join(map(str, self.mask)), ),
                 "state: %s" % (self.state, )]
        print("\n".join(lines))

    @classmethod
    def from_dict(cls, d):
        """Create a new instance of the class with attributes initialized to
        match those in the given dictionary."""
        game = cls.__new__(cls)
        for i in ('dimensions', 'board', 'state', 'mask'):
            setattr(game, i, d[i])
        return game
