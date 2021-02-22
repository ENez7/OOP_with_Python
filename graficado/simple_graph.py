from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('simple_graph.html')
    fig = figure() # Figure creation for plotting
    
    total_vals = int(input('Qty.: '))
    x_vals = list(range(total_vals))
    y_vals = []
    
    for x in x_vals:
        val = int(input(f'Y-Value for {x}: '))
        y_vals.append(val)
        
    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)