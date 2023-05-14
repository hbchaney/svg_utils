import PyQt5.QtWidgets as qtw

class InputPane(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self._input_label = qtw.QLabel("Input Filepath: ")
        self._output_folder_label = qtw.QLabel("Output Folder: ")

        self._input_field = qtw.QLineEdit()
        self._output_folder_field = qtw.QLineEdit()

        self._button = qtw.QPushButton("Go")

        self._grid = qtw.QGridLayout()

        self._grid.addWidget(self._input_label, 0, 0)
        self._grid.addWidget(self._input_field, 0, 1)
        self._grid.addWidget(self._output_folder_label, 1, 0)
        self._grid.addWidget(self._output_folder_field, 1, 1)
        self._grid.addWidget(self._button, 2, 0)
        self.setLayout(self._grid)
