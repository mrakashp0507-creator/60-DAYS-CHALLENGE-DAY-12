# 🐍 Day 12 – String Processing

## 📌 Overview

Day 12 focuses on string manipulation and understanding space usage.

The project takes a string from the user and reverses it without using Python's built-in reverse functions.

## 🎯 Problem Statement

Create a Python program that:

1. Takes a string as input.
2. Reverses the string.
3. Prints the original string.
4. Prints the reversed string.
5. Explains the space required by the solution.

## 💡 Example

Input:

Hello World

Output:

Original String: Hello World
Reversed String: dlroW olleH

## 🧠 Approach

The program starts from the last character of the string and moves toward the first character.

For example:

Python

Characters:

P y t h o n

Reverse order:

n o h t y P

Result:

nohtyP

The program uses a loop:

for i in range(len(text) - 1, -1, -1):

This allows the string to be traversed backwards.

## ⚡ Complexity

### Time Complexity

O(n)

Every character is processed once.

### Space Complexity

O(n)

The reversed string is stored separately and can contain n characters.

## 🌍 Real-World Applications

String processing is used extensively in software systems.

Examples include:

### Chat Systems

Messages are stored and processed as strings.

### Log Processing

Applications process log messages to search for errors, events, and patterns.

### Search Engines

Search systems process text to identify keywords and relevant content.

### Text Processing

Applications frequently manipulate strings for formatting, validation, searching, and analysis.

## 🛠️ Technologies

- Python 3
- VS Code
- Git
- GitHub

## 📂 Project Structure

Day12-String-Processing/
│
├── day12_reverse_string.py
└── README.md

## 🚀 How to Run

Open the project in VS Code.

Run:

python day12_reverse_string.py

Example:

Enter a string: Python

Output:

Original String: Python
Reversed String: nohtyP

## 📤 GitHub Submission

git add day12_reverse_string.py README.md

git commit -m "Complete Day 12 string processing"

git push

## 👨‍💻 Author

Akash

---

🐍 Python Mastery Sprint – Day 12
