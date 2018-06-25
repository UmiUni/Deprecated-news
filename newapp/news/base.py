import os
from . import app
from .command import initApp
from .config import Config

# Load config
app.config.from_object(Config)

# Create instance path
if not os.path.exists(app.instance_path):
    os.makedirs(app.instance_path)


initApp()


@app.route('/config')
def getConfig():
    return str(dict(app.config))