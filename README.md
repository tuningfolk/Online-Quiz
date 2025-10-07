# Online-Quiz
ASE Challenge
## API Design

|endpoint   |METHOD |Description                        |
|-----------|-------|-----------------------------------|
|/create    |POST   |Create quiz with title             |
|/add       |POST   |Add questions to a quiz- Question should have text, multiple options with one correct|
|/fetch     |GET    |Get all questions(without the answers) |
|/submit    |POST   |Submit answers. Request body: array of question IDs and selected option IDs, return score as {"score": 3, "total": 5}|

## Setup
```
git clone https://github.com/tuningfolk/Online-Quiz
cd Online-Quiz
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```
fastapi dev main.py
```



