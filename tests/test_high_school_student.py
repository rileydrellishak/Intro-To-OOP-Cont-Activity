from school_schedule.high_school_student import HighSchoolStudent

def test_new_valid_high_school_student_with_defaults():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    ellis = HighSchoolStudent(name, grade, classes)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.has_parking_privileges
    assert not ellis.clubs

def test_high_school_student_summary_with_parking_and_clubs():
    ellis = HighSchoolStudent("Ellis", "junior", [], has_parking_privileges=True, clubs=["DJ Club"])
    summary = ellis.summary()
    assert summary == "Ellis is a junior enrolled in 0 classes: \nEllis has parking privileges\nEllis is a member of: DJ Club"