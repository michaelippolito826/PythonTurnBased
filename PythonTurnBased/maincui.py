import py_cui
from py_cui.colors import GREEN_ON_BLACK
from py_cui.widgets import Button


class TurnBasedGame:
    def __init__(self, master: py_cui.PyCUI):

        self.master = master
        
        action_screen_cell_title = 'Actions'
        
        # Three Main Cells
        self.main_screen_cell =    self.master.add_scroll_menu('Main Screen', 0, 0, row_span=6, column_span=4) # Top Left Cell
        self.action_screen_cell =  self.master.add_scroll_menu(action_screen_cell_title, 6, 0, row_span=2, column_span=4) # Bottom Left Cell
        self.champ_stats_cell =    self.master.add_scroll_menu('Champions On Field', 0, 4, row_span=6, column_span=2) # Top Right Cell

        # Buttons For Actions and Champs
        self.moves_button = self.master.add_button('Moves', 6, 4, row_span=1, column_span=2, command=self.to_moveset) #Top Button
        self.moves_button = self.master.add_button('Champions', 7, 4, row_span=1, column_span=2) #Bottom Button
        
    def to_moveset(self):
        action_screen_cell_title = 'Moves'
        self.action_screen_cell =  self.master.add_scroll_menu(action_screen_cell_title, 6, 0, row_span=2, column_span=4)
        
        
        test = "Q"
        self.action_screen_cell.add_item(f"{test}")
            
        # Textbox for entering new items
        # self.new_todo_textbox = self.master.add_text_box('TODO Item', 5, 0, column_span=2)

        # buttons for rest of control
        # self.mark_in_progress = self.master.add_button('Mark in Progress', 7, 0, column_span=2,    command=self.mark_as_in_progress)
        # self.mark_in_progress = self.master.add_button('Mark As Done',     7, 2, column_span=2,    command=self.mark_as_done)
        # self.remove_todo =      self.master.add_button('Remove TODO Item', 6, 1, pady = 1,         command=self.remove_item)
        # self.new_todo_add =     self.master.add_button('Add TODO Item',    6, 0, pady =1,          command=self.add_item)
        # self.save_todo_button = self.master.add_button('Save',             7, 4, column_span=2,    command=self.save_todo_file)

        # add some custom keybindings
        # self.new_todo_textbox.add_key_command(          py_cui.keys.KEY_ENTER, self.push_and_reset)
        # self.todo_scroll_cell.add_key_command(          py_cui.keys.KEY_ENTER, self.mark_as_in_progress)
        # self.in_progress_scroll_cell.add_key_command(   py_cui.keys.KEY_ENTER, self.mark_as_done)
        
    


root = py_cui.PyCUI(8, 6)
root.set_title('Leaguiemon')
s = TurnBasedGame(root)
root.start()