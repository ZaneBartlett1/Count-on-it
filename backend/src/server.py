from typing import List, Tuple, Union
from flask import Flask, send_from_directory, jsonify, Response, request
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
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

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


@app.route("/")
def base() -> Response:
    """
    Serves the main Svelte page.
    """
    return send_from_directory("client/public", "index.html")


@app.route("/<path:path>")
def home(path: str) -> Response:
    """
    Serves static files (compiled JS/CSS, etc.) for the SPA application.
    """
    return send_from_directory("client/public", path)


@app.route("/counters")
def get_counters() -> Response:
    """
    Retrieves all counters from the database and returns them as a JSON string.
    """
    session = Session()

    counters = session.query(Counter).all()
    counters_json = [
        {"id": counter.id, "Name": counter.Name, "Count": counter.Count}
        for counter in counters
    ]

    session.close()

    return jsonify(counters_json)


@app.route("/increment/<int:id>")
def increment(id: int) -> str:
    """
    Increments the count of the counter with the given id. If the counter does not exist, it will be created with an initial count of 1.

    :param id: The id of the counter to increment
    :return: The updated count as part of a JSON object
    """
    session = Session()

    counter = session.query(Counter).get(id)
    if counter:
        counter.Count += 1  # type: ignore
    else:
        counter = Counter(id=id, Count=1)
        session.add(counter)

    session.commit()
    count = counter.Count  # retrieve the count from the counter object

    session.close()

    return json.dumps({"count": count})  # return the count as part of a JSON object


@app.route("/add-counter", methods=["POST"])
def add_counter() -> Tuple[Union[Response, str], int]:
    """
    Adds a new counter with the given name and an initial count of 0.

    :return: A success message with the new counter's ID or an error message if a counter with the same name already exists
    """
    session = Session()

    name = request.form.get("name")

    # Check if a counter with the same name already exists
    existing_counter = session.query(Counter).filter_by(Name=name).first()
    if existing_counter:
        session.close()
        return jsonify({"error": "Counter with the same name already exists"}), 400

    # Create a new Counter object with the given name and a count of 0
    new_counter = Counter(Name=name, Count=0)
    session.add(new_counter)
    session.commit()

    new_id = new_counter.id

    # Close the session and return a success message with the new counter's ID
    session.close()

    return jsonify({"id": new_id, "message": "Counter successfully added"}), 201


@app.route("/delete-counter/<int:id>", methods=["DELETE"])
def delete_counter(id: int) -> Union[str, Tuple[str, int]]:
    """
    Deletes a counter with the given id.
    :param id: The id of the counter to delete
    :return: A success message or an error message if the counter with the specified id does not exist
    """

    session = Session()

    counter = session.query(Counter).get(id)
    if not counter:
        session.close()
        return "Counter with the id does not exist", 400

    session.delete(counter)
    session.commit()

    session.close()

    return "Counter successfully deleted"


if __name__ == "__main__":
    app.run(debug=True)
