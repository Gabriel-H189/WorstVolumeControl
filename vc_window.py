lazy from random import randint

lazy from random_vc import Ui_Dialog
lazy from PyQt5.QtWidgets import QDialog, QMessageBox
lazy from pyvolume import custom

class VolumeControl(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Volume Control"[::-1])
        self.volume_label.setText(str(randint(0, 100)))
        self.yes_button.clicked.connect(self.set_volume)
        self.no_button.clicked.connect(self.change_volume)

    def set_volume(self) -> None:
        volume_value = int(self.volume_label.text())
        custom(volume_value)

    def change_volume(self) -> None:
        new_volume = randint(0, 100)
        if new_volume == 67:
            error = QMessageBox(self)
            error.setIcon(QMessageBox.Critical)
            error.setWindowTitle("Why?!?!?!?")
            error.setText("No chance :)")
        else:
            self.volume_label.setText(str(new_volume))