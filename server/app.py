#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from models import db, Student, Teacher
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Students(Resource):
    def get(self):
        students = [student.to_dict() for student in Student.query.all()]

        response = make_response(jsonify(students), 200)
        return response
    
class StudentByID(Resource):
    def get(self, id):
        student = Student.query.filter_by(id=id).first().to_dict()

        response = make_response(jsonify(student), 200)
        return response
    
    def patch(self, id):
        student = Student.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(student, attr, request.get_json()[attr])

        db.session.add(student)
        db.session.commit()

        student_dict = student.to_dict()
        response = make_response(jsonify(student_dict), 200)
        return response
    
    def delete(self, id):
        student = Student.query.filter_by(id=id).first()
        db.session.delete(student)
        db.session.commit()

        response = make_response(jsonify({"message": "student deleted successfully"}), 204)
        return response


    
api.add_resource(Students, '/students', endpoint='students')
api.add_resource(StudentByID, '/students/<int:id>', endpoint='student_id')

if __name__ == "__main__":
    app.run(port=5000, debug=True)