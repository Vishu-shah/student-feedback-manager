# feedback_entry.py

feedback_data = []

def add_feedback(student_name, subject, score):
    feedback = {
        "name": student_name,
        "subject": subject,
        "score": score
    }
    feedback_data.append(feedback)
    return feedback
