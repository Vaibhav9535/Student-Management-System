from flask import Flask, request, render_template, jsonify, redirect# type: ignore
from logic import StudentManager

app = Flask(__name__)
manager = StudentManager()

manager.add_student({"name":"venki", "age":20 , "Class":"10A","gender":"male", "grades":{"math":95,"history":85,"physics":88}})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students' , methods = ['GET'])
def get_student():
    query = request.args.get('query','')
    if query:
        students = manager.search_student(query)
    else:
        students = manager.get_all_students()

    return jsonify([s.to_dict() for s in students])

@app.route('/api/students' , methods = ['POST'])
def add_student():
    data = {
        "name":request.form["name"],
        "age":request.form["age"],
        "Class":request.form["Class"],
        "gender":request.form["gender"],
        "grades":{
            "math":request.form["math"],
            "history":request.form["history"],
            "physics":request.form["physics"]
        }
    }
    student = manager.add_student(data)
    return jsonify(student.to_dict())

@app.route('/api/students/<student_id>', methods = ['PUT'])
def edit_student(student_id):
    data = request.json
    grades = data.get('grades')
    if grades:
        student = manager.update_student_grades(student_id, grades)
        if student:
            return jsonify(student.to_dict())
    return jsonify({"error": "Student not found or valid data not provided"})

@app.route('/api/students/<student_id>', methods = ['DELETE'])
def delete_student(student_id):
    success = manager.delete_student(student_id)
    if success:
        return jsonify({"message": "Student deleted"})
    return jsonify({"error": "Student not found"})

@app.route('/api/stats')
def stats():
    avg_max_data = manager.max_and_avg_cal()
    return jsonify(manager.stats(avg_max_data))

if __name__ == "__main__":
    app.run(debug=True)
