# 🧠 Sample Test Quiz

## Purpose  
This project presents users with a short 4-question quiz, based on the difficulty level they select. It is designed to help beginners practice Python fundamentals such as loops, conditionals, functions, user input handling, and string replacement.

##  Technologies Used  
- Python 2.7  
- CLI interface with `raw_input()` and `print` (Python 2 syntax)  
- No external libraries required

## Features
- Prompts user to choose a difficulty level: easy, medium, or hard  
- Each level contains 4 fill-in-the-blank questions  
- Correct answers fill the blanks dynamically  
- Incorrect answers are re-asked until correct  
- Total number of attempts is shown at the end  
- Option to restart the quiz

## Sample Flow
choose level: easy / medium / hard
Choose a level: easy

elephants have tails (yes/no)  1
crows have 3 eyes (true/false) 2
result of this (21/7)+2        3
capital of turkey?             4

===> Answer for __1__  : yes
Correct!
===> Answer for __2__  : true
You are wrong, try again.

…

ALL ANSWERS ARE TRUE!
elephants have tails (yes/no)  yes
…
YOU HAVE DONE 6 TRIAL!

## 📦 Installation
```bash
git clone https://github.com/masaldede/sample-test-quiz.git
cd sample-test-quiz
python testquiz.py

Note: This code is written in Python 2.7. If you’re using Python 3, you’ll need to update print statements and replace raw_input() with input().

🗺️ What I Learned
	•	Building interactive CLI tools
	•	Using while loops and if-elif conditionals
	•	Handling user input and validating answers
	•	Replacing text dynamically with replace()
	•	Designing scalable question/answer sets

🧑‍🏫 Educational Use

I created this project to support beginner-level Python learners. It can be reused or adapted to build small quizzes in areas like math, geography, general knowledge, or tech fundamentals.



