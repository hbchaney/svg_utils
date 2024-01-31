import os

import PyQt5.QtWidgets as qtw
from PyQt5 import QtGui

from .dash import Dash

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        self._dash = Dash()
        self.setCentralWidget(self._dash)
        self.setGeometry(600,600,1200,600)
        
        # Is Windows
        if os.name == 'nt':
            import ctypes
            app_id = 'svg_trimmer'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        
        self.setWindowTitle("SVG Trimmer")
        self.setWindowIcon(QtGui.QIcon(os.path.join(__location__, 'pug.png')))
        
        