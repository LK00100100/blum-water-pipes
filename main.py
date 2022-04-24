from waterpipes.pipedata import PipeData
from waterpipes.waterpipes import WaterPipes


def main():
    # TODO double check
    input_pipe_data = [
        PipeData(0, 6),
        PipeData(1, 9),
        PipeData(2, 4),
        PipeData(3, 5),
        PipeData(4, 3),
        PipeData(5, 7),
        PipeData(6, 0),
        PipeData(7, 4),
        PipeData(8, 2),
        PipeData(9, 10),
        PipeData(10, 8),
        PipeData(11, 11),
        PipeData(12, 0)
    ]

    output_point_head = WaterPipes.calc_drain_sections(input_pipe_data)

    # print linked list
    current = output_point_head
    while current is not None:
        print(current)
        current = current.next_data


if __name__ == '__main__':
    main()
