from app import db


class Vacina(db.Model):
    __tablename__ = "vacinas"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(60))
    descricao = db.Column(db.String(200))
    doses = db.Column(db.Integer, nullable=False)
    periodicidade = db.Column(db.Integer)
    intervalo = db.Column(db.Integer)

    def __repr__(self):
        rep = 'Vacina = ' + self.titulo + ',' + self.descricao + ',' + self.doses + ',' + self.periodicidade + ',' + self.intervalo
        return rep


class Agenda(db.Model):
    __tablename__ = "agendas"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime)
    hora = db.Column(db.Time)
    situacao = db.Column(db.String(10))
    data_situacao = db.Column(db.DateTime)
    observacoes = db.Column(db.String(20))


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60))
    data_nascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String(1))
    lagradouro = db.Column(db.String(60))
    numero = db.Column(db.Integer)
    setor = db.Column(db.String(40))
    cidade = db.Column(db.String(40))
    uf = db.Column(db.String(2))


class Alergia(db.Model):
    __tablename__ = "alergias"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))