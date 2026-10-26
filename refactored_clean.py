"""
Refactored version of messy.py adhering to course standards.
Maintains character-for-character identical printed output.
"""

PASSING_SCORE_THRESHOLD = 80

def calculate_average(scores):
    """Returns the arithmetic mean of a sequence of scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def count_students_above_threshold(scores, threshold):
    """Returns the count of scores meeting or exceeding the threshold."""
    return sum(1 for score in scores if score >= threshold)

if __name__ == "__main__":
    student_scores = [85, 90, 78, 92, 88, 76, 95, 89]
    
    # Printed output matches character-for-character with messy.py
    print(f"Avg is {calculate_average(student_scores)}")
    print(f"Count: {count_students_above_threshold(student_scores, PASSING_SCORE_THRESHOLD)}")
