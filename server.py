from flask import (render_template)
import connexion
from sqlalchemy import create_engine,Column, Integer, String, ForeignKey,MetaData,Table,select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Usuario(Base):
	__tablename__ = "usuario"

	usuarioId = Column('usuarioid',Integer, primary_key=True)
	nombres = Column('nombres',String)
	apellidos = Column('apellidos',String)
	edad = Column('edad',Integer)

engine = create_engine('postgresql://postgres:contra20105@localhost/rasgos')
connection = engine.connect()
metadata = MetaData()
usuarioTabla = Table('usuario', metadata, autoload=True, autoload_with=engine)
query = select([usuarioTabla])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)


# Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)

# session = Session()

# usuarios = session.query(Usuario).all()
# for usuario in usuarios:
# 	print(usuario.nombres)

# session.close()


app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route('/')
def vistaInicial():
	return render_template('vistaInicial.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)