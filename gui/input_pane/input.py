import pathlib

from typing import Callable

import PyQt5.QtWidgets as qtw

class InputPane(qtw.QWidget):

    def __init__(self, go_process: Callable):
        super().__init__()
        self._input_file_label = qtw.QLabel("Input SVG: ")
        self._output_file_label = qtw.QLabel("Trimmed SVG ")
        
        self._input_file_field = qtw.QLineEdit()
        self._output_file_field = qtw.QLineEdit()

        self._in_button = qtw.QPushButton(
                "Browse for Input", clicked=self._choose_input_file
            )
        self._save_location_button = qtw.QPushButton(
                "Browse for Save", clicked=self._choose_out_file
            )
        self._go_button = qtw.QPushButton("Go", clicked=go_process)

        self._grid = qtw.QGridLayout()

        self._grid.addWidget(self._input_file_label, 0, 0)
        self._grid.addWidget(self._input_file_field, 0, 1)
        self._grid.addWidget(self._in_button, 0, 2)
        self._grid.addWidget(self._output_file_label, 1, 0)
        self._grid.addWidget(self._output_file_field, 1, 1)
        self._grid.addWidget(self._save_location_button, 1, 2)
        self._grid.addWidget(self._go_button, 2, 0)
        self.setLayout(self._grid)

    def get_input_path(self) -> str:
        return self._input_file_field.text()
    
    def get_output_path(self) -> str:
        return self._output_file_field.text()
    
    def _choose_input_file(self) -> None:
        home_dir = pathlib.Path.home().__str__()
        filename, _ = qtw.QFileDialog.getOpenFileName(
                self,
                caption="Which file to open?",
                directory=home_dir,
                filter="SVG files (*.svg)"
        )

        filename = filename.strip()

        if filename == '':
            return
                
        self._input_file_field.setText(filename)

    def _choose_out_file(self) -> None:
        home_dir = pathlib.Path.home().__str__()
        filename, _ = qtw.QFileDialog.getSaveFileName(
                parent=self,
                caption = "Where to save file?",
                directory=home_dir,
                filter="SVG files (*.svg)"
            )
        filename = filename.strip()

        if filename == '':
            return
        
        if filename[-4:] != ".svg":
            filename = filename + ".svg"
        
        self._output_file_field.setText(filename)
