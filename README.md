# WorstVolumeControl
Programmers were asked to make the worst volume controls they could think of for a contest... and so I deliver.

### Files
`main.pyw`: The random volume control interface.

`progressbar.pyw`: Another volume control that requires a progress bar to fill up in order for the volume to change.

### Installation
Create virtual environment: `python -m venv .venv`

Activate: `.venv\Scripts\activate.bat`

Install dependencies: `pip install -r requirements.txt`

Run: `python main.pyw` or `python progressbar.pyw`

### How it actually works
The program randomly picks an integer from 0 to 100 and asks you "Is this your desired volume?" If you click yes, the desired volume is set. If you click no, another value is picked.

Odd numbers are not supported for some reason. It is what it is!

**Warning: You CANNOT set the volume to 67%!**
