# tests/test_score_calculator.py

from score_calculator import calculate_average

def test_calculate_average():
    feedback = [
        {"name": "Alice", "subject": "Math", "score": 80},
        {"name": "Bob", "subject": "Science", "score": 90}
    ]
    assert calculate_average(feedback) == 85.0
