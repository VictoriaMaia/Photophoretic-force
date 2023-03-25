import matplotlib.pyplot as plt
import matplotlib as mpl

colors = ['g', 'r', 'b', 'k', 'c', 'm', 'y']
line = ['','-.','--','.', '*']

def plot_graphic(results_to_plot,
                 x_values,
                 x_label,
                 y_label,
                 legend,
                 image_size_x = 7,
                 image_size_y = 5,
                 font_size = 15,
                 ):

    plt.figure(figsize=[image_size_x, image_size_y])

    aux_color = 0
    aux_line = 0

    for i in range(len(results_to_plot)):
        if aux_color == len(colors): aux_color = 0
        if aux_line == len(line): aux_line = 0
        color_line = colors[aux_color]+line[aux_line]
        
        plt.plot(x_values, results_to_plot[i], color_line, label=legend[i])

        aux_color = aux_color+1
        aux_line = aux_line+1
        
    
    mpl.rcParams['font.size'] = font_size
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='best')
    plt.grid()
    plt.show()
        