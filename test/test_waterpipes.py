from unittest import TestCase

from plotter.pipedataplotter import PipeDataPlotter
from waterpipes.pipedata import PipeData
from waterpipes.waterpipes import WaterPipes


class TestWaterPipes(TestCase):
    def test_calc_drain_sections(self):
        input_pipe_data = [
            PipeData(0, 0),
            PipeData(1, 6),
            PipeData(2, 4),
            PipeData(3, 1),
            PipeData(4, 0, 0, True),
            PipeData(5, 3),
            PipeData(6, 0),
            PipeData(7, 2),
            PipeData(8, 5),
        ]

        output_point_head = WaterPipes.calc_drain_sections(input_pipe_data)

        # print linked list
        current = output_point_head
        while current is not None:
            print(current)
            current = current.next_data

        PipeDataPlotter.plot_pipe_data_head(output_point_head)

    def test_calc_drain_sections_2(self):
        input_pipe_data = [
            PipeData(0, 0),
            PipeData(1, 6),
            PipeData(2, 4),
            PipeData(3, 1),
            PipeData(4, 0, 0, True),
            PipeData(5, 3),
            PipeData(6, 4),
            PipeData(7, 2),
            PipeData(8, 5),
        ]

        output_point_head = WaterPipes.calc_drain_sections(input_pipe_data)

        # print linked list
        current = output_point_head
        while current is not None:
            print(current)
            current = current.next_data

        PipeDataPlotter.plot_pipe_data_head(output_point_head)

# test with decimals.
# test end points
# test with more flat areas
# test with points that are between peaks and ditches.
# test flat peaks with drainage.
