from app import app, db
from flask import render_template, flash, url_for, redirect
from app.models.forms import UserForm, AllergyForm, VaccineForm
from app.models.tables import Vacina, Agenda, Usuario, Alergia

@app.route('/')
def index():
   return render_template('index.html', title='Menu Principal')

@app.route('/cadastro/vacinas', methods=['GET', 'POST'])
def newVaccines():
    form = VaccineForm()  
    if form.validate_on_submit():
        vaccine = Vacina(titulo=form.title.data, descricao=form.description.data, doses=form.doses.data, periodicidade=form.frequency.data, intervalo=form.gap.data)
        db.session.add(vaccine)
        db.session.commit()
        return redirect(url_for('newVaccines'))
    return render_template('newvaccines.html', title='Cadastro Vacina', form=form)

@app.route('/cadastro/usuarios', methods=['GET', 'POST'])
def newUsers():
    allergies = Alergia.query.all()
    print(allergies)
    form = UserForm(allergies=allergies)
    return render_template('newuser.html', title='Cadastro Usuarios', form=form)

@app.route('/cadastro/agendas')
def newSchedules():
    return render_template('newschedule.html', title='Cadastro Agendas')

@app.route('/cadastro/alergias', methods=['GET', 'POST'])
def newAllergies():
    form = AllergyForm()
    if form.validate_on_submit():
        allergy = Alergia(nome=form.allergy.data)
        db.session.add(allergy)
        db.session.commit()
        flash('Cadastro feito com sucesso', 'success')
        return redirect(url_for('newAllergies'))
    return render_template('newvallergy.html', title='Cadastro Alergia', form=form)

