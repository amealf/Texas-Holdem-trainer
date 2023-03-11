import random
import tkinter as tk
import pandas as pd
import os
# import matplotlib.pyplot as plt
import hand_chart
# from sys import exit
training_data = []
mistake_record = []


# 全范围
# train_range = ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22',
#                   'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s',
#                   'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s',
#                   'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s',
#                   'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s',
#                   'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s',
#                   '98s', '97s', '96s', '95s', '94s', '93s', '92s',
#                   '87s', '86s', '85s', '84s', '83s', '82s',
#                   '76s', '75s', '74s', '73s', '72s',
#                   '65s', '64s', '63s', '62s',
#                   '54s', '53s', '52s',
#                   '43s', '42s',
#                   '32s',
#                   'AKo', 'AQo', 'AJo', 'ATo', 'A9o', 'A8o', 'A7o', 'A6o', 'A5o', 'A4o', 'A3o', 'A2o',
#                   'KQo', 'KJo', 'KTo', 'K9o', 'K8o', 'K7o', 'K6o', 'K5o', 'K4o', 'K3o', 'K2o',
#                   'QJo', 'QTo', 'Q9o', 'Q8o', 'Q7o', 'Q6o', 'Q5o', 'Q4o', 'Q3o', 'Q2o',
#                   'JTo', 'J9o', 'J8o', 'J7o', 'J6o', 'J5o', 'J4o', 'J3o', 'J2o',
#                   'T9o', 'T8o', 'T7o', 'T6o', 'T5o', 'T4o', 'T3o', 'T2o',
#                   '98o', '97o', '96o', '95o', '94o', '93o', '92o',
#                   '87o', '86o', '85o', '84o', '83o', '82o',
#                   '76o', '75o', '74o', '73o', '72o',
#                   '65o', '64o','63o', '62o',
#                   '54o', '53o', '52o',
#                   '43o', '42o',
#                   '32o']

# 自定范围
train_range = ['AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s',
             'AKo', 'KK', 'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s',
             'AQo', 'KQo', 'QQ', 'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s',
             'AJo', 'KJo', 'QJo', 'JJ', 'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s',
             'ATo', 'KTo', 'QTo', 'JTo', 'TT', 'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s',
             'A                         9o', 'K9o', 'Q9o', 'J9o', 'T9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s',
             'A8o', 'K8o', 'Q8o', 'J8o', 'T8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s',
             'A7o', 'K7o', 'Q7o', 'J7o', 'T7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s',
             'A6o', 'K6o', 'Q6o', 'J6o', 'T6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s',
             'A5o', 'K5o', 'Q5o', 'J5o', 'T5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s',
             'A4o', 'K4o', 'Q4o', 'J4o', 'T4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s',
             'A3o', 'K3o', 'Q3o', 'J3o', 'T3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s',
             'A2o', 'K2o', 'Q2o', 'J2o', 'T2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22']

deck = ['2s', '2h', '2c', '2d', '3s', '3h', '3c', '3d', '4s', '4h', '4c', '4d',
        '5s', '5h', '5c', '5d', '6s', '6h', '6c', '6d', '7s', '7h', '7c', '7d',
        '8s', '8h', '8c', '8d', '9s', '9h', '9c', '9d', 'Ts', 'Th', 'Tc', 'Td',
        'Js', 'Jh', 'Jc', 'Jd', 'Qs', 'Qh', 'Qc', 'Qd', 'Ks', 'Kh', 'Kc', 'Kd',
        'As', 'Ah', 'Ac', 'Ad']

# positions_list  = ["UTG", "UTG+1", "UTG+2", "LJ", "HJ", "CO", "BTN", "SB", "BB"]
positions_list  = ["UTG", "UTG+1", "UTG+2", "LJ", "HJ", "CO", "BTN", "SB"]

