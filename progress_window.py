from sys import argv
from time import sleep
from typing import Self

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from progress_ui import Ui_Dialog
from pyvolume import custom


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    volume = pyqtSignal(int)
    wt = pyqtSignal(int)

    def wait_inc_volume(self: Self, vol: int, wait: int) -> None:
        self.volume.emit(vol + 2)
        for i in range((wait * 100) + 1):
            sleep(wait / 20)
            self.progress.emit(i)

        custom(vol)
        self.wt.emit(wait * 2)
        self.finished.emit()

    def wait_dec_volume(self: Self, vol: int, wait: int) -> None:
        self.volume.emit(vol + 2)
        for i in range((wait * 100) + 1):
            sleep(wait / 20)
            self.progress.emit(i)

        custom(vol)
        self.wt.emit(wait * 2)
        self.finished.emit()

class ProgressWindow(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        self.wait_time: int = 1

        # setup the window
        QDialog.__init__(self)
        self.setupUi(self)
        self.plus_btn.clicked.connect(self.inc_volume)
        self.minus_btn.clicked.connect(self.dec_volume)

        # set the default volume
        self.volume: int = 14
        self.set_volume(self.volume)

    @pyqtSlot()
    def inc_volume(self: Self) -> None:

        self.thread: QThread = QThread()
        self.worker: Worker = Worker()

        self.worker.moveToThread(self.thread)
        
        self.thread.started.connect(lambda: self.worker.wait_inc_volume(self.volume, self.wait_time))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_progress)
        
        self.thread.start()

        # Final resets
        self.plus_btn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.plus_btn.setEnabled(True)
        ) 

        self.wait_time *= 2
        self.volume += 2

    @pyqtSlot()
    def dec_volume(self: Self) -> None:
        
        self.thread: QThread = QThread()
        self.worker: Worker = Worker()

        self.worker.moveToThread(self.thread)
        
        self.thread.started.connect(lambda: self.worker.wait_inc_volume(self.volume, self.wait_time))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_progress)
        
        self.thread.start()

        # Final resets
        self.minus_btn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.minus_btn.setEnabled(True)
        ) 

        self.wait_time *= 2
        self.volume -= 2

    def set_volume(self: Self, volume: int) -> None:
        custom(volume)


    @pyqtSlot(int)
    def update_progress(self: Self, val: int) -> None:
        self.progressbar.setValue(val)


def main() -> None:
    app: QApplication = QApplication(argv)
    pw: ProgressWindow = ProgressWindow()
    pw.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()

