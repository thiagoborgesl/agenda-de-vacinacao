from app import app
from flask import render_template

@app.route('/consulta/vacinas')
def vaccines():
    return render_template('newvaccines.html', title='Consulta Vacina')

@app.route('/consulta/usuarios')
def users():
    return render_template('users.html', title='Consulta Usuarios')

@app.route('/consulta/agendas')
def schedules():
    return render_template('schedules.html', title='Consulta Agendas')

@app.route('/consulta/alergias')
def allergies():
    return render_template('newallergy.html', title='Consulta Alergia')