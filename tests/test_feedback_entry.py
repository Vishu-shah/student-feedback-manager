# tests/test_feedback_entry.py

from feedback_entry import add_feedback

def test_add_feedback():
    result = add_feedback("Alice", "Math", 88)
    assert result['name'] == "Alice"
    assert result['subject'] == "Math"
    assert result['score'] == 88
