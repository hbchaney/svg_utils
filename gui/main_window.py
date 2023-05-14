import PyQt5.QtWidgets as qtw

from .dash import Dash

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        self._dash = Dash()
        self.setCentralWidget(self._dash)
        