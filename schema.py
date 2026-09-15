import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Instructor(Base):
    __tablename__ = 'instructores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    activo = Column(Boolean, default=True)

    clases = relationship("Clase", back_populates="instructor")

class Clase(Base):
    __tablename__ = 'clases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    cupo_max = Column(Integer, nullable=False)
    instructor_id = Column(Integer, ForeignKey('instructores.id'), nullable=False)

    instructor = relationship("Instructor", back_populates="clases")
    inscripciones = relationship("Inscripcion", back_populates="clase")

class Socio(Base):
    __tablename__ = 'socios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    activo = Column(Boolean, default=True)

    inscripciones = relationship("Inscripcion", back_populates="socio")

class Inscripcion(Base):
    __tablename__ = 'inscripciones'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime, default=datetime.datetime.now)
    socio_id = Column(Integer, ForeignKey('socios.id'), nullable=False)
    clase_id = Column(Integer, ForeignKey('clases.id'), nullable=False)

    socio = relationship("Socio", back_populates="inscripciones")
    clase = relationship("Clase", back_populates="inscripciones")
    