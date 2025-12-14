# Math-Adaptive-Prototype
## Math Adventures — Adaptive Learning Prototype

An AI-inspired adaptive math learning system that dynamically adjusts problem difficulty based on learner performance.  
This project demonstrates how adaptive logic can personalize learning to keep students in their optimal challenge zone.

---

## Objective

To build a minimal adaptive learning prototype for children (ages 5–10) that:
- Generates math puzzles dynamically
- Tracks learner performance (correctness and response time)
- Automatically adjusts difficulty based on performance
- Displays a summary of learning outcomes at the end of the session

The focus of this project is on adaptive logic, not UI or visuals.

---

## Approach Used

This prototype uses a **rule-based adaptive engine** (not a trained ML model).

**Why rule-based?**
- No real historical user data is available
- Rules are deterministic, explainable, and easy to reason about
- Ideal for early-stage adaptive learning systems

> With real user data, this system can later be upgraded to a lightweight ML model such as logistic regression or a decision tree.

---

## Features

- Dynamic math puzzle generation
- Three difficulty levels: **Easy, Medium, Hard**
- Real-time performance tracking:
  - Correct / incorrect answers
  - Time taken per question
- Automatic difficulty adaptation
- Immediate feedback after each question
- End-of-session performance summary

---

## Adaptive Logic

The system adjusts difficulty using recent learner performance:

- If the **last 3 questions are answered correctly** → difficulty increases
- If the **last 2 questions are answered incorrectly** → difficulty decreases
- Otherwise → difficulty remains unchanged

This keeps the learner within an appropriate challenge zone.

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Anusshaydv/Math-Adaptive-Prototype.git
cd math-adaptive-prototype
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the program
```bash
python src/main.py
```

---

## Output

### 1.During the session:

- Displays whether each answer is correct or incorrect

- Shows time taken for each question

- Indicates the difficulty level of the next question

### 2.At the end of the session:

- Total number of questions attempted

- Number of correct answers

- Accuracy percentage

- Average response time per question

---

## Metrics Tracked

- Correctness (True / False)

- Response time per question

- Accuracy

- Difficulty transitions

These metrics drive the adaptive learning behavior and final summary.

---

## Future Improvements

- Upgrade to a lightweight ML-based adaptive engine

- Add support for division and mixed operations

- Visualize progress with charts or dashboards

- Store long-term learner progress

- Build a simple web interface (e.g., Streamlit)

---

## Deliverables

- Functional adaptive learning prototype

- Clean, modular Python code

- Automatic difficulty adjustment

4.Performance tracking and summary
