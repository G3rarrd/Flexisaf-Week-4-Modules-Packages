from studenttools.student import Student


def student_summary(student: Student) -> dict:
    lines = []
    COLUMN_LEN : list[int] = [12, 30, 4, 5, 5, 5, 5, 5, 5]
    TOP_BORDER_LEN : int = sum(COLUMN_LEN) + (3 * len(COLUMN_LEN)) - 1
    
    lines.append("=" * TOP_BORDER_LEN)
    lines.append(f"NAME: {student.name}")
    lines.append(f"MATRIC NO: {student.matric_no}")
    lines.append(f"LEVEL: {student.level}")
    lines.append(f"GPA: {student.gpa}")
    lines.append("-" * TOP_BORDER_LEN)

    lines.append(
        f"{'COURSE CODE':<{COLUMN_LEN[0]}} | "
        f"{'COURSE TITLE':<{COLUMN_LEN[1]}} | "
        f"{'UNIT':<{COLUMN_LEN[2]}} | "
        f"{'ASSGN':<{COLUMN_LEN[3]}} | "
        f"{'TEST':<{COLUMN_LEN[4]}} | "
        f"{'ATTND':<{COLUMN_LEN[5]}} | "
        f"{'EXAM':<{COLUMN_LEN[6]}} | "
        f"{'TOTAL':<{COLUMN_LEN[7]}} | "
        f"{'GRADE':<{COLUMN_LEN[8]}} |"
    )

    lines.append("-" * TOP_BORDER_LEN)

    for r in student.records.values():
        lines.append(
            f"{r.course.code:<{COLUMN_LEN[0]}} | "
            f"{r.course.title[:COLUMN_LEN[1] - 1]:<{COLUMN_LEN[1]}} | "
            f"{r.course.unit:<{COLUMN_LEN[2]}} | "
            f"{r.assignment:<{COLUMN_LEN[3]}} | "
            f"{r.test:<{COLUMN_LEN[4]}} | "
            f"{r.attendance.score:<{COLUMN_LEN[5]}} | "
            f"{r.exam:<{COLUMN_LEN[6]}} | "
            f"{r.total:<{COLUMN_LEN[7]}} | "
            f"{r.letter_grade:<{COLUMN_LEN[8]}} |"
        )

    lines.append("-" * TOP_BORDER_LEN)

    print("\n".join(lines))

    # API/application-friendly structure
    return {
        "name": student.name,
        "matric_no": student.matric_no,
        "level": student.level,
        "gpa": student.gpa,
        "courses": [
            {
                "code": r.course.code,
                "title": r.course.title,
                "unit": r.course.unit,
                "assignment": r.assignment,
                "test": r.test,
                "attendance": r.attendance.score,
                "exam": r.exam,
                "total": r.total,
                "grade": r.letter_grade,
                "gp": r.grade_point,
            }
            for r in student.records.values()
        ],
    }