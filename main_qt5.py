# main_qt5.py
# -*- coding: utf-8 -*-

# required libraries
from sys import argv, exit

lazy from PyQt5.QtWidgets import QApplication
lazy from vc_window import VolumeControl


# Create an application and show the GUI
def main() -> None:
    app: QApplication = QApplication(argv)
    vc: VolumeControl = VolumeControl()
    vc.show()
    exit(app.exec())


# Only show GUI when ran directly
if __name__ == "__main__":
    main()
