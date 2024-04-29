from flask import Blueprint
from app import db
from sqlalchemy import or_, and_
from models import Time
main = Blueprint('main', __name__)

@main.route('/')
def time_of_entry():
    current_time = Time()
    db.session.add(current_time)
    db.session.commit()
    count = Time.query.count()
    last_visit = Time.query.order_by(Time.id.desc()).first().date_entry
    return {"number_of_visits": str(count), "last_visit": str(last_visit)}