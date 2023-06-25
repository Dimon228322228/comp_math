import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        fig, ax = plt.subplots()
        self.fig = fig
        self.canvas = ax

    def add_plot(self, x_data, y_data, color, label):
        self.canvas.plot(x_data, y_data, color=color, label=label)

    def add_green_plot(self, x_data, y_data, label):
        self.add_plot(x_data, y_data, "green", label)
        return self

    def add_red_plot(self, x_data, y_data, label):
        self.add_plot(x_data, y_data, "red", label)
        return self

    def add_blue_plot(self, x_data, y_data, label):
        self.add_plot(x_data, y_data, "blue", label)
        return self

    def add_init_black_data(self, x_data, y_data):
        self.canvas.scatter(x_data, y_data, edgecolors='black', label="Исходные данные")
        return self

    def set_graph_title(self, label):
        self.canvas.set_title(label)
        return self

    def set_x_axis(self, label):
        self.canvas.set_xlabel(label)
        return self

    def set_y_axis(self, label):
        self.canvas.set_ylabel(label)
        return self

    def show(self):
        self.canvas.legend()
        plt.show()
