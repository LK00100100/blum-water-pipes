from typing import List

from waterpipes.pipedata import PipeData


class WaterPipes:

    @staticmethod
    def calc_drain_sections(input_points: List[PipeData]):
        """
        Code is written simply without optimizations.
        Alters the input.
        If you want to optimize, try to cut down calculations.
        :param input_points: Will be sorted by x. All x is unique or will raise error. ~100 points. will be sorted
        and linked to each other.
        :return: The first pipe point.
        """
        WaterPipes._check_input_points(input_points)

        WaterPipes._sort_and_connect(input_points)

        input_head = WaterPipes._split_drain_sections(input_points)

        drain_points = WaterPipes._get_drain_points(input_head)

        # note: can optimize here. pass more information to stop early.
        for drain_point in drain_points:
            WaterPipes._calc_what_drains(drain_point)

        return input_head

    @staticmethod
    def _split_drain_sections(input_points: List[PipeData]):
        """
        Splits the pipes more so we have height-related subsections.
        In a ditch of points, every point to the left of the ditch will have a matching
        point to the right of the ditch.
        :param input_points:
        :return:
        """
        # ordered by appearance. always decreasing height
        # past peaks should be overtaken in the future by a bigger peak. don't add anything overtaken
        past_points: List[PipeData] = []

        # process every point from left to right.
        for current_idx, current_point in enumerate(input_points):
            # current point is decreasing, skip
            if current_point.prev_data is None or current_point.prev_data.height > current_point.height:
                past_points.append(current_point)
                continue

            # touch past points. remove past point blocked by a peak.
            for past_idx in range(len(past_points) - 1, -1, -1):

                past_point = past_points[past_idx]

                # past point is higher. (keep it)
                if past_point.height > current_point.height:

                    # past_point and the next_point is too high. ignore
                    if past_point.next_data.height >= current_point.height:
                        continue

                    # we need to add another point in-between past and next
                    # split left
                    past_point.split(current_point.height)

                # past point is equal or lower. current peak blocks it
                else:
                    # split right
                    if past_point != current_point.prev_data and past_point.height != current_point.height:
                        current_point.prev_data.split(past_point.height)

                    del past_points[past_idx]

            past_points.append(current_point)

        return input_points[0]

    @staticmethod
    def _check_input_points(input_points: List[PipeData]):
        """
        Validates for silly user inputs.
        Can put more here.
        :param input_points:
        :return: True, if valid input. Otherwise, raise error.
        """

        # check for duplicate x
        x_seen = set()
        for pipe in input_points:
            if pipe.x in x_seen:
                raise ValueError("multiple x val", pipe.x)

            x_seen.add(pipe.x)

        # check for enough input
        if len(input_points) <= 1:
            raise ValueError("need more than 1 input_points")

        return True

    @staticmethod
    def _get_drain_points(pipe_head: PipeData):
        """
        Get all drain points as a list.
        :param pipe_head: The first point (leftmost) of the pipeline.
        :return: A list of PipeData with drain points.
        """
        drain_points = []

        current = pipe_head
        while current is not None:
            if current.is_drain_point:
                drain_points.append(current)

            current = current.next_data

        return drain_points

    @staticmethod
    def _sort_and_connect(input_points: List[PipeData]):
        """
        Will sort then connect each point with each other.
        :param input_points: Alters data.
        :return: Sorted and connected input_puts.
        """
        input_points.sort(key=lambda pnt: pnt.x)

        for idx, current_point in enumerate(input_points):
            if idx > 0:
                current_point.prev_data = input_points[idx - 1]

            if idx < len(input_points) - 1:
                current_point.next_data = input_points[idx + 1]

    @staticmethod
    def _calc_what_drains(drain_point: PipeData):
        """
        This will mark everything to the left/right of this drain_point as can_drain.
        :param drain_point: A point with a drain.  Will raise error otherwise.
        :return:
        """
        if not drain_point.is_drain_point:
            raise ValueError("Point must be a drain.")

        # calc what drains to the left
        drain_height = drain_point.height

        current = drain_point
        while current is not None:
            if current.height >= drain_height:
                current.can_drain = True
                drain_height = current.height

            current = current.prev_data

        # calc what drains to the right
        drain_height = drain_point.height

        current = drain_point
        while current is not None:
            if current.height >= drain_height:
                current.can_drain = True
                drain_height = current.height

            current = current.next_data
