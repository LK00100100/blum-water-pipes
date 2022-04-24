import math
from typing import Union


class PipeData:
    """
    Plain object to hold Pipe Section data. Either points or lengths
    For pipe side profiles
    """

    x: float  # x location
    height: int  # y or height
    is_drain_point: bool  # if true, there is a drain here (optional)

    length: float  # length to next point (optional. defaults to 0)
    can_drain: Union[None, bool]  # True, if it can drain. Coupled with length of pipe

    # these should be ordered by x
    prev_data: Union[None, 'PipeData']
    next_data: Union[None, 'PipeData']

    # todo: can put where this will drain to.

    def __init__(self, x: float, height: int, length: int = 0, is_drain_point: bool = False):
        self.x = x
        self.height = height
        self.length = length
        self.is_drain_point = is_drain_point
        self.can_drain = None
        self.prev_data = None
        self.next_data = None

    def calc_length_to_next(self):
        if self.next_data is None:
            raise ValueError("no next point to calc")

        width = abs(self.x - self.next_data.x)
        height = abs(self.height - self.next_data.height)

        self.length = math.sqrt((width * width) + (height * height))

    def split(self, split_height: int):
        """
        if between current height and next height, split_height, will add a new node between current and next.
        current, in-between, and next will have their next_data adjusted.
        :param split_height:
        :return:
        """
        if self.next_data is None:
            raise ValueError("no next point to calc")

        if split_height >= self.height or split_height <= self.next_data.height:
            raise ValueError("split_height not in between self and next point")

        big_height = abs(self.height - self.next_data.height)
        big_width = abs(self.x - self.next_data.x)

        small_height = abs(self.height - split_height)
        small_width = (big_width * small_height) / big_height

        between_node = PipeData(self.x + small_width, split_height)

        if self.x < self.next_data.x:
            between_node.prev_data = self
            between_node.next_data = self.next_data
        elif self.x > self.next_data.x:
            raise ValueError("next point's x is smaller. should be bigger")
        else:
            raise ValueError("this and next point's x's are the same.")

        self.next_data.prev_data = between_node
        self.next_data = between_node

    def __repr__(self):
        is_drain_str = ""
        if self.is_drain_point:
            is_drain_str = ", is_drain"

        return 'PipeData(x={0}, height={1}, length={2}, can_drain={3}{4})'.format(round(self.x, 4), self.height,
                                                                                  self.length,
                                                                                  self.can_drain,
                                                                                  is_drain_str)
