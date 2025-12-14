from typing import List, Dict

# Global simple in-memory attempts list (list of dicts)
attempts: List[Dict] = []

def log_attempt(question: str, user_ans: int, correct_ans: int, time_taken: float) -> None:
    attempts.append({
        'question': question,
        'user_ans': user_ans,
        'correct_ans': correct_ans,
        'correct': (user_ans == correct_ans),
        'time': time_taken
    })

def clear_attempts() -> None:
    attempts.clear()

def get_summary() -> Dict:
    if not attempts:
        return {'total': 0, 'correct': 0, 'accuracy': 0.0, 'avg_time': 0.0}
    total = len(attempts)
    correct = sum(1 for a in attempts if a['correct'])
    avg_time = sum(a['time'] for a in attempts) / total
    return {'total': total, 'correct': correct, 'accuracy': correct / total, 'avg_time': avg_time}

def recent_history(n: int = 10):
    """Return last n attempts (most recent last)."""
    return attempts[-n:]
events = []  # list of events like {'type':'level_change','from':'easy','to':'medium','reason':'3_correct','time':...}

def log_event(event_type: str, meta: dict):
    import time
    events.append({'type': event_type, 'meta': meta, 'ts': time.time()})

def get_events():
    return list(events)
