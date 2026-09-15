engine = create_engine('sqlite:///:memory:', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


instructores = [
    Instructor(nombre="Martín", apellido="Palermo", especialidad="Spinning", activo=True),
    Instructor(nombre="Luciana", apellido="Aymar", especialidad="Crossfit", activo=True),
    Instructor(nombre="Emanuel", apellido="Ginóbili", especialidad="Funcional", activo=True),
    Instructor(nombre="Paula", apellido="Pareto", especialidad="Judo", activo=True),
    Instructor(nombre="Guillermo", apellido="Coria", especialidad="Musculación", activo=False),
    Instructor(nombre="Gabriela", apellido="Sabatini", especialidad="Yoga", activo=True),
    Instructor(nombre="Sergio", apellido="Martínez", especialidad="Boxeo", activo=True),
    Instructor(nombre="Marcela", apellido="Acuña", especialidad="Kickboxing", activo=False),
    Instructor(nombre="Fabricio", apellido="Oberto", especialidad="Pilates", activo=True),
    Instructor(nombre="Magdalena", apellido="Aicega", especialidad="Zumba", activo=True)
]
session.add_all(instructores)
session.commit()

clases = [
    Clase(nombre="Spinning Intenso", horario="Lun y Mié 18:00hs", cupo_max=15, instructor_id=1),
    Clase(nombre="Crossfit WOD", horario="Mar y Jue 19:00hs", cupo_max=10, instructor_id=2),
    Clase(nombre="Funcional HIIT", horario="Lun, Mié y Vie 09:00hs", cupo_max=20, instructor_id=3),
    Clase(nombre="Judo Inicial", horario="Vie 17:00hs", cupo_max=12, instructor_id=4),
    Clase(nombre="Yoga Flow", horario="Mar y Jue 08:00hs", cupo_max=15, instructor_id=6),
    Clase(nombre="Boxeo Recreativo", horario="Lun y Mié 20:00hs", cupo_max=10, instructor_id=7),
    Clase(nombre="Pilates Mat", horario="Sáb 10:00hs", cupo_max=8, instructor_id=9),
    Clase(nombre="Zumba Fitness", horario="Mar y Jue 18:00hs", cupo_max=25, instructor_id=10),
    Clase(nombre="Spinning Suave", horario="Sáb 11:00hs", cupo_max=15, instructor_id=1),
    Clase(nombre="Crossfit Avanzado", horario="Lun y Mié 21:00hs", cupo_max=8, instructor_id=2)
]
session.add_all(clases)
session.commit()

socios = [
    Socio(nombre="Lionel", apellido="Messi", email="leo.messi@gmail.com", activo=True),
    Socio(nombre="Antonela", apellido="Roccuzzo", email="anto.roccuzzo@gmail.com", activo=True),
    Socio(nombre="Angel", apellido="Di Maria", email="fideo.dimaria@gmail.com", activo=True),
    Socio(nombre="Rodrigo", apellido="De Paul", email="rodri.depaul@gmail.com", activo=True),
    Socio(nombre="Emiliano", apellido="Martínez", email="dibu.martinez@gmail.com", activo=False),
    Socio(nombre="Alexis", apellido="Mac Allister", email="alexis.mac@gmail.com", activo=True),
    Socio(nombre="Julián", apellido="Álvarez", email="araña.alvarez@gmail.com", activo=True),
    Socio(nombre="Enzo", apellido="Fernández", email="enzo.f@gmail.com", activo=False),
    Socio(nombre="Lautaro", apellido="Martínez", email="toro.martinez@gmail.com", activo=True),
    Socio(nombre="Nicolas", apellido="Otamendi", email="ota.nicolas@gmail.com", activo=False)
]
session.add_all(socios)
session.commit()

inscripciones = [
    Inscripcion(socio_id=1, clase_id=1),
    Inscripcion(socio_id=1, clase_id=2),
    Inscripcion(socio_id=2, clase_id=1),
    Inscripcion(socio_id=2, clase_id=5),
    Inscripcion(socio_id=3, clase_id=3),
    Inscripcion(socio_id=4, clase_id=6),
    Inscripcion(socio_id=6, clase_id=2),
    Inscripcion(socio_id=7, clase_id=10),
    Inscripcion(socio_id=9, clase_id=8),
    Inscripcion(socio_id=9, clase_id=9)
]
session.add_all(inscripciones)
session.commit()



print(f"Total Instructores: {session.query(Instructor).count()}")
print(f"Total Clases: {session.query(Clase).count()}")
print(f"Total Socios: {session.query(Socio).count()}")
print(f"Total Inscripciones: {session.query(Inscripcion).count()}\n")

print("MUESTRA DE CLASES ACTIVAS")
clases_db = session.query(Clase).limit(5).all()
for c in clases_db:
    print(f"Clase: {c.nombre} | Instructor: {c.instructor.nombre} {c.instructor.apellido} (Especialidad: {c.instructor.especialidad})")

session.close()