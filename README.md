# Simple Chat Bot

A simple chat bot in python.

Install all dependencies
``pip install -r requirements.txt``

Run the main.py file
``python main.py``

If you get the error "AttributeError: module 'time has no attribute 'clock'"

Browse to ``C:\Users\{enter your username here}\AppData\Local\Programs\Python\{enter your python folder here}\Lib\site-packages\sqlalchemy\util``

Open ``compat.py`` search for ``time.clock`` with Ctrl + F and replace it with ``time.time``


## You can add your own language support by simply training it on other languages

All languages are located here 
