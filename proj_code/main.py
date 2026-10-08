from enum import Enum

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()


class Subject(str, Enum):
    Math = "Toan"
    Information_Technology = "Tin"


class Level(str, Enum):
    Thpt = "Thpt"
    Uni = "University"


class Course(BaseModel):
    title: str = Field(min_length=1)
    subject: Subject
    level: Level
    description: str


courses: dict[int, dict] = {
    1: {
        "title": "Calculus",
        "subject": Subject.Math,
        "level": Level.Thpt,
        "description": "The first level",
    },
    2: {
        "title": "Algebra",
        "subject": Subject.Math,
        "level": Level.Thpt,
        "description": "Introduction to algebra",
    },
    3: {
        "title": "Geometry",
        "subject": Subject.Math,
        "level": Level.Thpt,
        "description": "Foundations of geometry",
    },
    4: {
        "title": "Statistics",
        "subject": Subject.Math,
        "level": Level.Uni,
        "description": "Introduction to statistics",
    },
    5: {
        "title": "Linear Algebra",
        "subject": Subject.Math,
        "level": Level.Uni,
        "description": "Vectors and matrices",
    },
    6: {
        "title": "Programming Fundamentals",
        "subject": Subject.Information_Technology,
        "level": Level.Thpt,
        "description": "Basic programming concepts",
    },
    7: {
        "title": "Web Development",
        "subject": Subject.Information_Technology,
        "level": Level.Thpt,
        "description": "Building websites",
    },
    8: {
        "title": "Data Structures",
        "subject": Subject.Information_Technology,
        "level": Level.Uni,
        "description": "Core data structures and algorithms",
    },
    9: {
        "title": "Database Systems",
        "subject": Subject.Information_Technology,
        "level": Level.Uni,
        "description": "Introduction to database design",
    },
    10: {
        "title": "Computer Networks",
        "subject": Subject.Information_Technology,
        "level": Level.Uni,
        "description": "Networking fundamentals",
    },
    11: {
        "title": "Cybersecurity",
        "subject": Subject.Information_Technology,
        "level": Level.Uni,
        "description": "Fundamentals of cybersecurity",
    },
}


# GET - Lấy danh sách khóa học + filter
@app.get("/courses")
def get_courses(
    subject_search: Subject | None = None,
    level: Level | None = None,
    q: str | None = None,
):
    results = list(courses.values())

    if subject_search is not None:
        results = [
            c for c in results
            if c["subject"] == subject_search
        ]

    if q is not None:
        results = [
            c for c in results
            if q.lower() in c["title"].lower()
        ]

    if level is not None:
        results = [
            c for c in results
            if c["level"] == level
        ]

    return results


# GET - Lấy một khóa học theo ID
@app.get("/courses/{course_id}")
def get_course_by_id(course_id: int):

    if course_id not in courses:
        raise HTTPException(
            status_code=404,
            detail="This course ID is not found"
        )

    return courses[course_id]


# POST - Tạo khóa học
@app.post("/courses", status_code=status.HTTP_201_CREATED)
def create_course(course_add: Course):

    # Kiểm tra trùng title
    if any(
        c["title"] == course_add.title
        for c in courses.values()
    ):
        raise HTTPException(
            status_code=409,
            detail="This course title already exists"
        )

    # Tạo ID mới
    course_id = max(courses, default=0) + 1

    # Course object -> dict
    courses[course_id] = course_add.model_dump()

    return courses[course_id]


# PUT - Cập nhật toàn bộ khóa học
@app.put(
    "/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def update_course(course_id: int, course_add: Course):

    # Kiểm tra ID có tồn tại không
    if course_id not in courses:
        raise HTTPException(
            status_code=404,
            detail="This course ID is not found"
        )

    # Kiểm tra title có bị trùng với khóa học khác không
    if any(
        c["title"] == course_add.title
        for id, c in courses.items()
        if id != course_id
    ):
        raise HTTPException(
            status_code=409,
            detail="This course title already exists"
        )

    # Course object -> dict
    courses[course_id] = course_add.model_dump()

    # 204 -> không trả body
    return


# DELETE - Xóa khóa học
@app.delete(
    "/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_course(course_id: int):

    if course_id not in courses:
        raise HTTPException(
            status_code=404,
            detail="This course ID is not found"
        )

    del courses[course_id]

    return