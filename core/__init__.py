from flask import Flask
import os
from dotenv import load_dotenv
from flask_wtf import CSRFProtect


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("secret_key")

csrf = CSRFProtect(app)


from core import routes
