from fastapi import FastAPI,HTTPException
from typing import Union, List
from pydantic import BaseModel
quizzes = []
class Option(BaseModel):
    id: int
    text: str
class QuestionOut(BaseModel):
    id: int
    options: List[Option] = []

class QuestionIn(BaseModel):
    id: int
    options: List[Option] = []
    correct_option_id: int

class Quiz(BaseModel):
    id: int
    title: str
    questions: List[QuestionIn] = []

class CreateQuiz(BaseModel):
    title: str

class CreateQuestions(BaseModel):
    quiz_id: int
    questions: List[QuestionIn] = []
app = FastAPI()

@app.get("/fetch/{quiz_id}")
def read_root(quiz_id: int):
    if quiz_id < 0 or quiz_id >= len(quizzes):
        raise HTTPException(status_code=404, detail="Item not found")

    questions = quizzes[quiz_id].questions
    return [
            QuestionOut(id=q.id, options=q.options) for q in questions
    ]

@app.post("/create")
def create_quiz(quiz: CreateQuiz):
    quiz_id = len(quizzes)
    quiz = Quiz(id=quiz_id, title=quiz.title)
    quizzes.append(quiz)
    return {"quiz_id": quiz.id, "quiz_title": quiz.title}

@app.post("/add")
def add_questions(create_questions: CreateQuestions):
    quiz_id = create_questions.quiz_id
    if quiz_id<0 or quiz_id>=len(quizzes):
        raise HTTPException(status_code=404, detail="Item not found")
    questions = create_questions.questions
    quizzes[quiz_id].questions += questions
    return {"quiz_id": quiz_id, "no_of_questions": len(questions)}





