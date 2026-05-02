from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = 'advance_core_key'
DB_FILE = 'advance_data.db'
PASSWORD_MAESTRA = 'advance2026'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'auth' not in session:
            # Si no hay sesión, mandarlo al login con un mensaje implícito
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    conn = sqlite3.connect(DB_FILE); conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activos WHERE status = 'APROBADO' ORDER BY id DESC")
    activos = cursor.fetchall()
    conn.close()
    return render_template('index.html', activos=activos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('password') == PASSWORD_MAESTRA:
            session['auth'] = True
            return redirect(url_for('socio'))
        else:
            return "CLAVE INCORRECTA - ACCESO DENEGADO"
    return '''
        <body style="background:#000; color:#0f8; display:flex; justify-content:center; align-items:center; height:100vh; font-family:sans-serif;">
            <form method="post" style="border:2px solid #0f8; padding:50px; border-radius:20px; text-align:center; box-shadow: 0 0 20px #0f8;">
                <h1 style="letter-spacing:10px;">ADVANCE</h1>
                <p style="color:#555;">SISTEMA DE CONTROL DE SOCIOS</p>
                <input type="password" name="password" placeholder="PASSWORD" style="padding:15px; background:#111; border:1px solid #333; color:#fff; width:100%; border-radius:10px;"><br><br>
                <button type="submit" style="background:#0f8; color:#000; padding:15px 30px; border:none; border-radius:10px; font-weight:bold; cursor:pointer; width:100%;">ENTRAR AL NÚCLEO</button>
            </form>
        </body>
    '''

@app.route('/socio')
@login_required
def socio():
    conn = sqlite3.connect(DB_FILE); conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activos ORDER BY id DESC")
    todos = cursor.fetchall()
    conn.close()
    return render_template('partner.html', activos=todos)

@app.route('/subir_activo', methods=['POST'])
@login_required
def subir_activo():
    conn = sqlite3.connect(DB_FILE); cursor = conn.cursor()
    cursor.execute("INSERT INTO activos (negocio, nombre, precio, ciudad, desc, status) VALUES (?,?,?,?,?,?)",
                   (request.form.get('negocio'), request.form.get('nombre'), request.form.get('precio'), 
                    request.form.get('ciudad'), request.form.get('desc'), 'APROBADO'))
    conn.commit(); conn.close()
    return redirect(url_for('socio'))

@app.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    conn = sqlite3.connect(DB_FILE); cursor = conn.cursor()
    cursor.execute("DELETE FROM activos WHERE id = ?", (id,))
    conn.commit(); conn.close()
    return redirect(url_for('socio'))

@app.route('/logout')
def logout():
    session.pop('auth', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
