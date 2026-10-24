VS Code mein:
1. Cmd + Shift + P press karo.
2. Search karo Python: Select Interpreter.
3. Apne project ke .venv wale Python interpreter ko select karo.




Ye hamare project ka isolated Python environment hai. Ismein install ki gayi libraries doosre Python projects se separate rahengi.

python3 -m venv .venv


Activate Karo
source .venv/bin/activate


Activation ke baad terminal prompt ke start mein usually (.venv) dikhega.


.venv/
Virtual environment ka main folder


bin/
Python executable aur commands, jaise python, pip aur activation script.


lib/
Installed Python packages aur environment ki library files.


pyvenv.cfg
Environment ki configuration, including base Python installation ka reference.