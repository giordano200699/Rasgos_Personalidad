create table usuario (
  usuarioId integer,
  nombres varchar(100),
  apellidos varchar(100),
  edad integer
 );

INSERT INTO public.usuario(
	usuarioid, nombres, apellidos, edad)
	VALUES (1, 'Giordano de Jesus', 'Barbieri Lizama', 20);