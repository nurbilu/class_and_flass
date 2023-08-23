class Student:
    def __init__(self, first_name, last_name, student_id, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" 


    def print_name(self):
        print(self.get_full_name())

    def add_course(self, course_name):
        """Add a course to the student's list of courses."""
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{course_name} has been added to {self.get_full_name()}'s courses.")
        else:
            print(f"{self.get_full_name()} is already enrolled in {course_name}.")

    def remove_course(self, course_name):
        """Remove a course from the student's list of courses."""
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{course_name} has been removed from {self.get_full_name()}'s courses.")
        else:
            print(f"{self.get_full_name()} is not enrolled in {course_name}.")

    def display_courses(self):
        """Display the list of courses the student is enrolled in."""
        if self.courses:
            print(f"{self.get_full_name()}'s enrolled courses: {', '.join(self.courses)}")
        else:
            print(f"{self.get_full_name()} is not enrolled in any courses.")

# Example usage:
student1 = Student("John", "Doe", "12345")
student1.print_name()
student1.add_course("Mathematics")
student1.add_course("History")
student1.display_courses()
student1.remove_course("History")
student1.display_courses()
