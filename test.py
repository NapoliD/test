# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Hola'

if __name__=='__main__':
    app.run()