from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    name:str
    id:int
    grade:int

students =[
    Student(id=1 , name="Aziz", grade=100),
    Student(id=2 , name="ali" , grade=95),
]



@app.get("/students/")
async def read_students():
    return students

@app.post("/students/")
async def create_student(newStudent: Student):
    students.append(newStudent)
    return  newStudent

@app.put("/students/{std_id}")
async def update_student(std_id:int , updated_student: Student):
    for index, student in enumerate(students):
        if std_id == student.id:
            students[index] = updated_student
            return updated_student
    return {"error":"Student not found"}

@app.delete("/students/{std_id}")
async def delete_student(std_id: int):
    for index, student in enumerate(students):
        if std_id == student.id:
            del students[index]
            return {"message": "Student deleted successfully"}
    return {"error": "Student not found"}


