import os

import PyQt5.QtWidgets as qtw
from PyQt5 import QtGui

from .main_window import MainWindow

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))

class App(qtw.QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        self._mw = MainWindow()
        self.setWindowIcon(QtGui.QIcon(os.path.join(__location__, 'pug.png')))
        
        self._mw.show()
        self.exec()
        

if __name__ == '__main__':
    a = App([])