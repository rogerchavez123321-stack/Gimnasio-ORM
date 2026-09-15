from sqlalchemy import or_

print("=== ACTIVIDAD 3: CONSULTAS ===\n")

socios_activos = session.query(Socio).filter(Socio.activo == True).all()
print(f"1a. Socios activos ({len(socios_activos)}):")
for s in socios_activos:
    print(f" - {s.nombre} {s.apellido}")

clases_grandes = session.query(Clase).filter(Clase.cupo_max > 12).all()
print(f"\n1b. Clases con cupo mayor a 12 ({len(clases_grandes)}):")
for c in clases_grandes:
    print(f" - {c.nombre} (Cupo: {c.cupo_max})")

instructores_inactivos = session.query(Instructor).filter(Instructor.activo != True).all()
print(f"\n1c. Instructores inactivos ({len(instructores_inactivos)}):")
for i in instructores_inactivos:
    print(f" - {i.nombre} {i.apellido}")

instructores_or = session.query(Instructor).filter(
    or_(Instructor.especialidad == "Spinning", Instructor.especialidad == "Crossfit")
).all()

print(f"\n2. Instructores de Spinning o Crossfit ({len(instructores_or)}):")
for i in instructores_or:
    print(f" - {i.nombre} {i.apellido} ({i.especialidad})")

socios_martinez = session.query(Socio).filter(Socio.apellido.startswith("M")).all()

print(f"\n3. Socios cuyo apellido empieza con 'M' ({len(socios_martinez)}):")
for s in socios_martinez:
    print(f" - {s.nombre} {s.apellido}")

clase_mayor_cupo = session.query(Clase).order_by(Clase.cupo_max.desc()).first()

print(f"\n4. Clase con mayor cupo disponible:")
print(f" - {clase_mayor_cupo.nombre} con {clase_mayor_cupo.cupo_max} lugares.")
