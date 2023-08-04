show databases;

-- para crear base de datos
create database if exists colegio;

-- para eliminar base de datos
drop database if not exists colegio;

-- para seleccionar una base de datos
use colegio;

-- mostrar tablas
show tables;

-- para crear un tabla
create table alumnos(
	nombre varchar(255),
	email varchar(100)
);

-- modificar una tabla para agregar un campo
alter table alumnos 
add column biografia text;

-- agregar un primary key
alter table alumnos
add column id int(11)not null primary key auto_increment first;
-- modificar una columna
alter table alumnos 
modify nombre varchar (255) not null;
-- agregar una restriccion de valor unico
alter table alumnos
add unique(email);
-- para mostrar la estructura de una tabla 
describe alumnos;

-- para eliminar una tabla
drop table alumnos;

-- creacion de tabla desde el inicio
-- colegio.alumnos definition

-- colegio.alumnos definition

CREATE TABLE `alumnos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `biografia` text,
  PRIMARY KEY (`id`)
);





