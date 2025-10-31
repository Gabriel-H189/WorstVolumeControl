# WorstVolumeControl
Programmers were asked to make the worst volume control they could think of for a contest... and so I deliver.

### Installation
Create virtual environment: `python -m venv .venv`

Activate: `.venv\Scripts\activate.bat`

Install dependencies: `pip install -r requirements.txt`

Run: `python main.pyw`

### How it actually works
The program randomly picks an integer from 1 to 100 and asks you "Is this your desired volume?" If you click yes, the desired volume is set. If you click no, another value is picked.

! Warning: You CANNOT set the volume to 67% !