from school_schedule.student import Student

# Write your tests here!

# Are the attributes correct
def test_student_attributes():
    name = "Quinn"
    grade = "junior"
    classes = ["Pre-Calc", "English III"]

    result = Student(name, grade, classes)

    assert result.name == name
    assert result.grade == grade
    assert result.classes == classes

# Do the methods act in the way they're supposed to
def test_student_no_classes():
    name = "Quinn"
    grade = "junior"
    classes = []

    result = Student(name, grade, classes)

    assert len(result.classes) == 0

def test_student_summary_output():
    name = "Quinn"
    grade = "junior"
    classes = ["Pre-Calc", "English III"]

    quinn = Student(name, grade, classes)
    result = quinn.summary()

    assert result == ("Quinn is a junior "
            "enrolled in 2 classes: "
            "Pre-Calc, English III")

def test_add_class_then_get_num_classes():
    name = "Quinn"
    grade = "junior"
    classes = ["Pre-Calc", "English III"]
    class_to_add = "Gym"
    quinn = Student(name, grade, classes)
    result = quinn.add_class(class_to_add)

    assert len(result) == 3
    assert len(quinn.classes) == 3
    assert quinn.classes == ["Pre-Calc", "English III", "Gym"]