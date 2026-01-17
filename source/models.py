import uuid
from typing import List, Dict, Optional

class Student:
    def __init__(self, name: str, age: int, student_class: str, gender: str, grades: Dict[str, float] = None):
        self.student_id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.student_class = student_class
        self.gender = gender
        self.grades = grades if grades else {}

    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)



class StudentManager:
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, name: str, age: int, student_class: str, gender: str, grades: Dict[str, float]) -> Student:
        student = Student(name, age, student_class, gender, grades)
        self.students.append(student)
        return student

    def get_all_students(self) -> List[Student]:
        return self.students

    def get_student_by_id(self, student_id: str) -> Optional[Student]:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


    def search_students(self, query: str) -> List[Student]:
        if not query:
            return self.students
        
        query = query.lower()
        return [
            s for s in self.students 
            if query in s.name.lower() or query in s.student_class.lower()
        ]


    def update_student_details(self, student_id: str, name: str, age: int, student_class: str, gender: str, grades: Dict[str, float]) -> Optional[Student]:
        student = self.get_student_by_id(student_id)
        if student:
            student.name = name
            student.age = age
            student.student_class = student_class
            student.gender = gender
            student.grades = grades
            return student
        return None
    
    def delete_student(self, student_id: str) -> bool:
         for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                return True
         return False

    def get_class_statistics(self):
        if not self.students:
            return {
                "class_average": 0.0,
                "top_student": None,
                "subject_stats": {}
            }

        total_avg = sum(s.calculate_average() for s in self.students) / len(self.students)
        
        # Top student
        top_student = max(self.students, key=lambda s: s.calculate_average())
        
        # Subject stats
        subjects = set()
        for s in self.students:
            subjects.update(s.grades.keys())
            
        subject_stats = {}
        for subject in subjects:
            grades = [s.grades[subject] for s in self.students if subject in s.grades]
            if grades:
                subject_stats[subject] = {
                    "average": sum(grades) / len(grades),
                    "max": max(grades),
                    "min": min(grades)
                }

        return {
            "class_average": total_avg,
            "top_student": top_student,
            "subject_stats": subject_stats
        }
