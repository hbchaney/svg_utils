import os
import re
import sys
from typing import Tuple, Optional

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

if __parent_dir__ not in sys.path:
    sys.path.insert(0, __parent_dir__)

from shape import Shape, Coordinate, Edge

class MatchDescription:
    """
    Helper struct for holdind match information while parsing an svg path.
    """
    def __init__(
            self,
            match_type: int,
            coords: Tuple[int, int],
            absolute: bool,
            end_index: int
        ) -> None:
        self.match_type = match_type
        self.coords = coords
        self.absolute = absolute
        self.end_index = end_index


class PathReader:
    """
    This object contains methods to parse a shape's path, as represented by
    a d tag in an svg file.
    """

    def __init__(self,name: str, path: str) -> None:
        self._name = name
        self._path = path
        self._parsing_path = path
        self._current_coord = Coordinate(0,0)
        self._is_parsed = False
        
        # TODO: will change to shape eventually
        self._shape = list()

    @property
    def is_parsed(self) -> bool:
        return self._is_parsed

    def to_shape(self) -> Shape:
        return Shape(_id=self._name, _edges=self._shape)

    def parse_path(self) -> None:
        while not self._is_parsed:
            self._is_parsed = True
            cases = [
                self._is_case_one,
                self._is_case_two,
                self._is_case_three,
            ]

            for case in cases:
                check, match_info = case(self._parsing_path)
                if check:
                    self._is_parsed = False
                    self._process_match_info(match_info)   

    def _is_case_one(
            self,
            path: str
            ) -> Tuple[bool, Optional[MatchDescription]]:
        """
        This method checks if the next direction in the path string is a move
        command.
        """
        pattern = r"[mM] ([\-0-9\.]+(|e\-[0-9]))\,([0-9\.\-]+(|e\-[0-9])) "
        match = re.match(pattern, path)
        if match is None:
            return False, None
        if match.start() != 0:
            return False, None
        
        absolute = (path[match.start()].upper() == path[match.start()])
        coords = path[2:match.end()-1]

        x_y = tuple(float(i) for i in coords.split(","))

        return True, MatchDescription(1, x_y, absolute, match.end())

    def _is_case_two(
            self,
            path: str
            ) -> Tuple[bool, Optional[MatchDescription]]:
        """
        This method returns True, and the corresponding re.Match, when the
        next direction is a vertical or horizontal line.
        """
        pattern = r"[vVhH] (([0-9-+\.]+)|([0-9\.]+e\-[0-9]+)) "
        match = re.match(pattern, path)
        if match is None:
            return False, None
        if match.start() != 0:
            return False, None
        
        absolute = (path[match.start()].upper() == path[match.start()])

        value = float(path[2:match.end()-1])
        
        if path[match.start()] in ["v","V"]:
            if absolute:
                x_y = (self._current_coord.x, value)
            else:
                x_y = (0, value)
        else:
            # horizontal
            if absolute:
                x_y = (value, self._current_coord.y)
            else:
                x_y = (value, 0)

        return True, MatchDescription(2, x_y, absolute, match.end())


    def _is_case_three(
        self,
            path: str
            ) -> Tuple[bool, Optional[MatchDescription]]:
        """
        This method returns True, and the corersponding re.Match, when the
        next direction is a genertic line.
        """
        pattern = r"[lL] ([\-0-9\.]+(|e\-[0-9]))\,([0-9\.\-]+(|e\-[0-9])) "
        match = re.match(pattern, path)
        if match is None:
            return False, None
        if match.start() != 0:
            return False, None
        
        absolute = (path[match.start()].upper() == path[match.start()])
        coords = path[2:match.end()-1]

        x_y = tuple(float(i) for i in coords.split(","))

        return True, MatchDescription(3, x_y, absolute, match.end())

    def _process_match_info(self, match_info: MatchDescription) -> None:
        if match_info.match_type == 1:
            if match_info.absolute:
                self._current_coord = Coordinate(
                    match_info.coords[0], match_info.coords[1]
                )
            else:
                self._current_coord = Coordinate(
                    self._current_coord.x + match_info.coords[0],
                    self._current_coord.y + match_info.coords[1]
                )        
        elif match_info.match_type in (2,3):
            if match_info.absolute:
                ending_coord = Coordinate(
                    match_info.coords[0],
                    match_info.coords[1]
                )
                
            else:
                ending_coord = Coordinate(
                    self._current_coord.x + match_info.coords[0],
                    self._current_coord.y + match_info.coords[1]
                )
            self._shape.append(
                Edge(self._current_coord, ending_coord)
            )
            self._current_coord = ending_coord
        self._parsing_path = self._parsing_path[match_info.end_index:]



if __name__ == '__main__':
    # path = "M 300,9.9999999 V 29.99981 h -4.99969 V 50.00014 H 300 v 9.99991 h -4.99969 v 4.99969 l 29.99972,5.2e-4 v 4.99969 h -29.99972 v 9.99991 H 300 v 25.00054 h 25.00003 v 4.9997 h 19.99981 v -4.9997 h 20.00033 v 4.9997 h 19.99981 v -4.9997 h 29.99972 v 4.9997 h 30.00024 v -4.9997 h 30.00023 v 4.9997 h 19.99982 v -4.9997 h 19.99981 v 4.9997 h 20.00033 v -4.9997 h 25.00002 V 79.99986 h 5.00021 v -9.99991 h -30.00023 v -5.00021 h 30.00023 v -4.99969 h -5.00021 v -9.99991 h 5.00021 V 29.99981 h -5.00021 V 9.9999999 Z M 344.99984,65.00026 h 20.00033 v 4.99969 h -20.00033 z m 40.00014,0 h 29.99972 v 4.99969 h -29.99972 z m 59.99996,0 h 30.00023 v 4.99969 h -30.00023 z m 50.00005,0 h 19.99981 v 4.99969 h -19.99981 z"

    # pr = PathReader(path)

    # pr.parse_path()
    pass