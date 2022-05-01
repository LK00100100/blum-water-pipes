from plotter.pipedataplotter import PipeDataPlotter
from waterpipes.pipedata import PipeData
from waterpipes.waterpipes import WaterPipes


def main():
    input_pipe_data = []

    print("Please input the file path...")
    file_path = input()

    with open(file_path, 'r') as file:
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


if __name__ == '__main__':
    main()
