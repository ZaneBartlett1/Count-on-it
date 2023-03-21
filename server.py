from flask import Flask, send_from_directory, jsonify
import random
from flask_cors import CORS
import json

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

engine = create_engine("sqlite:///count-on-it.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)  # create a sessionmaker object

class Counter(Base):
    __tablename__ = "Counter"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(String)
    Name = Column(String)
    Count = Column(Integer, default=0)


Base.metadata.create_all(engine)  # <--- Check and create the table

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


@app.route("/counters")
def get_counters():
    session = Session()

    counters = session.query(Counter).all()
    counters_json = [{"id": counter.id, "Name": counter.Name, "Count": counter.Count} for counter in counters]

    session.close()

    return jsonify(counters_json)


@app.route("/increment/<name>")
def increment(name):
    session = Session()

    counter = session.query(Counter).filter_by(Name=name).first()
    if counter:
        counter.Count += 1
    else:
        counter = Counter(Name=name, Count=1)
        session.add(counter)

    session.commit()
    count = counter.Count  # retrieve the count from the counter object

    session.close()

    return json.dumps({"count": count})  # return the count as part of a JSON object


@app.route("/add-counter/<name>", methods=["POST"])
def add_counter(name):
    session = Session()

    # Check if a counter with the same name already exists
    existing_counter = session.query(Counter).filter_by(Name=name).first()
    if existing_counter:
        session.close()
        return jsonify({"error": "Counter with the same name already exists"}), 400

    # Create a new Counter object with a count of 0
    new_counter = Counter(Name=name, Count=0)
    session.add(new_counter)
    session.commit()

    new_id = new_counter.id

    # Close the session and return a success message with the new counter's ID
    session.close()
    
    return jsonify({"id": new_id, "message": "Counter successfully added"})


@app.route("/delete-counter/<name>", methods=["DELETE"])
def delete_counter(name):
    session = Session()

    # Check if a counter with the name exists
    existing_counter = session.query(Counter).filter_by(Name=name).first()
    if existing_counter == False:
        session.close()
        return "Counter with the name does not exist", 400

    session.delete(existing_counter)
    session.commit()

    # Close the session and return a success message
    session.close()
    
    return "Counter successfully deleted"



if __name__ == "__main__":
    app.run(debug=True)
