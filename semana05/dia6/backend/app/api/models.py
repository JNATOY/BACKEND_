from utils.db import db
from sqlalchemy.orm import relationship


class Categoria(db.Model):
    __tablename__ = "tbl_categoria"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    imagen = db.Column(db.String(254), nullable=True)

    def __init__(self, nombre):
        self.nombre = nombre

    @staticmethod
    def get_all():
        return Categoria.query.all()

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Categoria.query.get(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Plato(db.Model):
    __tablename__ = "tbl_plato"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    precio = db.Column(db.Double, default=0)
    imagen = db.Column(
        db.String(254),
        default="https://img.freepik.com/vector-premium/icono-parrilla-pollo-negro-simbolo-ilustracion-pollo-caliente-signo-vector-alimentos_744955-457.jpg",
    )
    categoria_id = db.Column(
        db.Integer, db.ForeignKey("tbl_categoria.id"), nullable=True
    )
    categoria = relationship("Categoria", backref="platos")

    def __init__(self, nombre):
        self.nombre = nombre

    @staticmethod
    def get_all():
        return Plato.query.all()

    @staticmethod
    def get_by_id(id):
        return Plato.query.get(id)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Usuario(db.Model):
    __tablename__ = "tbl_usuario"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(254), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)

    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
