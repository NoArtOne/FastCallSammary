"""
The flask application package.
"""

from flask import Flask

import FastCallSammary.views

app = Flask(__name__)

@app.route('/')
def 
