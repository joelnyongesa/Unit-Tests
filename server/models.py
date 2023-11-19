from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()


# Two classes, student and teachers.
# Relationships: One teacher, many students, one student, one teacher

class Student(db.Model, SerializerMixin):

    __tablename__ = "students"
    
    serialize_rules = ("-teacher.students",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))

    def __repr__(self):
        return f"Student {self.name}"

class Teacher(db.Model, SerializerMixin):

    __tablename__ = "teachers"

    serialize_rules = ("-students.teacher",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    students = db.relationship("Student", backref="teacher")