from school_schedule.student import Student
from school_schedule.high_school_student import HighSchoolStudent

# first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

# quinn.add_class("Painting")
# quinn.get_num_classes()
# print(quinn.summary())

# second instance
claire = HighSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                True, 
                ["Algorithms Club"]
            )

claire.get_num_classes()
print(claire.summary())