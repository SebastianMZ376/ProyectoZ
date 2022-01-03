from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,ForeignKey,Float
db=SQLAlchemy()

class Usuarios(db.Model):
    tablename = 'Usuarios'
    idUsuario = Column(Integer,primary_key=True)
    Telefono = Column(String,nullable=False)
    No_Salon= Column(String,nullable=False)
    No_Edificio = Column(String,nulleable=False)
    Correo_Electronico = Column(String,nulleable=False)
    Contraseña = (String,nulleable=False)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividuall(self, id):
        return Categoria.query.get(id)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        detped = self.consultaIndividuall(id)
        db.session.delete(detped)
        db.session.commit()

class Pedidos(db.Model):
    tablename = 'Pedidos'
    Id_pedido = Column(Integer,primary_key=True)
    Id_edifico = Column(Integer,ForeignKey('Usuarios.'))
    Id_vendedor = Column(Integer,nulleable=True)



