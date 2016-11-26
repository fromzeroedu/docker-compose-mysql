# Create tables for all models
from app import db
from counter.models import *
db.create_all()
