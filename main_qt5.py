from sys import argv, exit

lazy from PyQt5.QtWidgets import QApplication
lazy from vc_window import VolumeControl

def main() -> None:
    app: QApplication = QApplication(argv)
    vc = VolumeControl()
    vc.show()
    exit(app.exec())

if __name__ == "__main__":
    main()