import matplotlib.pyplot as plt
import os


class Plotter:
    """
    - Tool for making graphical representation of a data set
    """

    def __init__(self, x_data: list[float], y_data: list[list], spin_values: list[float]) -> None:
        self.x_data = x_data
        self.y_data = y_data
        self.spin_values = spin_values
        self.save_file_dir = f'../data/'
        os.makedirs(self.save_file_dir, exist_ok=True)

    def make_plot(self, plot_name: str, x_label: str, y_label: str, plot_label: str) -> None:
        """
        - Use pyplot to create and export a graphical representation of the input data
        - the y data is given as a list of tuples, where each tuple represents the potential V(q) evaluated for a list of spins
        """
        default_colors = ['-r', '-k', '-b', '-g']
        for idx in range(len(self.spin_values)):
            plt.plot(
                self.x_data, [x[idx] for x in self.y_data],
                default_colors[idx], label=f'I={self.spin_values[idx]}')
        plt.legend(loc='best')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(plot_label)
        plt.savefig(f'{self.save_file_dir}{plot_name}.pdf',
                    dpi=300, bbox_inches='tight')
        plt.close()

    @staticmethod
    def plot_data(x_data: list[float], y_data_list: list[list[float]], label_list: list[str], plot_name: str) -> None:
        """
        - create a graphical representation with several functions
        - uses a line plot style
        """
        iter_labels = iter(label_list)
        for y_data in y_data_list:
            plt.plot(x_data, y_data, '-r', label=f'{next(iter_labels)}')
        plt.legend(loc='best')
        plt.xlabel(r'x')
        plt.xlabel(r'f(x)')
        plt.savefig(f'../data/{plot_name}.pdf', dpi=450, bbox_inches='tight')
