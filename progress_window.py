from sys import argv
from time import sleep
from typing import Self

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from progress_ui import Ui_frm_main
from pyvolume import custom


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    volume = pyqtSignal(int)

    def __init__(self: Self, volume: int, wait: int) -> None:
        super().__init__()
        self.target_volume: int = volume
        self.wait: int = wait

    @pyqtSlot()
    def run(self: Self) -> None:
        try:
            for i in range((self.wait * 100) + 1):
                sleep(self.wait / 20)
                self.progress.emit(i)

            custom(self.target_volume)
            self.volume.emit(self.target_volume)

        except Exception as exc:
            self.error.emit(str(exc))

        finally:
            self.finished.emit()

    error = pyqtSignal(str)

class ProgressWindow(QDialog, Ui_frm_main):
    def __init__(self: Self) -> None:
        self.wait_time: int = 1
        self._thread: QThread | None = None
        self._worker: Worker | None = None

        # setup the window
        QDialog.__init__(self)
        self.setupUi(self)
        self.btn_plus.clicked.connect(self.inc_volume)
        self.btn_minus.clicked.connect(self.dec_volume)

        # set the default volume
        self.volume: int = 14
        self.set_volume(self.volume)

    @pyqtSlot()
    def inc_volume_thread(self: Self) -> None:
        self._start_volume_change(2)

    @pyqtSlot()
    def dec_volume_thread(self: Self) -> None:
        self._start_volume_change(-2)

    def _start_volume_change(self: Self, delta: int) -> None:
        if self._thread is not None:
            return

        worker: Worker = Worker(self.volume + delta, self.wait_time)
        thread: QThread = QThread(self)
        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.progress.connect(self.update_progress)
        worker.volume.connect(self._volume_changed)
        worker.error.connect(self._show_error)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(self._operation_finished)
        thread.finished.connect(thread.deleteLater)

        self._worker = worker
        self._thread = thread
        self.btn_plus.setEnabled(False)
        self.btn_minus.setEnabled(False)
        
        thread.start()

    @pyqtSlot(int)
    def _volume_changed(self: Self, volume: int) -> None:
        self.volume = volume
        self.wait_time *= 2

    @pyqtSlot(str)
    def _show_error(self: Self, message: str) -> None:
        QMessageBox.warning(self, "Volume change failed", message)

    @pyqtSlot()
    def _operation_finished(self: Self) -> None:
        self._worker = None
        self._thread = None
        self.btn_plus.setEnabled(True)
        self.btn_minus.setEnabled(True)

    def set_volume(self: Self, volume: int) -> None:
        custom(volume)

    def inc_volume(self: Self) -> None:
        self.inc_volume_thread()

    def dec_volume(self: Self) -> None:
        self.dec_volume_thread()

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
