import json

from app import app
from models import db, Student, Teacher



class TestApp:
    '''Flask application in flask_app.py'''

    def test_has_a_students_route(self):
        '''has an endpoint "/students"'''
        response = app.test_client().get('/students')
        assert (response.status_code == 200)

    def test_student_by_id(self):
        '''has a resource available at "/students/<int:id>"'''
        response = app.test_client().get('/students/1')
        assert(response.status_code == 200)

    def test_student_by_id_route_returns_one_student(self):
        '''return JSON object representing one Student object at "students/<int:id>".'''
        response = app.test_client().get('students/1')
        data = json.loads(response.data.decode())

        assert(type(data) == dict)
        assert(data["id"])
        assert(data["name"])

    def test_student_by_id_patch_route_updates_student_name(self):
        '''returns JSON representing the updated Student object with name="Sam Altman" at "/students/<int:id>".'''
        with app.app_context():
            student_1 = Student.query.filter_by(id=1).first()
            student_1.name = "Joel Nyongesa"
            db.session.add(student_1)
            db.session.commit()

        response = app.test_client().patch(
            '/students/1',
            json = {
                "name": "Sam Altman",
            }
        )

        data = json.loads(response.data.decode())

        assert(type(data) == dict)
        assert(data["id"])
        assert(data["name"] == "Sam Altman")

    def test_student_by_id_delete_route_deletes_student(self):
        '''returns a JSON representing updated Student object at "/student/<int:id>".'''
        with app.app_context():
            student = Student(
                name="Joyce Mwangi"
            )

            db.session.add(student)
            db.session.commit()

            response = app.test_client().delete(f'/students/{student.id}')
            data = response.data.decode()

            assert(not data)

    # def test_creates_student(self):
    #     '''can create a new student through "/students" route'''

    #     with app.app_context():

    #         joel = Student.query.filter_by(name="Joel Nyongesa").first()

    #         if joel:
    #             db.session.delete(joel)
    #             db.session.commit()
            
    #         response = app.test_client().post(
    #             '/students',
    #             data={
    #                 "name": "Joel Nyongesa"
    #             }
    #         )

    #         joel = Student.query.filter_by(name="Joel Nyongesa").first()

    #         assert response.status_code == 201
    #         assert response.content_type == "application/json"
    #         assert joel.id