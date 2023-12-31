"""
Virtual environments in Python (venv):

Documentation:
https://docs.python.org/3/library/venv.html

A virtual environment carries your entire installation
from Python to a folder in the chosen path.
When activating a virtual environment, installing the
virtual environment will be used.
venv is the module we will use to
create virtual environments.
You can give whatever name you prefer to a
virtual environment, but the most common are:

Common names:
venv env (Windows)
.venv .env (Linux, MacOS, Unix). The dot(.) leaves the folder hidden

You can give whatever name you prefer to a
virtual environment, but the most common are:
venv env .venv .env

How to create virtual environments
Open your project folder in the terminal and type:

python -m venv venv

Checking which folder Python is running:

> gcm python.exe -Syntax

Versions:
> python --version
> pip --version

!Activate and deactivate a virtual environment:

Open your project folder in terminal and type:

>python -m venv venv

Activating and deactivating my virtual environment:

Windows: .\venv\Scripts\activate

Linux and Mac: source venv/bin/activate
Linux and Mac: . venv/bin/activate

deactivating: deactivate
"""
