from faker import Faker
from models import db, Student, Teacher
from app import app
from random import choice as rc


fake = Faker()

with app.app_context():
    print("Clearing the database...")

    Student.query.delete()
    Teacher.query.delete()

    print("Database emptied...")

    teachers = []

    for _ in range(10):
        teacher = Teacher(
            name=fake.name()
        )
        teachers.append(teacher)

    print("Adding teachers...")
    db.session.add_all(teachers)

    students = []

    for _ in range(15):
        student = Student(
            name=fake.name(),
            teacher=rc(teachers)
        )

        students.append(student)

    print("Adding students...")
    db.session.add_all(students)

    db.session.commit()

    print("Done seeding...")
    