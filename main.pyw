# main.pyw

# imports
from random import randint
from tkinter.messagebox import showerror

from customtkinter import CTk, CTkButton, CTkLabel, CTkSlider
from pyvolume import custom

title: str = "Volume Control"[::-1]
volume = randint(1, 100)


def set_volume() -> None:
    global volume
    if int(volume) == 67:
        showerror(title="Why?!?!?!?!", message="No chance :)")

    else:
        custom(percent=int(volume))


def random_volume() -> None:
    global volume
    volume = randint(1, 100)
    volume_label.configure(text=f"{volume}")


# Screen
root: CTk = CTk()
root.title(title)
root.geometry("400x400+200+200")
root.attributes("-topmost", 1)

volume_label = CTkLabel(master=root, text=f"{volume}", font=("arial", 20))
volume_label.place(x=200, y=200)

label: CTkLabel = CTkLabel(
    master=root, text="Is this your desired volume?", font=("arial", 20)
)
label.pack()

# Buttons
yes: CTkButton = CTkButton(
    master=root, text="Yes", font=("arial", 16), command=set_volume
)
yes.place(x=50, y=350)

no: CTkButton = CTkButton(
    master=root, text="No", font=("arial", 16), command=random_volume
)
no.place(x=200, y=350)

# Start program
if __name__ == "__main__":

    root.mainloop()
