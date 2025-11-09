from threading import Thread
from time import sleep
from tkinter import HORIZONTAL
from tkinter.messagebox import showinfo

from customtkinter import CTk, CTkButton, CTkLabel, CTkProgressBar  # type: ignore
from pyvolume import custom  # type: ignore

# Initialise window
root: CTk = CTk()
root.title("Volume Control")
root.geometry("300x300+200+200")
root.attributes("-topmost", 1)  # type: ignore
root.resizable(False, False)

wait_time = 100
volume = 14
custom(int(volume))


def increase_vol() -> None:
    """Increases volume"""

    global wait_time
    global volume

    if wait_time != 100:

        for _ in range(int(100 / wait_time)):

            progress.set(float(wait_time / 100))  # type: ignore
            root.update()
            sleep(1)

        wait_time /= 2
        progress.set(0)  # type: ignore
        volume += 1
        custom(int(volume))
        showinfo(title="Success!", message="Volume has been incremented by 1!")

    elif wait_time == 100:

        progress.set(int(wait_time / 100))  # type: ignore
        root.update()
        sleep(1)
        wait_time /= 2
        progress.set(0)  # type: ignore
        volume += 1
        custom(int(volume))
        showinfo(title="Success!", message="Volume has been incremented by 1!")


def increase_volume() -> None:
    """Starts volume increasing thread"""

    thread: Thread = Thread(target=increase_vol)
    thread.start()


def decrease_vol() -> None:
    """Decreases volume"""

    global wait_time
    global volume

    if wait_time != 100:

        for _ in range(int(100 / wait_time)):

            progress.set(float(wait_time / 100))  # type: ignore
            root.update()
            sleep(1)

        wait_time /= 2
        progress.set(0)  # type: ignore
        volume -= 1
        custom(int(volume))
        showinfo(title="Success!", message="Volume has been decremented by 1!")

    elif wait_time == 100:

        progress.set(int(wait_time / 100))  # type: ignore
        root.update()
        sleep(1)
        wait_time /= 2
        progress.set(0)  # type: ignore
        volume -= 1
        custom(int(volume))
        showinfo(title="Success!", message="Volume has been decremented by 1!")


def decrease_volume() -> None:
    """starts volume decreasing thread"""

    thread: Thread = Thread(target=decrease_vol)
    thread.start()


label: CTkLabel = CTkLabel(master=root, text="Volume Control", font=("arial", 20))
label.pack(pady=10)  # type: ignore

plus: CTkButton = CTkButton(
    master=root, text="+", font=("arial", 14), command=increase_volume
)
plus.pack(padx=110, pady=20)  # type: ignore

minus: CTkButton = CTkButton(
    master=root, text="-", font=("arial", 14), command=decrease_volume
)
minus.pack(padx=130)  # type: ignore

progress: CTkProgressBar = CTkProgressBar(
    master=root, orientation=HORIZONTAL, width=100
)
progress.pack(pady=15)  # type: ignore

if __name__ == "__main__":

    root.mainloop()  # type: ignore
