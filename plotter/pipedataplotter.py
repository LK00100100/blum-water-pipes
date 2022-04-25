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

            target_color = 'aqua' if current.can_drain else 'pink'

            plt.plot(x1, y1, marker='o', color=target_color)

            current = current.next_data

        # color drain nodes
        current = pipe_data_head
        while current is not None:
            if current.is_drain_point:
                plt.scatter([current.x], [current.height], color='mediumblue', zorder=10)

            current = current.next_data

        plt.xlabel("x")
        plt.ylabel("heights")
        plt.show()
