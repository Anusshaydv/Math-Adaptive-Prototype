from typing import List, Dict

LEVELS = ['easy', 'medium', 'hard']

def next_level(history: List[Dict], current_level: str) -> str:
    """
    Simple rule-based adaptation:
    - If last 3 attempts exist and are all correct -> increase difficulty (if possible)
    - If last 2 attempts exist and are both incorrect -> decrease difficulty (if possible)
    - Else keep same level.
    history: list of attempts (each attempt has 'correct' key). Most recent attempts are at the end.
    """
    if current_level not in LEVELS:
        current_level = 'easy'
    idx = LEVELS.index(current_level)

    # Look at last 3
    if len(history) >= 3:
        last3 = history[-3:]
        if all(a.get('correct', False) for a in last3) and idx < len(LEVELS)-1:
            return LEVELS[idx+1]

    # Look at last 2
    if len(history) >= 2:
        last2 = history[-2:]
        if all(not a.get('correct', False) for a in last2) and idx > 0:
            return LEVELS[idx-1]

    return current_level
