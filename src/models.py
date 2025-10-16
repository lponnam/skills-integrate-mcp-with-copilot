from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True, index=True, nullable=False)
    description = Column(Text)
    schedule = Column(String(200))
    max_participants = Column(Integer, default=0)

    signups = relationship("Signup", back_populates="activity", cascade="all, delete-orphan")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(200), unique=True, index=True, nullable=False)
    name = Column(String(200), nullable=True)
    grade = Column(String(50), nullable=True)

    signups = relationship("Signup", back_populates="student", cascade="all, delete-orphan")


class Signup(Base):
    __tablename__ = "signups"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    activity = relationship("Activity", back_populates="signups")
    student = relationship("Student", back_populates="signups")