range_list = [] 
call_list = []
UTG_list = ['66', '77', '88', '99', 'AQo', 'AKo', 'AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A5s', 'KK', 'QQ', 'JJ', 'TT', 'KTs', 'QTs', 'JTs', '98s', 'T9s', 'QJs', 'KJs', 'KQs']
UTG1_list = ['66', '77', '88', '99', 'AQo', 'AKo', 'AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A5s', 'KK', 'QQ', 'JJ', 'TT', 'KTs', 'QTs', 'JTs', '98s', 'T9s', 'QJs', 'KJs', 'KQs', 'K9s', 'Q9s', 'J9s', 'AJo', 'KQo', 'A4s', 'A6s', 'A7s', 'A8s', '87s']
UTG2_list = ["55", "66", "77", "88", "99", "AQo", "AKo", "AA", "AKs", "AQs", "AJs", "ATs", "A9s", "A5s", "KK", "QQ", "JJ", "TT", "KTs", "QTs", "JTs", "87s", "98s", "T9s", "QJs", "KJs", "KQs", "K9s", "Q9s", "J9s", "AJo", "KQo", "A4s", "A6s", "A7s", "A8s", "76s", "A3s", "A2s"]
LJ_list = ['44', '55', '66', '77', '88', '99', 'AQo', 'AKo', 'AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A5s', 'KK', 'QQ', 'JJ', 'TT', 'KTs', 'QTs', 'JTs', '87s', '98s', 'T9s', 'QJs', 'KJs', 'KQs', 'K9s', 'Q9s', 'J9s', 'AJo', 'KQo', 'A4s', 'A6s', 'A7s', 'A8s', '76s', 'KJo', 'ATo', '65s', 'A3s', 'A2s']
HJ_list = ['22', '33', '44', '55', '66', '77', '88', '99', 'AQo', 'AKo', 'AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A5s', 'KK', 'QQ', 'JJ', 'TT', 'KTs', 'QTs', 'JTs', '87s', '98s', 'T9s', 'QJs', 'KJs', 'KQs', 'K9s', 'Q9s', 'J9s', 'AJo', 'KQo', 'A4s', 'A6s', 'A7s', 'A8s', '76s', 'KJo', 'ATo', '65s', 'QJo', 'K8s', 'T8s', '97s', '54s', 'A3s', 'A2s']
CO_list = ['43s', '22', '33', '44', '55', '66', '77', '88', '99', 'AQo', 'AKo', 'AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A5s', 'KK', 'QQ', 'JJ', 'TT', 'KTs', 'QTs', 'JTs', '87s', '98s', 'T9s', 'QJs', 'KJs', 'KQs', 'K9s', 'Q9s', 'J9s', 'AJo', 'KQo', 'A4s', 'A6s', 'A7s', 'A8s', '76s', 'KJo', 'ATo', '65s', 'QJo', 'K8s', 'T8s', '97s', '54s', 'A3s', 'A2s', 'K7s', 'A9o', 'KTo', 'QTo', 'JTo', '64s', '75s', '86s', 'Q8s', 'J8s']
BTN_list = ["32s", "22", "33", "44", "55", "66", "77", "88", "99", "AQo", "AKo", "AA", "AKs", "AQs", "AJs", "ATs", "A9s", "A5s", "KK", "QQ", "JJ", "TT", "KTs", "QTs", "JTs", "87s", "98s", "T9s", "QJs", "KJs", "KQs", "K9s", "Q9s", "J9s", "AJo", "KQo", "A4s", "A6s", "A7s", "A8s", "76s", "KJo", "ATo", "65s", "QJo", "K8s", "T8s", "97s", "54s", "A3s", "A2s", "K7s", "A9o", "KTo", "QTo", "JTo", "64s", "75s", "86s", "Q8s", "J8s", "K2s", "K6s", "K5s", "K4s", "K3s", "Q7s", "Q6s", "Q5s", "Q4s", "Q3s", "Q2s", "J6s", "T6s", "96s", "J7s", "T7s", "74s", "85s", "53s", "43s", "K9o", "K8o", "K7o", "98o", "T8o", "J8o", "Q8o", "Q9o", "J9o", "T9o", "A8o", "A7o", "A6o", "A5o", "A4o", "A3o", "A2o", "97o", "87o", "76o"]
SB_bet_list = ['88', '99', 'AKs', 'AQs', 'AJs', 'ATs', 'KQs', 'KJs', 'QJs', 'QQ', 'KQo', 'AQo', 'AJo', 'KJo', 'ATo', 'TT', 'JJ', 'J6o', 'T6o', '96o', '86o', 'Q5o', 'Q4o', 'Q3o', 'Q2o', 'K3o', 'K2o', 'J2s', 'J3s', 'J4s', 'T4s', '94s', '84s', '74s', '85s', '95s', 'T5s', '63s', '53s', '43s']
SB_call_list = ['22', '33', '44', '55', '66', '77', 'AA', 'AKo', 'KK', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s', 'K2s', 'Q2s', 'Q3s', 'K3s', 'K4s', 'K5s', 'K6s', 'K7s', 'K8s', 'K9s', 'KTs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'J5s', 'J6s', 'J7s', 'J8s', 'J9s', 'JTs', 'T9s', '98s', '87s', '76s', '65s', '54s', '64s', '75s', '86s', '96s', 'T6s', 'T7s', 'T8s', '97s', '32s', '65o', '76o', '87o', '97o', 'T7o', 'J7o', 'Q7o', 'K7o', 'A8o', 'A9o', 'KTo', 'QJo', 'JTo', 'T9o', '98o', 'T8o', 'J8o', 'Q8o', 'K8o', 'K9o', 'Q9o', 'J9o', 'QTo', 'A7o', 'A6o', 'A5o', 'A4o', 'A3o', 'A2o', 'K4o', 'K5o', 'K6o', 'Q6o']

