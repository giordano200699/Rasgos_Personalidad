from flask import (render_template)
import connexion
from sqlalchemy import create_engine,Column, Integer, String, ForeignKey,MetaData,Table,select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://postgres:contra20105@localhost/rasgos',echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

session = Session()


class Usuario(Base):
	__tablename__ = "usuario"

	usuarioId = Column('usuarioid',Integer, primary_key=True)
	nombres = Column('nombres',String)
	apellidos = Column('apellidos',String)
	edad = Column('edad',Integer)

	def __repr__(self):
		return 'Id = '+str(self.usuarioId)+' nombres = '+self.nombres+' apellidos = '+self.apellidos+' edad = '+str(self.edad)



nuevoUsuario = Usuario(nombres='Giordano',apellidos='Barbieri Lizama',edad=20)
session.add_all([nuevoUsuario])
usuarioBuscado = session.query(Usuario).filter_by(nombres='Giordano').first() 
print(usuarioBuscado)

#session.rollback()
session.commit()


#print(session.new)
#print(nuevoUsuario is usuarioBuscado)
#print(nuevoUsuario == usuarioBuscado)


#print(Usuario.__table__)

#Base.metadata.create_all(engine)
#print(Base.metadata)

#connection = engine.connect()
#metadata = MetaData()
#usuarioTabla = Table('usuario', metadata, autoload=True, autoload_with=engine)
#query = select([usuarioTabla])
#ResultProxy = connection.execute(query)
#ResultSet = ResultProxy.fetchall()
#print(ResultSet)


# Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)

# session = Session()

# usuarios = session.query(Usuario).all()
# for usuario in usuarios:
# 	print(usuario.nombres)

# session.close()
# comentario


app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route('/')
def vistaInicial():
	return render_template('vistaInicial.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)