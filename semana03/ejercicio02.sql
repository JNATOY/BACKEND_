-- seleccionamos la base de datos
use colegio;

-- insertar datos en nuestra tabla
insert into alumnos (nombre,email) values('juan ñato','jcnatoyepez@gmail.com');

-- mostrar los registros
select * from alumnos;

-- RETO
-- crear tabla experiencia y estudios donde registremos la experiencia laboral y estudios para nuestro cv 
-- usar los campos que crean convenientes e insertar datos

insert into experiencia (puesto laboral,empresa,año) values('desarrollador web','IBM', '2022');

insert into estudios (Nivel,Institucion,Titulo) values('diplomado','UTP', 'BOOTCAM FULL STUCK');

select * from experiencia;
select * from estudios;

CREATE TABLE estudios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nivel VARCHAR(50) NOT NULL,
    institucion VARCHAR(100) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    descripcion TEXT
    
    CREATE TABLE `alumnos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `biografia` text,
  PRIMARY KEY (`id`)
);