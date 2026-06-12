GRADE_POINTS = {
    "A": 5.0,
    "B": 4.0,
    "C": 3.0,
    "D": 2.0,
    "E": 1.0,
    "F": 0.0,
}


def validate_score(score: float) -> None:
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")


def letter_grade(score: float) -> str:
    validate_score(score)

    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    return "F"


def grade_point(score: float) -> float:
    return GRADE_POINTS[letter_grade(score)]


def is_pass(score: float) -> bool:
    return score >= 40