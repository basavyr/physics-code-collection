import matplotlib.pyplot as plt
import os


class Plotter:
    """
    - Tool for making graphical representation of a data set
    """

    def __init__(self, x_data: list[float], y_data: list[float]) -> None:
        self.x_data = x_data
        self.y_data = y_data
        self.save_file_dir = f'../data/'
        os.makedirs(self.save_file_dir, exist_ok=True)

    def make_plot(self, plot_name: str, x_label: str, y_label: str, plot_label: str) -> None:
        """
        - Use pyplot to create and export a graphical representation of the input data
        """
        plt.plot(self.x_data, self.y_data, '-r', label=plot_label)
        plt.legend(loc='best')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        # plt.ylim(-200, 300)
        plt.savefig(f'{self.save_file_dir}{plot_name}.pdf',
                    dpi=300, bbox_inches='tight')
        plt.close()
