# backend/__init__.py

from flask import Flask
from flask_rbac import RBAC

app = Flask(__name__)
rbac = RBAC(app)