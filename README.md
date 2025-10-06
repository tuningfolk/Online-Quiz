# Online-Quiz
ASE Challenge
## API Design

|endpoint   |METHOD |Description                        |
|-----------|-------|-----------------------------------|
|/create    |POST   |Create quiz with title             |
|/add       |POST   |Add questions to a quiz-Q should have text, multiple options with one correct|
|/fetch     |GET    |get all questions(without the answers) |
|/submit    |POST   |submit answers-request body: array of question IDs and selected option IDs, return score as {"score": 3, "total": 5}|



