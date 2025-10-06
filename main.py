from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel
quizzes = []
class Option(BaseModel):
    id: int
    text: str
class QuestionOut(BaseModel):
    id: int
    text: str
    options: List[Option] = []

class Question(BaseModel):
    text: str
    options: List[Option] = []
    correct_option_id: int

class Quiz(BaseModel):
    id: int
    title: str
    questions: dict[int, Question] = {}

class CreateQuiz(BaseModel):
    title: str

class CreateQuestions(BaseModel):
    quiz_id: int
    questions: dict[int, Question] = {} #List[Question] = []
class Response(BaseModel):
    question_id: int
    selected_option: int

class QuizResponse(BaseModel):
    quiz_id: int
    question_and_response: List[Response]

app = FastAPI()

@app.get("/fetch/{quiz_id}")
def fetch(quiz_id: int):
    if quiz_id < 0 or quiz_id >= len(quizzes):
        raise HTTPException(status_code=404, detail="Item not found")

    questions = quizzes[quiz_id].questions
    return [
            QuestionOut(id=id, text=q.text, options=q.options) for id,q in questions.items()
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
    quizzes[quiz_id].questions.update(questions)
    return {"quiz_id": quiz_id, "no_of_questions": len(questions)}

@app.post("/submit")
def submit_answers(answers: QuizResponse):
    quiz_id = answers.quiz_id
    question_and_response = answers.question_and_response
    if quiz_id<0:
        return HTTPException(status_code=400, details="Invalid quiz")
    if quiz_id<0 or quiz_id>=len(quizzes):
        return HTTPException(status_code=404, detail="Item not found")
    
    quiz = quizzes[quiz_id]
    total = len(question_and_response)
    if len(quiz.questions)!=total:
        print(answers,quiz.questions)
        return HTTPException(status_code=400, detail="Invalid submission")
    score = 0
    for i in range(total): 
        score += question_and_response[i].selected_option == quiz.questions[i].correct_option_id
    return {"score": score, "total": total} 
