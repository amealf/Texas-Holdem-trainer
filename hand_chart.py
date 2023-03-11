import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_range(open_range=[], call_range=[], bluff_range=[]):
    hands = ['AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s',
             'AKo', 'KK', 'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s',
             'AQo', 'KQo', 'QQ', 'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s',
             'AJo', 'KJo', 'QJo', 'JJ', 'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s',
             'ATo', 'KTo', 'QTo', 'JTo', 'TT', 'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s',
             'A9o', 'K9o', 'Q9o', 'J9o', 'T9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s',
             'A8o', 'K8o', 'Q8o', 'J8o', 'T8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s',
             'A7o', 'K7o', 'Q7o', 'J7o', 'T7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s',
             'A6o', 'K6o', 'Q6o', 'J6o', 'T6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s',
             'A5o', 'K5o', 'Q5o', 'J5o', 'T5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s',
             'A4o', 'K4o', 'Q4o', 'J4o', 'T4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s',
             'A3o', 'K3o', 'Q3o', 'J3o', 'T3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s',
             'A2o', 'K2o', 'Q2o', 'J2o', 'T2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22']
    hands_array = np.array(hands).reshape((13, 13))
    df = pd.DataFrame(hands_array)
    
    # Plot the DataFrame as a table
    # col_widths = [1/20] * len(df[0])
    
    fig1 = plt.figure('hands chart', figsize=(12, 8))
    fig1.set_figheight(10)
    fig1.set_figwidth(10)
    left = 0.04
    width = 0.94
    # bottom = 0.055
    bottom = 0.083
    height = 0.87
    rect_line = [left, bottom, width, height]  # below parameter
    ax0 = fig1.add_axes(rect_line)
    
    ax0.axis('off')
    ax0.axis('tight')
    table = ax0.table(
        cellText=df.values, cellLoc='center', loc='center')
    # Adjust the position of the table within the figure
    table.scale(1, 4)
    
    # set color
    for h1 in open_range:
        search_value = h1
        table_get_celld = table.get_celld()
        for row in range(len(hands_array)):
            for col in range(len(hands_array[0])):
                cell_value = table_get_celld[(row, col)].get_text().get_text()
                if cell_value == search_value:
                    # Found the search_value - print the row and column indices
                    cell = table[row,col]
                    cell.set_facecolor('red')
                    # print('Row index:', row)
                    # print('Column index:', col)
                    break
    for h2 in call_range:
        search_value_2 = h2
        table_get_celld = table.get_celld()
        for row in range(len(hands_array)):
            for col in range(len(hands_array[0])):
                cell_value = table_get_celld[(row, col)].get_text().get_text()
                if cell_value == search_value_2:
                    # Found the search_value_2 - print the row and column indices
                    cell = table[row,col]
                    cell.set_facecolor('lightgreen')
                    # print('Row index:', row)
                    # print('Column index:', col)
                    break

    for h3 in bluff_range:
        search_value_3 = h3
        table_get_celld = table.get_celld()
        for row in range(len(hands_array)):
            for col in range(len(hands_array[0])):
                cell_value = table_get_celld[(row, col)].get_text().get_text()
                if cell_value == search_value_3:
                    # Found the search_value_2 - print the row and column indices
                    cell = table[row,col]
                    cell.set_facecolor('blue')
                    # print('Row index:', row)
                    # print('Column index:', col)
                    break

    # Define a function to handle cell click events
    def on_cell_clicked(event):
        # Get the row and column index of the clicked cell
        row, col = event.ydata, event.xdata

        # Set the background color of the clicked cell to red
        cell = table.get_celld()[int(row), int(col)]
        cell.set_facecolor('red')

        # Redraw the table to show the updated color
        fig1.canvas.draw_idle()

    # Bind the on_cell_clicked function to the button_press_event of the figure
    fig1.canvas.mpl_connect('button_press_event', on_cell_clicked)
    
if __name__ == "__main__":
    show_range()


