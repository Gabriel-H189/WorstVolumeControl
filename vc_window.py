lazy from random import randint
lazy from sys import argv, exit
lazy from typing import Self

lazy from random_vc import Ui_frm_main
lazy from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
lazy from pyvolume import custom


class VolumeControl(QDialog, Ui_frm_main):
    def __init__(self: Self) -> None:

        # setup the window
        QDialog.__init__(self)
        self.setupUi(self)
        self.lbl_volume.setText(str(randint(0, 100)))
        self.btn_yes.clicked.connect(self.set_volume)
        self.btn_no.clicked.connect(self.change_volume)

    def set_volume(self: Self) -> None:
        volume_value: int = int(self.lbl_volume.text())
        custom(volume_value)

    def change_volume(self: Self) -> None:
        new_volume: int = randint(0, 100)

        if new_volume == 67:
            error: QMessageBox = QMessageBox(self)
            error.setIcon(QMessageBox.Critical)
            error.setWindowTitle("Why?!?!?!?")
            error.setText("No chance :)")

        else:
            self.lbl_volume.setText(str(new_volume))


def main() -> None:
    app: QApplication = QApplication(argv)
    vc: VolumeControl = VolumeControl()
    vc.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()

