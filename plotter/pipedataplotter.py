import matplotlib.pyplot as plt

from waterpipes.pipedata import PipeData


class PipeDataPlotter:
    """
    Plots for PipeData and various metadata
    """

    @staticmethod
    def plot_pipe_data_head(pipe_data_head: PipeData):
        current = pipe_data_head

        while current is not None:
            next_node = current.next_data

            if next_node is None:
                break

            x1, y1 = [current.x, next_node.x], [current.height, next_node.height]

            target_color = 'blue' if current.can_drain else 'red'

            plt.plot(x1, y1, marker='o', color=target_color)

            current = current.next_data

        plt.xlabel("x")
        plt.ylabel("heights")
        plt.show()
