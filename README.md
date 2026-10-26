# Messy Python Code Improvement (Session 6)

Demonstrates systematic refactoring of unstructured legacy Python code using AI-assisted engineering in **Cursor AI**.

## Overview
This repository captures the complete refactoring workflow taught in Session 6: transitioning from an unformatted script (`messy.py`) with poor variable names and redundant logic to a clean, idiomatic implementation (`refactored_clean.py`) adhering to explicit standards (`.cursor/rules/python-standards.mdc`).

## Refactoring Standards Applied
* **Descriptive Naming:** Replaced single-letter variables (`s`, `t`, `st`, `c`) with meaningful identifiers (`scores`, `student_scores`, `threshold`).
* **Reusable Functions:** Replaced redundant average calculations with a modular `calculate_average()` utility function.
* **Docstrings:** Documented each function with a precise one-line docstring stating what it returns.
* **Constants:** Named magic numbers (`PASSING_SCORE_THRESHOLD = 80`).
* **Modern Formatting:** Replaced string concatenation with clean f-strings.
* **Preserved Output:** Maintained 100% character-for-character identical console output (`original_output.txt`).

## Technologies Used
* **Language:** Python 3.x
* **AI Tooling:** Cursor AI Agent, Ask Mode, Inline Edit, Rule Specification (`.mdc`)

## Author
* **Name:** Sakshi Sharma (B.Tech CSE, 2nd Year)
* **University:** JECRC University
