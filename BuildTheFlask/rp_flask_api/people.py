
from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema






def read_all():
    people = Person.query.filter(Person.lname == lname).one_or_none()
    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")


def create(person):

    new_person = person_schema.load(person, session=db.session)
    db.session.add(new_person)
    db.session.commit()
    return person_schema.dump(new_person), 201


    # lname = person.get("lname")
    # existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    # if existing_person is None:
    #     new_person = person_schema.load(person, session=db.session)
    #     db.session.add(new_person)
    #     db.session.commit()
    #     return person_schema.dump(new_person), 201
    # else:
    #     abort(406, f"Person with last name {lname} already exists")


def read_one(lname):
    person = Person.query.get(person_id)
    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404,f"Person with ID {person_id} not found")

def read_all():
    people = Person.query.all()
    return people_schema.dump(people)



def update(lname, person):
    existing_person = Person.query.get(person_id)

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with ID {person_id} not found")


def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)

    else:
        abort(404, f"Person with last name {lname} not found")


# %%
import sqlite3
print("Hello world!")
conn = sqlite3.connect("people.db")
columns = [
    "id INTEGER PRIMARY KEY",
    "lname VARCHAR UNIQUE",
    "fname VARCHAR",
    "timestamp DATETIME"
]
create_table_cmd = f"CREATE TABLE person1 ({','.join(columns)})"
conn.execute(create_table_cmd)
# %%
conn = sqlite3.connect("people.db")
people = [
    "1, 'Fairy', 'Tooth', '2022-10-08 09:15:10'",
    "2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'",
    "3, 'Bunny', 'Easter', '2022-10-08 09:15:27'",
]
for person_data in people:
    insert_cmd = f"INSERT INTO person1 VALUES ({person_data})"
    conn.execute(insert_cmd)
# %%
conn.commit()
# %%
import sqlite3
conn = sqlite3.connect("people.db")
cur = conn.cursor()
cur.execute("SELECT * FROM person")


# %%
people = cur.fetchall()
for person in people:
    print(person)
# %%
