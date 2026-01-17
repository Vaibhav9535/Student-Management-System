from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import StudentManager

app = Flask(__name__)
manager = StudentManager()

# Pre-populate some data for demo
# Pre-populate 15 Indian student records
manager.add_student("Aarav Sharma", 20, "10A", "Male", {"Math": 92, "Science": 89, "History": 84})
manager.add_student("Ananya Iyer", 19, "10B", "Female", {"Math": 98, "Science": 95, "History": 91})
manager.add_student("Vihaan Gupta", 21, "10A", "Male", {"Math": 76, "Science": 80, "History": 78})
manager.add_student("Ishani Verma", 20, "10C", "Female", {"Math": 85, "Science": 88, "History": 94})
manager.add_student("Arjun Reddy", 19, "10B", "Male", {"Math": 91, "Science": 82, "History": 87})
manager.add_student("Sanya Malhotra", 20, "10A", "Female", {"Math": 88, "Science": 90, "History": 85})
manager.add_student("Rohan Das", 21, "10C", "Male", {"Math": 65, "Science": 72, "History": 70})
manager.add_student("Meera Nair", 19, "10B", "Female", {"Math": 94, "Science": 96, "History": 98})
manager.add_student("Aditya Singh", 20, "10A", "Male", {"Math": 82, "Science": 85, "History": 80})
manager.add_student("Zoya Khan", 19, "10C", "Female", {"Math": 89, "Science": 91, "History": 92})
manager.add_student("Karthik Subramanian", 21, "10B", "Male", {"Math": 77, "Science": 79, "History": 83})
manager.add_student("Diya Mukherjee", 20, "10A", "Female", {"Math": 90, "Science": 87, "History": 88})
manager.add_student("Pranav Joshi", 19, "10C", "Male", {"Math": 84, "Science": 86, "History": 81})
manager.add_student("Avni Patel", 20, "10B", "Female", {"Math": 96, "Science": 93, "History": 95})
manager.add_student("Kabir Malhotra", 21, "10A", "Male", {"Math": 70, "Science": 75, "History": 72})


@app.route('/')
def index():
    query = request.args.get('q')
    if query:
        students = manager.search_students(query)
    else:
        students = manager.get_all_students()
    return render_template('index.html', students=students, query=query)

@app.route('/stats')
def stats():
    raw_stats = manager.get_class_statistics()
    
    # Process stats for template
    total_students = len(manager.get_all_students())
    top_student_name = raw_stats['top_student'].name if raw_stats['top_student'] else "-"
    
    # Extract just the average for each subject
    subject_averages = {
        subject: data['average'] 
        for subject, data in raw_stats['subject_stats'].items()
    }
    
    return render_template(
        'stats.html', 
        total_students=total_students,
        class_average=raw_stats['class_average'],
        top_student=top_student_name,
        subject_averages=subject_averages
    )

@app.route('/add', methods=['GET', 'POST'])
def add_student_page():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = int(request.form['age'])
            student_class = request.form['student_class']
            gender = request.form['gender']
            
            grades = {
                "Math": float(request.form.get('math', 0)),
                "Science": float(request.form.get('science', 0)),
                "History": float(request.form.get('history', 0))
            }
            
            manager.add_student(name, age, student_class, gender, grades)
            return redirect(url_for('index'))
        except ValueError:
            return "Invalid input", 400
            
    return render_template('add_student.html')





@app.route('/student/<student_id>')
def student_details(student_id):
    student = manager.get_student_by_id(student_id)
    if not student:
        return "Student not found", 404
    return render_template('student_details.html', student=student)

@app.route('/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = manager.get_student_by_id(student_id)
    if not student:
        return "Student not found", 404
        
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = int(request.form['age'])
            student_class = request.form['student_class']
            gender = request.form['gender']
            
            grades = {
                "Math": float(request.form.get('math', 0)),
                "Science": float(request.form.get('science', 0)),
                "History": float(request.form.get('history', 0))
            }
            
            manager.update_student_details(student_id, name, age, student_class, gender, grades)
            return redirect(url_for('index'))
        except ValueError:
            return "Invalid input", 400

    return render_template('edit_student.html', student=student)

@app.route('/delete/<student_id>', methods=['POST'])
def delete_student(student_id):
    manager.delete_student(student_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
