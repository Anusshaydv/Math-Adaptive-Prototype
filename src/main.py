import time
from puzzle_generator import generate_puzzle
from tracker import log_attempt, get_summary, recent_history, clear_attempts
from adaptive_engine import next_level

def choose_initial_level() -> str:
    print("Choose initial difficulty:")
    print("1) Easy\n2) Medium\n3) Hard")
    pick = input("Enter 1/2/3 (default 1): ").strip()
    return {'1': 'easy', '2': 'medium', '3': 'hard'}.get(pick, 'easy')

def run_session(num_questions: int = 10):
    clear_attempts()

    name = input("Enter learner's name: ").strip() or "Learner"
    level = choose_initial_level()

    print(f"\nHello {name}! Starting at '{level}' level.")
    print(f"You will get {num_questions} questions.\n")

    for qnum in range(1, num_questions + 1):
        question, correct_ans = generate_puzzle(level)

        print(f"Q{qnum} (level = {level})")
        print(f"{question} = ?")

        start_time = time.time()
        user_input = input("Your answer: ").strip()
        time_taken = time.time() - start_time

        try:
            user_ans = int(user_input)
        except ValueError:
            user_ans = None

        is_correct = (user_ans == correct_ans)

        # Log the attempt
        log_attempt(
            question=question,
            user_ans=user_ans if user_ans is not None else -1,
            correct_ans=correct_ans,
            time_taken=time_taken
        )

        # Feedback to user
        if is_correct:
            print("Correct!")
        else:
            print(f"Incorrect. Correct answer is {correct_ans}")

        print(f"⏱ Time taken: {time_taken:.2f} seconds")

        # Decide next difficulty
        history = recent_history(10)
        new_level = next_level(history, level)

        if new_level != level:
            print(f"⬆ Difficulty changed: {level} → {new_level}")
        else:
            print(f"➡ Difficulty remains: {level}")

        level = new_level
        print("-" * 40)

    # Session summary
    summary = get_summary()
    print("\n SESSION SUMMARY")
    print(f"Total Questions: {summary['total']}")
    print(f"Correct Answers: {summary['correct']}")
    print(f"Accuracy: {summary['accuracy'] * 100:.1f}%")
    print(f"Average Time per Question: {summary['avg_time']:.2f} seconds")

if __name__ == "__main__":
    run_session(num_questions=10)
