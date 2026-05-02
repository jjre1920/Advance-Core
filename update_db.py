import sqlite3

conn = sqlite3.connect('advance_data.db')
cursor = conn.cursor()

try:
    # Intentamos añadir la columna 'status' por si no existe
    cursor.execute("ALTER TABLE activos ADD COLUMN status TEXT DEFAULT 'APROBADO'")
    print("[!] ADVANCE: Columna de seguridad añadida con éxito.")
except sqlite3.OperationalError:
    # Si ya existe, simplemente aseguramos que todo sea APROBADO
    print("[!] ADVANCE: La estructura ya era correcta.")

# Aseguramos que todo lo anterior sea visible para los vacacionistas
cursor.execute("UPDATE activos SET status = 'APROBADO'")

conn.commit()
conn.close()
print("--- CONTROL FINALIZADO: Todo el inventario está en línea y visible ---")
