from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, IntegerField, SubmitField, validators, FieldList, FormField

class VaccineForm(FlaskForm):
    title = StringField('title', validators=[validators.input_required()])
    description = StringField('description')
    doses = IntegerField(validators=[validators.input_required()])
    frequency = IntegerField(validators=[validators.input_required()])
    gap = IntegerField(validators=[validators.input_required()])
    submit = SubmitField('Enviar')

class AllergyForm(FlaskForm):
    allergy = StringField('allergy', validators=[validators.input_required()])
    submit = SubmitField('Enviar')

class UserForm(FlaskForm):
    username = StringField('username', validators=[validators.input_required()])
    gender = SelectField('sexo', choices=[('M', 'Masculino'),('F', 'Feminino')])
    birthdate = DateField()
    street = StringField('lagradouro')
    number = IntegerField()
    district = StringField('setor')
    city = StringField('cidade')
    state = SelectField('sexo', choices=[('AC', 'Acre'),('AL', 'Alagoas'),('AP', 'Amapá'),('AM', 'Amazonas')
                                        ,('BA', 'Bahia'),('CE', 'Ceará'),('DF', 'Distrito Federal'),('ES', 'Espírito Santo')
                                        ,('GO', 'Goiás'),('MA', 'Maranhão'),('MT', 'Mato Grosso'),('MS', 'Mato Grosso do Sul')
                                        ,('MG', 'Minas Gerais'),('PA', 'Pará'),('PB', 'Paraíba'),('PR', 'Paraná')
                                        ,('PE', 'Pernambuco'),('PI', 'Piauí'),('RJ', 'Rio de Janeiro'),('RN', 'Rio Grande do Norte')
                                        ,('RS', 'Rio Grande do Sul'),('RO', 'Rondonia'),('RR', 'Roraima'),('SC', 'Santa Catarina')
                                        ,('SP', 'Sao Paulo'),('SE', 'Sergipe'),('TO', 'Tocantins')])
    allergies = FieldList(StringField('allergy', validators=[validators.input_required()]))
    submit = SubmitField('Enviar')   