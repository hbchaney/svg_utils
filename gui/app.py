import PyQt5.QtWidgets as qtw

from .main_window import MainWindow

class App(qtw.QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        self._mw = MainWindow()
        self._mw.show()
        self.exec()

if __name__ == '__main__':
    a = App([])