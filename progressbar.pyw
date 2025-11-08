import threading
import time
import tkinter as tk
import tkinter.messagebox as msg
import tkinter.ttk as ttk

import pyvolume

# Initialise window
root = tk.Tk()
root.title("Volume Control")
root.geometry("300x300+200+200")
root.attributes("-topmost", 1)
root.resizable(False, False)

wait_time = 100
volume = 14
pyvolume.custom(int(volume))


def increase_vol():
    global wait_time
    global volume

    if wait_time != 100:
        for _ in range(int(100 / wait_time)):
            progress["value"] += int(wait_time)
            time.sleep(1)
        wait_time /= 2
        progress["value"] = 0
        volume += 1
        pyvolume.custom(int(volume))
        msg.showinfo(title="Success!", message="Volume has been incremented by 1!")

    elif wait_time == 100:
        progress["value"] = int(wait_time)
        time.sleep(1)
        wait_time /= 2
        progress["value"] = 0
        volume += 1
        pyvolume.custom(int(volume))
        msg.showinfo(title="Success!", message="Volume has been incremented by 1!")


def increase_volume():
    thread = threading.Thread(target=increase_vol)
    thread.start()


def decrease_vol():
    global wait_time
    global volume

    if wait_time != 100:
        for i in range(int(100 / wait_time)):
            progress["value"] += int(wait_time)
            time.sleep(1)
        wait_time /= 2
        progress["value"] = 0
        volume -= 1
        pyvolume.custom(int(volume))
        msg.showinfo(title="Success!", message="Volume has been decremented by 1!")

    elif wait_time == 100:
        progress["value"] = int(wait_time)
        time.sleep(1)
        wait_time /= 2
        progress["value"] = 0
        volume -= 1
        pyvolume.custom(int(volume))
        msg.showinfo(title="Success!", message="Volume has been decremented by 1!")


def decrease_volume():
    thread = threading.Thread(target=decrease_vol)
    thread.start()


label = tk.Label(root, text="Volume Control", font=("arial", 20))
label.pack(pady=10)

plus = tk.Button(root, text="+", font=("arial", 14), command=increase_volume)
plus.pack(padx=110, pady=20)

minus = tk.Button(root, text="-", font=("arial", 14), command=decrease_volume)
minus.pack(padx=130)

progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=100)
progress.pack(pady=15)

if __name__ == "__main__":
    root.mainloop()
