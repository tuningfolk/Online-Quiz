# Online-Quiz
ASE Challenge
## API Design

|endpoint   |METHOD |Description                        |
|-----------|-------|-----------------------------------|
|/create    |POST   |Create quiz with title             |
|/add       |POST   |Add questions to a quiz-Q should have text, multiple options with one correct|
|/fetch     |GET    |get all questions(without the answers) |
|/submit    |POST   |submit answers-request body: array of question IDs and selected option IDs, return score as {"score": 3, "total": 5}|

## Known Issues
Implement a more realistic  way of db handling
adding questions to a quiz with questions already may cause problems -- questions of same id may be a problem?


