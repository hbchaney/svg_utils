import PyQt5.QtWidgets as qtw

class OutputPane(qtw.QPlainTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