train_range = SB_bet_list+SB_call_list  # 用SB的范围，排除最弱的牌


def get_position():
    root = tk.Tk()
    root.geometry("400x800")
    root.title("Select Position")
    
    ## center the window on the screen
    # window_width = root.winfo_reqwidth()
    # window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth() / 5)
    position_down = int(root.winfo_screenheight() / 5)
    root.geometry("+{}+{}".format(position_right, position_down))

    label = tk.Label(root, text="Select your position:")
    label.pack(pady=10)

    # create a list of buttons to select the position
    buttons = []
    for p in positions_list:
        button = tk.Button(
            root, text=p, command=lambda position=p: set_position(position))
        button.pack(pady=5)
        buttons.append(button)


    # create a function to set the selected position
    def set_position(position):
        nonlocal selected_position
        selected_position = position
        root.destroy()

    # create a button to cancel the selection
    cancel_button = tk.Button(root, text="Cancel", command=root.destroy)
    cancel_button.pack(pady=10)

    # set the default selected position to None
    selected_position = None
    root.mainloop()
    
    print('Selected position: ' + selected_position)
    # return the selected position
    return selected_position

# def exit_program(root, selection):
#     root.destroy()
#     print(f"Selected position: {selection}")

def exit_program(root, selection):
    root.destroy()
    print(f"Selected position: {selection}")

# Select position
if __name__ == "__main__":
    # position = get_position()  # 自选位置
    position = random.choice(positions_list)  # 随机位置
    if position == 'UTG':
        range_list = UTG_list
    elif position == 'UTG+1':
        range_list = UTG1_list
    elif position == 'UTG+2':
        range_list = UTG2_list
    elif position == 'LJ':
        range_list = LJ_list
    elif position == 'HJ':
        range_list = HJ_list
    elif position == 'CO':
        range_list = CO_list
    elif position == 'BTN':
        range_list = BTN_list
    elif position == 'SB':
        range_list = SB_bet_list
        call_list = SB_call_list
    # elif position == 'BB':
    #     range_list = BB_list
    
# Create a function that randomly selects two cards from the deck to create a starting hand
# def select_hand():
#     hand = random.sample(train_range, 1)
#     return ''.join(hand)

