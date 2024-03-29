from datetime import datetime
import os
import subprocess
import sys

import PyQt5.QtWidgets as qtw

from .input_pane import InputPane
from .output_pane import OutputPane

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

class Dash(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self._input_pane = InputPane(self._on_button_press)
        self._output_pane = OutputPane()

        self._grid = qtw.QGridLayout()
        self._grid.addWidget(self._input_pane, 0, 0)
        self._grid.addWidget(self._output_pane, 0, 1)
        self._grid.setColumnStretch(0,3)
        self._grid.setColumnStretch(1,1)
        self.setLayout(self._grid)

    def _on_button_press(self):
        py = sys.executable
        parsing_script = os.path.join(__parent_dir__, "line_trimmer.py")
        in_file = self._input_pane.get_input_path()
        out_file = self._input_pane.get_output_path()

        try:
            self._validate_inputs(in_file, out_file)
        except Exception as e:
            self._output_pane.setPlainText(e.__str__())
            return
        error = False
        try:

            process = subprocess.run(
                [py, parsing_script, in_file, out_file, "--debug"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
        except:
            error = True
        if process.returncode == 0 and not error:
            out_str = (
                f"Success!\n"
                + f"A trimmed version of the .svg file at\n\n{in_file}\n\n"
                + f"has been saved to\n\n{out_file}\n\n!"
            )
        else:         
            log_name = f"trimmer_log_{datetime.now(): %Y-%m-%d.%H-%M-%S}.txt"
            log_folder = os.path.dirname(out_file)
            log_path = os.path.join(log_folder, log_name)
            with open(log_path, 'w') as f:
                f.write(process.stdout)
            
            out_str = (
                f"Failed trimming svg :(\n"
                + f"Could not trim the .svg file at {in_file}.\n\n"
                + f"The log file was saved to:\n\n{log_path}\n\n"
                + f"Please send the .svg file and the log to Harrison in an"
                + f" email."
            )
        
        self._output_pane.setPlainText(out_str)

    def _validate_inputs(self, in_path: str, out_path: str):
        if len(in_path) == 0:
            raise FileNotFoundError(
                "Please choose an input file."
            )
        
        if len(out_path) == 0:
            raise FileExistsError(
                "Please choose a place for the output to be saved."
            )
        
        if not os.path.exists(in_path):
            raise FileNotFoundError(
                "Error opening the input file, please confirm the input is "
                + "valid.")
        
        
