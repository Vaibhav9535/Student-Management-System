import uuid

class Student:
    def __init__(self,data: dict):
        self.id = str(uuid.uuid4())
        self.name = data.get("name")
        self.age = int(data.get("age"))
        self.Class = data.get("Class")
        self.gender = data.get("gender")

        grades = data.get("grades", {})
        self.grades = {
            "math": int(grades.get("math")),
            "history": int(grades.get("history")),
            "physics": int(grades.get("physics"))
        }
        self.avg = self.average()
    
    def average(self) -> float:
        return sum(self.grades.values()) / len(self.grades)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "Class": self.Class,
            "gender": self.gender,
            "grades": self.grades,
            "avg": self.average()
        }
    

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self,data:dict):
        student = Student(data)
        self.students.append(student)
        return student
    
    def get_all_students(self) -> list[Student]:
        return self.students
    
    def get_student_by_id(self,student_id:str):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    
    def search_student(self, query:str) -> list[Student]:
        query = query.lower()
        for student in self.students:
            if query in student.name.lower():
                return student
            
    def delete_student(self, student_id:str) -> bool:
        for i,student in enumerate(self.students):
            if student.id == student_id:
                del self.students[i]
                return True
        return False
    
    def update_student_grades(self, student_id:str, grades: dict):
        student = self.get_student_by_id(student_id)
        if student:
            student.grades = grades
            return student
        return None
    
    def search_topper(self, max_avg : float) -> list[Student]:
        for student in self.students:
            if max_avg == student.avg:
                return student
        return None
            
    def search_subject_topper(self,subject: str, max_subject_marks: str) -> list[Student]:
        for student in self.students:
            if student.grades[subject] == max_subject_marks:
                return student
        return None

    def max_and_avg_cal(self):
        avg_sum_of_all_students = 0
        avg_sum_of_maths = 0
        avg_sum_of_physics = 0
        avg_sum_of_history = 0
        max_avg = 0
        max_math_marks = 0
        max_history_marks = 0
        max_physics_marks = 0

        for student in self.students:
            avg_sum_of_all_students = student.avg + avg_sum_of_all_students
            avg_sum_of_maths = avg_sum_of_maths + student.grades["math"]
            avg_sum_of_physics = avg_sum_of_physics + student.grades["physics"]
            avg_sum_of_history = avg_sum_of_history + student.grades["history"]

            max_avg = max(max_avg,student.avg)
            max_math_marks = max(max_math_marks,student.grades["math"])
            max_history_marks = max(max_history_marks,student.grades["history"])
            max_physics_marks = max(max_physics_marks,student.grades["physics"])



        avg_of_class = avg_sum_of_all_students/len(self.students)
        avg_of_math = avg_sum_of_maths/len(self.students)
        avg_of_physics = avg_sum_of_physics/len(self.students)
        avg_of_history = avg_sum_of_history/len(self.students)

        return {
            "avg": {
                "class": avg_of_class,
                "math": avg_of_math,
                "history": avg_of_history,
                "physics": avg_of_physics
            },
            "max": {
                "avg": max_avg,
                "math": max_math_marks,
                "history": max_history_marks,
                "physics": max_physics_marks
            }
        }
    
    def stats(self, data: dict):
        max = data.get("max", {})
        avg = data.get("avg", {})
        subject_stats = {
            "math": {
                "average": avg.get("math"),
                "maximum": max.get("math")
            },
           "history": {
                "average": avg.get("history"),
                "maximum": max.get("history")
            },
            "physics": {
                "average": avg.get("physics"),
                "maximum": max.get("physics")
            }
        }
        return {
            "class_average": avg.get("class"),
            "class_topper": max.get("avg"),
            "subject_stats": subject_stats
        }