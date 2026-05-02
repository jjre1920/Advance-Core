import sqlite3

conn = sqlite3.connect('advance_data.db')
cursor = conn.cursor()

# Esta instrucción le pone el sello de APROBADO a todo lo que ya existía
cursor.execute("UPDATE activos SET status = 'APROBADO' WHERE status IS NULL OR status = 'PENDIENTE'")

conn.commit()
conn.close()
print("--- CONTROL ADVANCE: Todos los activos han sido APROBADOS y son visibles ahora ---")
