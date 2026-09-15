print("=== ACTIVIDAD 4: OPERACIONES (UPDATE Y DELETE) ===\n")

clase_modificar = session.get(Clase, 1)
if clase_modificar:
    print(f"Antes del UPDATE 1: {clase_modificar.nombre} - Horario: {clase_modificar.horario}, Cupo: {clase_modificar.cupo_max}")
    
    clase_modificar.horario = "Lun y Mié 19:30hs"
    clase_modificar.cupo_max = 18
    session.commit()
    
    print(f"Después del UPDATE 1: {clase_modificar.nombre} - Horario: {clase_modificar.horario}, Cupo: {clase_modificar.cupo_max}\n")

socio_modificar = session.query(Socio).filter(Socio.email == "dibu.martinez@gmail.com").first()
if socio_modificar:
    print(f"Antes del UPDATE 2: {socio_modificar.nombre} {socio_modificar.apellido} - Activo: {socio_modificar.activo}")
    
    socio_modificar.activo = True
    session.commit()
    
    print(f"Después del UPDATE 2: {socio_modificar.nombre} {socio_modificar.apellido} - Activo: {socio_modificar.activo}\n")

inscripcion_eliminar = session.get(Inscripcion, 10)
if inscripcion_eliminar:
    total_antes = session.query(Inscripcion).count()
    
    session.delete(inscripcion_eliminar)
    session.commit()
    
    total_despues = session.query(Inscripcion).count()
    print(f"DELETE realizado: Se eliminó la inscripción ID 10.")
    print(f"Total de inscripciones antes: {total_antes} | Después: {total_despues}\n")

clases_a_actualizar = session.query(Clase).filter(Clase.cupo_max < 15).all()

print("UPDATE Masivo (Aumentar cupo a clases de cupo < 15):")
for c in clases_a_actualizar:
    print(f" - {c.nombre}: Cupo previo = {c.cupo_max}")
    c.cupo_max += 5

session.commit()

print("\nValores post UPDATE masivo:")
for c in clases_a_actualizar:
    print(f" - {c.nombre}: Nuevo cupo = {c.cupo_max}")
