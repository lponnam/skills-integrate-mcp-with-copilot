"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pathlib import Path
from .db import engine, Base, get_db
from .models import Activity, Student, Signup
from sqlalchemy.orm import Session
import os

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount static files
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=current_dir / "static"), name="static")


@app.on_event("startup")
def startup_event():
    # Create DB tables
    Base.metadata.create_all(bind=engine)
    # Seed sample activities if none exist
    db = next(get_db())
    if not db.query(Activity).first():
        samples = [
            {"name": "Chess Club", "description": "Learn strategies and compete in chess tournaments", "schedule": "Fridays, 3:30 PM - 5:00 PM", "max_participants": 12},
            {"name": "Programming Class", "description": "Learn programming fundamentals and build software projects", "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM", "max_participants": 20},
            {"name": "Gym Class", "description": "Physical education and sports activities", "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM", "max_participants": 30}
        ]
        for s in samples:
            act = Activity(**s)
            db.add(act)
        db.commit()


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities(db: Session = Depends(lambda: next(get_db()))):
    acts = db.query(Activity).all()
    result = {}
    for a in acts:
        result[a.name] = {
            "description": a.description,
            "schedule": a.schedule,
            "max_participants": a.max_participants,
            "participants": [s.student.email for s in a.signups]
        }
    return result


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str, db: Session = Depends(lambda: next(get_db()))):
    # Validate activity exists
    activity = db.query(Activity).filter(Activity.name == activity_name).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Ensure student exists or create
    student = db.query(Student).filter(Student.email == email).first()
    if not student:
        student = Student(email=email)
        db.add(student)
        db.commit()
        db.refresh(student)

    # Check existing signup
    existing = db.query(Signup).filter(Signup.activity_id == activity.id, Signup.student_id == student.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Student is already signed up")

    # Check capacity
    if activity.max_participants and len(activity.signups) >= activity.max_participants:
        raise HTTPException(status_code=400, detail="Activity is full")

    signup = Signup(activity_id=activity.id, student_id=student.id)
    db.add(signup)
    db.commit()
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str, db: Session = Depends(lambda: next(get_db()))):
    activity = db.query(Activity).filter(Activity.name == activity_name).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    student = db.query(Student).filter(Student.email == email).first()
    if not student:
        raise HTTPException(status_code=400, detail="Student is not signed up for this activity")

    signup = db.query(Signup).filter(Signup.activity_id == activity.id, Signup.student_id == student.id).first()
    if not signup:
        raise HTTPException(status_code=400, detail="Student is not signed up for this activity")

    db.delete(signup)
    db.commit()
    return {"message": f"Unregistered {email} from {activity_name}"}
