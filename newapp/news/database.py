import os
import sqlite3
from shutil import copyfile
from termcolor import colored
from datetime import datetime
from . import app


def getDatabase():
    if "database" not in g:
        g.database = sqlite3.connect(
            app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.database.row_factory = sqlite3.Row
    return g.database


def closeDatabase(e=None):
    db = g.pop('database', None)
    if db is not None:
        db.close()


def dupDatabase():
    # Make replica of database
    if not os.path.exists(app.config["REPLICA"]):
        os.path.exists(app.config["REPLICA"])
    src = app.config["DATABASE"]
    tar = app.config["REPLICA"] + "/" + "dup_"
    tar += str(datetime.now()).replace(" ", "_")
    tar += ".db"
    copyfile(src, tar)
