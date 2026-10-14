from PyQt5.QtWidgets import QDialog
from progress_ui import Ui_Dialog

class ProgressWindow(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Volume Control")
        self.plus_btn.clicked.connect(self.inc_volume)
        self.minus_btn.clicked.connect(self.dec_volume)

    def inc_volume(self):
        pass

    def dec_volume(self):
        pass