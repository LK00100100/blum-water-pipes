from waterpipes.pipedata import PipeData
from waterpipes.waterpipes import WaterPipes


def main():
    # TODO: just pass in a CSV through args

    input_pipe_data = []

    output_point_head = WaterPipes.calc_drain_sections(input_pipe_data)

    # print linked list
    current = output_point_head
    while current is not None:
        print(current)
        current = current.next_data


if __name__ == '__main__':
    main()
