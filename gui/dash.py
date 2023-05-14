import PyQt5.QtWidgets as qtw

from .input_pane import InputPane
from .output_pane import OutputPane

class Dash(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self._input_pane = InputPane()
        self._output_pane = OutputPane()

        self._grid = qtw.QGridLayout()
        self._grid.addWidget(self._input_pane, 0, 0)
        self._grid.addWidget(self._output_pane, 0, 1)
        self.setLayout(self._grid)
