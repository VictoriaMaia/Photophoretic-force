import matplotlib.pyplot as plt
import matplotlib as mpl

colors = ['g', 'r', 'b', 'c', 'm', 'y']


def plot_graphic_math(n, title, variable, results, z, y_lower_limit, y_upper_limit):
    plt.figure(figsize=[10, 5])
    for i in n:
        label_str = variable + '_' + str(i) + '(x)'
        plt.plot(z, results[i], colors[i], label=label_str)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(y_lower_limit, y_upper_limit)
    plt.legend(loc='best')
    plt.grid()
    plt.show()


def plot_graphic_real_and_imaginary_parts(title, label_input, color, results, z, y_lower_limit, y_upper_limit):
    plt.figure(figsize=[10, 5])
    plt.plot(z, results.real, color, label=label_input + ' (real)')
    plt.plot(z, results.imag, color+'-.', label=label_input + ' (imaginary)')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(y_lower_limit, y_upper_limit)
    plt.legend(loc='best')
    plt.grid()
    plt.show()


def plot_graphic_real_and_imaginary_parts_mpmath(title, label_input, color, results_real, results_imaginary, z,
                                                 y_lower_limit, y_upper_limit):
    plt.figure(figsize=[10, 5])
    plt.plot(z, results_real, color, label=label_input + ' (real)')
    plt.plot(z, results_imaginary, color+'-.', label=label_input + ' (imaginary)')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(y_lower_limit, y_upper_limit)
    plt.legend(loc='best')
    plt.grid()
    plt.show()


def plot_one_graphic(title, label_input, color, results, z, y_lower_limit, y_upper_limit, x_label='x', y_label='y'):
    plt.figure(figsize=[10, 5])
    plt.plot(z, results, color, label=label_input)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.ylim(y_lower_limit, y_upper_limit)
    plt.legend(loc='best')
    plt.grid()
    plt.show()


class ResultsGraphicAttributes:
    def __init__(self, results, color, x_loc_text=0, y_loc_text=0, message_text="", label="") -> None:
        self.results = results
        self.color = color
        self.label = label
        self.x_loc_text = x_loc_text
        self.y_loc_text = y_loc_text
        self.message_text = message_text
        pass


class GraphicAttributes:
    def __init__(self, image_size_x, image_size_y, x_label, y_label, title="",
                 y_lower_limit=0, y_upper_limit=0, x_lower_limit=0, x_upper_limit=0) -> None:
        self.image_size_x = image_size_x
        self.image_size_y = image_size_y
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.y_lower_limit = y_lower_limit
        self.y_upper_limit = y_upper_limit
        self.x_lower_limit = x_lower_limit
        self.x_upper_limit = x_upper_limit
        pass


def plot_graphic(results_to_plot,
                 graphic_info,
                 x_values,
                 latex=True,
                 y_limit=False,
                 x_limit=False,
                 text=False,
                 legend=False,
                 save_fig=False
                 ):

    if len(results_to_plot) == 0:
        print("Error. Don't have graphics to plot")
        return 

    for i in results_to_plot:
        if type(i) != ResultsGraphicAttributes:
            print("Error: parameters is not of type class ResultsGraphicAttributes. Type returned: ", type(results_to_plot))
            return 0
    
    if type(graphic_info) != GraphicAttributes:
        print("Error: parameters is not of type class GraphicAttributes. Type returned: ", type(graphic_info))
        return 0

    plt.figure(figsize=[graphic_info.image_size_x, graphic_info.image_size_y])
    mpl.rcParams["text.usetex"] = latex

    for i in results_to_plot:
        if i.label != "":
            plt.plot(x_values, i.results, i.color, label=i.label)
        else:
            plt.plot(x_values, i.results, i.color)
    
    plt.title(graphic_info.title)
    plt.xlabel(graphic_info.x_label)
    plt.ylabel(graphic_info.y_label)

    if legend:
        plt.legend(loc='best')
    
    if y_limit:
        plt.ylim(graphic_info.y_lower_limit, graphic_info.y_upper_limit)

    if x_limit:
        plt.xlim(graphic_info.x_lower_limit, graphic_info.x_upper_limit)

    if save_fig:
        plt.savefig(graphic_info.title+".png", format='png', dpi=500)
    
    if text:
        for i in results_to_plot:
            plt.text(i.x_loc_text, i.y_loc_text, i.message_text)

    plt.grid()
    plt.show()
