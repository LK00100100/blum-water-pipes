from typing import List

from waterpipes.pipedata import PipeData


class WaterPipes:

    @staticmethod
    def calc_drain_sections(input_points: List[PipeData]):
        """
        Code is written simply without optimizations.
        :param input_points: Will be sorted by x. all x is unique or will raise error. ~100 points. will be sorted
        and linked to each other.
        :return: a list of "points with length beyond X" that will drain or not
        """

        WaterPipes.__check_input_points(input_points)

        WaterPipes.__sort_and_connect(input_points)

        # any peaks from the past that are overtaken. ordered by appearance. always decreasing height
        # important! past peaks should be overtaken in the future by a bigger peak. don't add overtaken peaks.
        past_points: List[PipeData] = []

        drain_points: List[PipeData] = WaterPipes.__get_drain_points(input_points)

        # TODO: will have to work with non-peaks later

        # process every point from left to right.
        for current_idx, current_point in enumerate(input_points):

            # peak check
            # TODO check for flat

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
                    new_point = past_point.next_data

                    new_point.calc_length_to_next()

                    if new_point.can_drain is None:
                        new_point.can_drain = False

                        if WaterPipes.__drain_point_exists(drain_points, past_point.x, current_point.x):
                            new_point.can_drain = True

                            # move can_drain upwards to the left (and flat areas)
                            temp_point = new_point.prev_data

                            while temp_point is not None:
                                if temp_point.height < temp_point.next_data.height:
                                    break

                                temp_point.can_drain = True
                                temp_point.calc_length_to_next()

                                temp_point = temp_point.prev_data

                # past point is equal or lower. current peak blocks it
                else:
                    if past_point.can_drain is None:
                        # does not drain
                        if not WaterPipes.__drain_point_exists(drain_points, past_point.x, current_point.x):
                            past_point.calc_length_to_next()
                            past_point.can_drain = False
                        else:
                            past_point.calc_length_to_next()
                            past_point.can_drain = True

                    # split right
                    if past_point != current_point.prev_data and past_point.height != current_point.height:
                        current_point.prev_data.split(past_point.height)

                        between_point = current_point.prev_data

                        between_point.calc_length_to_next()
                        between_point.can_drain = past_point.can_drain

                        between_point.prev_data.calc_length_to_next()
                        between_point.prev_data.can_drain = past_point.can_drain

                    # move can_drain upwards to the right (and flat areas)
                    if past_point.can_drain:
                        temp_point = past_point.next_data

                        while temp_point is not None:
                            if temp_point.next_data is None:
                                break

                            if temp_point.height > temp_point.next_data.height:
                                break

                            temp_point.can_drain = True
                            temp_point.calc_length_to_next()

                            temp_point = temp_point.next_data

                    del past_points[past_idx]

            past_points.append(current_point)

        # TODO flush past_points

        return input_points[0]

    # TODO can add more
    @staticmethod
    def __check_input_points(input_points: List[PipeData]):
        """

        :param input_points:
        :return: true if valid input. Otherwise, raise error
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
    def __is_peak(input_points: List[PipeData], idx):
        """
        is the point at input_points[idx] a peak?

        Peak if the points to the left and right or equal or lower.
        1,2,1. 2 is a peak.
        1,2,2. both 2s are peaks.
        :param input_points:
        :param idx:
        :return: True if peak. False otherwise
        """
        if len(input_points) <= 1:
            raise ValueError("not enough input_points")

        # first point
        if idx == 0:
            return input_points[idx].height >= input_points[idx + 1].height

        # last point
        if idx == len(input_points) - 1:
            return input_points[idx - 1].height <= input_points[idx].height

        # middle points
        return (input_points[idx - 1].height <= input_points[idx].height) and (
                input_points[idx].height >= input_points[idx + 1].height)

    @staticmethod
    def __get_drain_points(input_points: List[PipeData]):
        drain_points = []

        for point in input_points:
            if point.is_drain_point:
                drain_points.append(point)

        return drain_points

    @staticmethod
    def __drain_point_exists(drain_points: List[PipeData], x_left: float, x_right: float):
        """
        Checks to see if a drain point exists x_left and x_right (both inclusive)
        :param drain_points:
        :param x_left: inclusive
        :param x_right: inclusive
        :return:
        """
        for drain_point in drain_points:
            if x_left <= drain_point.x <= x_right:
                return True

        return False

    @staticmethod
    def __sort_and_connect(input_points: List[PipeData]):
        """
        Will sort then connect each point with each other.
        :param input_points: Will alter this
        :return: sorted and connected input_puts
        """
        input_points.sort(key=lambda pnt: pnt.x)

        for idx, current_point in enumerate(input_points):
            if idx > 0:
                current_point.prev_data = input_points[idx - 1]

            if idx < len(input_points) - 1:
                current_point.next_data = input_points[idx + 1]
