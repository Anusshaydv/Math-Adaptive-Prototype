import random
from typing import Tuple

def generate_puzzle(difficulty: str) -> Tuple[str, int]:
    """
    Generate a math puzzle and return (question_str, correct_answer)
    difficulty in {'easy', 'medium', 'hard'}
    """
    if difficulty == "easy":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        ops = ['+','-','*','/']
    elif difficulty == "medium":
        a = random.randint(10, 50)
        b = random.randint(1, 20)
        ops = ['+','-','*','/']
    else:  # hard
        a = random.randint(50, 200)
        b = random.randint(10, 50)
        ops = ['+','-','*','/']

    op = random.choice(ops)
    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b
    elif op == '/':
        ans = int(a / b)
    else:
        ans = a * b

    question = f"{a} {op} {b}"
    return question, ans
