import os.path
from flask import Flask
from flask.ext.autoindex import AutoIndex

app = Flask(__name__)
AutoIndex(app, browse_root=os.path.curdir)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
