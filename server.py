from flask import Flask, send_from_directory
import random
from flask_cors import CORS

from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///budget.db")
Base = declarative_base()

class Counter(Base):
    __tablename__ = "Counter"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(String)
    Name = Column(String)
    Count = Column(Integer, default=0)

app = Flask(__name__)
CORS(app)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


if __name__ == "__main__":
    app.run(debug=True)


