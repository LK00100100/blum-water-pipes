import unittest
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
            PipeData(4, 0, True),
            PipeData(5, 3),
            PipeData(6, 0),
            PipeData(7, 2),
            PipeData(8, 10),
            PipeData(9, 12),
        ]

        output_point_head = WaterPipes.calc_drain_sections(input_pipe_data)

        # print linked list
        current = output_point_head
        while current is not None:
            print(current)
            current = current.next_data

        # Assert
        expected_x_can_drain = [1, 2, 3, 4, 5, 7.125, 7.25, 7.5, 8, 9]
        current = output_point_head
        while current is not None:
            if current.x in expected_x_can_drain:
                self.assertTrue(current.can_drain, "current.x is supposed to drain: {}".format(current.x))

            current = current.next_data

        # PipeDataPlotter.plot_pipe_data_head(output_point_head)

    def test_calc_drain_sections_2(self):
        input_pipe_data = [
            PipeData(0, 0),
            PipeData(1, 6),
            PipeData(2, 4),
            PipeData(3, 1),
            PipeData(4, 0),
            PipeData(5, 3, True),
            PipeData(6, 4),
            PipeData(7, 4),
            PipeData(8, 4),
            PipeData(9, 10),
        ]

        output_point_head = WaterPipes.calc_drain_sections(input_pipe_data)

        # print linked list
        current = output_point_head
        while current is not None:
            print(current)
            current = current.next_data

        # Assert
        expected_x_can_drain = [1, 2, 5, 6, 7, 8]
        current = output_point_head
        while current is not None:
            if current.x in expected_x_can_drain:
                self.assertTrue(current.can_drain, "current.x is supposed to drain: {}".format(current.x))

            current = current.next_data

        # PipeDataPlotter.plot_pipe_data_head(output_point_head)

    @unittest.skip("Manual testing only")
    def test_calc_drain_file(self):

        input_pipe_data = []

        with open('./input_files/main_input.csv', 'r') as file:
            for line in file:
                if "x" in line:
                    continue

                x, height, can_drain = line.split(",")

                can_drain = True if str(can_drain).strip().lower() == 'true' else False

                data = PipeData(float(x), float(height), can_drain)
                input_pipe_data.append(data)

        output_point_head = WaterPipes.calc_drain_sections(input_pipe_data)

        # print linked list
        current = output_point_head
        while current is not None:
            print(current)
            current = current.next_data

        PipeDataPlotter.plot_pipe_data_head(output_point_head)