def get_action_popup():
    hand = random.choice(train_range)
    root = tk.Tk()
    root.geometry("700x900")
    root.title("Preflop Training")

    # center the window on the screen
    position_right = int(root.winfo_screenwidth() / 5)
    position_down = int(root.winfo_screenheight() / 5)
    root.geometry("+{}+{}".format(position_right, position_down))

    # create the label and buttons as before
    label = tk.Label(
        root,
        text=f"What is your action for {hand} in {position}?",
        font=('Arial', 12),
        padx=30,pady=30)
    # label.place(relx = 5,
    #             rely = 5,
    #             anchor = 'center')
    label.pack()
    button_frame = tk.Frame(root)
    tk_text2 = "Raise"
    bet_button = tk.Button(
        button_frame, text=tk_text2,
        command=lambda: update_label_text(tk_text2),
        width=6, height=2, font=('Arial', 12))
    bet_button.pack(side="left", padx=40, pady=50)
    tk_text3 = "Fold"
    fold_button = tk.Button(
        button_frame, text=tk_text3,
        command=lambda: update_label_text(tk_text3),
        width=6, height=2, font=('Arial', 12))
    fold_button.pack(side="left", padx=40, pady=50)
    tk_text1 = "Call"
    call_button = tk.Button(
        button_frame, text=tk_text1,
        command=lambda: update_label_text(tk_text1),
        width=6, height=2, font=('Arial', 12))
    call_button.pack(side="left", padx=40, pady=50)
    button_frame.pack()
    # create a button to show a plot in a subwindow
    def show_plot():
        hand_chart.show_range(range_list)
    # create another frame to contain the "Exit" and "Answer" buttons
    button_frame2 = tk.Frame(root)
    plot_button = tk.Button(
        button_frame2, text="Answer", command=show_plot,
        width=8, height=2, font=('Arial', 12))
    plot_button.pack(side="left", padx=25, pady=25, anchor="e")
    button_frame2.pack(side="bottom")
    exit_button = tk.Button(
        button_frame2, text="Exit", command=lambda: exit_program2(root),
        width=8, height=2, font=('Arial', 12))
    exit_button.pack(side="left", padx=25, pady=25)
    def judge(hand, selection):
        if selection == 'Raise':
            if hand not in range_list:
                print(hand + ' Raise ✕  Fold ✓')
                mistake_record.append((hand, selection, position))
        elif selection == 'Fold':
            if hand in range_list:
                print(hand + ' Raise ✓ Fold ✕')
                mistake_record.append((hand, selection, position))
        elif selection == 'Call':
            if hand not in SB_call_list:
                if hand in SB_bet_list:
                    print(hand + ' ✕' + 'Raise ✓' )
                else:
                    print(hand + ' ✕' + ' ✓' )
                mistake_record.append((hand, selection, position))
        else:
            train_range.remove(hand)  # if right, remove it
            # print(hand + ' ' + selection)
            pass
        training_data.append((hand, selection, position))
        
    hand2 = hand
    # update the label's text when the user makes a selection
    def update_label_text(selection):
        nonlocal hand2
        judge(hand2, selection)
        hand = random.choice(train_range)
        updated_text = f"{hand} in {position}?"
        label.config(text=updated_text,padx=30,pady=30)
        root.update()  # refresh the window
        hand2 = hand
        
    root.mainloop()

def exit_program2(root):
    root.destroy()
    # exit(0)

action = get_action_popup()
mistake_df = pd.DataFrame(
    mistake_record, columns = ['Hand', 'Action', 'Position'])
counts = str(len(training_data))
print('训练手数 ' + counts)

saved_path = 'rif mis.xlsx'
if os.path.isfile(saved_path):
    mistake_df_pre = pd.read_excel(saved_path, index_col=0)
    merged_df = pd.concat([mistake_df_pre, mistake_df])
    merged_df.to_excel(saved_path)
else:
    mistake_df.to_excel(saved_path)

# mistake_df.to_excel('rif mis.xlsx')  # 覆盖




