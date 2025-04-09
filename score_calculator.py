# score_calculator.py

def calculate_average(feedback_list):
    if not feedback_list:
        return 0
    total = sum(item['score'] for item in feedback_list)
    return total / len(feedback_list)
