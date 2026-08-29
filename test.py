student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 160
}


def student_value_to_grading(value):
    if value > 100 or value < 0:
        raise ValueError("Value must be positive")
    elif value >= 91:
        return "Outstanding"
    elif value >= 81:
        return "Exceeds Expectations"
    elif value >= 71:
        return "Acceptable"
    else:
        return "Fail"


student_grades = {}
for name in student_scores:
    student_grades[name] = student_value_to_grading(student_scores[name])
    
print(student_grades)
    