from .student import Student

class HighSchoolStudent(Student):

    def __init__(self, name, grade, classes, has_parking_privileges=False,clubs=None):

        super().__init__(name, grade, classes)
        self.has_parking_privileges = has_parking_privileges
        self.clubs = clubs if clubs is not None else []

    def join_club(self, club_name):
        self.clubs.append(club_name)

    def display_parking_message(self):
        has_message = "has" if self.has_parking_privileges else "doesn't have"
        return f"{self.name} {has_message} parking privileges"

    def display_clubs(self):
        club_str = ", ".join(self.clubs)
        if club_str:
            return f"{self.name} is a member of: {club_str}"

        return f"{self.name} hasn't joined a club yet."
    
    # Override the student.summary() method while maintaining some of the parent qualities
    def summary(self):
        # Holds original text from the parent summary along with two other methods to construct a new summary for this particular child class of Student
        student_summary = super().summary()
        parking_msg = self.display_parking_message()
        club_msg = self.display_clubs()
        return "\n".join((student_summary, parking_msg, club_msg))