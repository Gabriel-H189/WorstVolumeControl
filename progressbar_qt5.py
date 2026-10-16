from sys import argv, exit

lazy from PyQt5.QtWidgets import QApplication
lazy from progress_window import ProgressWindow


def main() -> None:
    app: QApplication = QApplication(argv)
    vc: ProgressWindow = ProgressWindow()
    vc.show()
    exit(app.exec())


if __name__ == "__main__":
    main()

