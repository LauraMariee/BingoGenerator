import typing

from number import Number


class Card:
    """
    A bingo card of size nxm.

    Numbers can be put on the card, however it is possible to leave fields blank.
    Numbers that have been called out can be crossed out.
    A card can be checked for a winning combination.
    """

    width: int 
    height: int
    numbers: typing.List[typing.Optional[Number]]
    marked: typing.List[bool]

    def __init__(self, height=3, width=9):
        """
        Creates a new bingo card with the given dimensions.

        Different bingo places tend to use different bingo cards. 
        In the united kingdom, 9x3 bing cards seem to be popular, which is
        the default for this class. (See: https://en.wikipedia.org/wiki/Bingo_(British_version))

        Initially, all fields on the card will be blank.
        """
        self.width = width
        self.height = height
        nr_fields = width * height 
        self.numbers = [None] * nr_fields
        self.marked = [False] * nr_fields

    def _get_index(self, row: int, col: int):
        """
        Calculates the index, at which the field at the given row and column
        is stored in the self.numbers array.
        """

        # Check that row and col are within the valid bounds
        # Otherwise, this method would probably return some unexpected result.
        if row < 0:
            raise ValueError("The row must be positive.")
        if col < 0:
            raise ValueError("The column must be positive.")
        if row >= self.height:
            raise ValueError(f"The row index ({row}) is too large. " 
                             f"This bingo card has {self.height} rows, "
                             f"so the row must be between 0 and {self.height - 1}.")
        if col >= self.width:
            raise ValueError(f"The column index ({col}) is too large. " 
                             f"This bingo card has {self.width} columns, "
                             f"so the column must be between 0 and {self.width - 1}.")

        # calculate the index
        # the numbers are stored row-wise in self.numbers.
        # For example, a 3 by 2 bingo card like this:
        #
        # +---+---+---+
        # | A | B | C |
        # +---+---+---+
        # | X | Y | Z |
        # +---+---+---+
        #
        # would be stored like this:
        # 
        # self.numbers = [
        #     A, B, C,
        #     D, E, F,
        # ]
        # 
        # So that the elements of the first row are stored at
        # indices 0 to 2
        # And the elements of the second row are stored 
        # at the indices 3 to 5
        index = row * self.width + col
        return index

    def get_number(self, row: int, col: int) -> typing.Optional[Number]:
        """
        Returns the number on the bingo card at the field at the given 
        row and column. The result will be None, if this field is blank.
        """
        index = self._get_index(row, col)
        return self.numbers[index]

    def put_number(self, row: int, col: int, number: Number):
        """
        Writes the given number into the field at 
        the given row/column on the bingo card. 
        """ 
        index = self._get_index(row, col)
        self.numbers[index] = number

    def is_blank(self, row: int, col: int) -> bool:
        """
        Checks, if the field at the given 
        row/column contains a number or not.
        The field contains a number -> return False
        The field does not contain a number -> return True
        """
        index = self._get_index(row, col)
        return self.numbers[index] is None

    def is_marked(self, row: int, col: int) -> bool:
        """
        Checks if the given field is crossed out.
        Usually, a field gets crossed out, when the game master calls
        out the number of that field.
        """
        index = self._get_index(row, col)
        return self.marked[index]

    def mark_number(self, called_number: Number):
        """
        After a number has been called out by the game master,
        this method marks that number on the bingo card.
        """
        for index, number in enumerate(self.numbers):
            if number is not None and number.number == called_number.number:
                self.marked[index] = True

    def pretty_print(self):
        """
        Pretty-prints this bingo card.
        This is quite useful for debugging.
        """
        line_seperator = "+" + "----+" * self.width
        print(line_seperator)
        for row in range(self.height):
            line = "|"
            for col in range(self.width):
                if self.is_marked(row, col):
                    space = "#"
                else:
                    space = " "
                field = self.get_number(row, col)
                if field is None:
                    nr = space * 2
                elif field.number < 10:
                    nr = space + str(field.number)
                else:
                    nr = str(field.number)
                line += space + nr + space + "|"
            print(line)
            print(line_seperator)

    def check(self) -> bool:
        """
        Checks, if this bingo card has a "bingo" pattern.

        There seem to be different winning patterns based on which rules you are playing with.
        The wikipedia article lists a few common examples:
        https://en.wikipedia.org/wiki/Bingo_(British_version)#Gameplay
        """
        return self._check_line_pattern() or \
            self._check_four_corners_pattern() or \
            self._check_full_house_pattern() or \
            self._check_two_lines_pattern()

    def _check_line_pattern(self) -> bool:
        """
        Checks for the line pattern described here:
        https://en.wikipedia.org/wiki/Bingo_(British_version)#Gameplay
        """

        # this only makes sense if the bingo card has at least a width of 5
        if self.width < 5:
            return False

        # Check for the pattern in each row
        for row in range(self.height):

            # search for 5 consecutive crossed-out numbers
            nr_marked = 0
            for col in range(self.width):
                if self.is_marked(row, col):
                    nr_marked += 1
                else:
                    nr_marked = 0

                if nr_marked >= 5:
                    return True

        # if we did not find anything, then this is not a win :-(
        return False

    def _check_four_corners_pattern(self) -> bool:
        # Checks for the four-corner-pattern described here:
        # https://en.wikipedia.org/wiki/Bingo_(British_version)#Gameplay
        # TODO
        return False

    def _check_full_house_pattern(self) -> bool:
        # Checks for the full-house-pattern described here:
        # https://en.wikipedia.org/wiki/Bingo_(British_version)#Gameplay
        # TODO
        return False

    def _check_two_lines_pattern(self) -> bool:
        # Checks for the two-lines-pattern described here:
        # https://en.wikipedia.org/wiki/Bingo_(British_version)#Gameplay
        # TODO
        return False
