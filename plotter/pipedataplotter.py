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

            # color line if both nodes are good.
            # if only one node drains, check code below
            target_color = 'gray'
            if current.can_drain and current.next_data is not None and current.next_data.can_drain:
                target_color = 'aqua'

            plt.plot(x1, y1, marker='o', color=target_color)

            current = current.next_data

        # color singular can_drain nodes
        current = pipe_data_head
        while current is not None:
            if current.can_drain:
                plt.scatter([current.x], [current.height], color='aqua', zorder=10)

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
